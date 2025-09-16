# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _
from .wix_client import WixClient

def sync_item_to_wix(doc, method=None):
    """
    Sync Frappe Item to Wix Product
    Called when an Item is created or updated
    """
    # Skip if sync is disabled or item is disabled
    if doc.disabled or not should_sync_item(doc):
        return
    
    try:
        # Initialize Wix client
        wix_client = WixClient()
        
        # Prepare product data for Wix
        product_data = prepare_wix_product_data(doc)
        
        # Check if product already exists in Wix
        wix_product_id = doc.get('wix_product_id')
        
        if wix_product_id:
            # Update existing product
            result = wix_client.update_product(wix_product_id, product_data)
            frappe.msgprint(_(f"Product '{doc.item_name}' updated in Wix successfully"))
        else:
            # Create new product
            result = wix_client.create_product(product_data)
            
            # Store Wix product ID in Frappe
            if result and 'product' in result and 'id' in result['product']:
                doc.db_set('wix_product_id', result['product']['id'], update_modified=False)
                frappe.msgprint(_(f"Product '{doc.item_name}' created in Wix successfully"))
        
        # Log successful sync
        create_sync_log(doc, "Success", "Product synced successfully")
        
    except Exception as e:
        # Log error
        error_msg = str(e)
        create_sync_log(doc, "Failed", error_msg)
        frappe.log_error(f"Wix sync failed for item {doc.name}: {error_msg}", "Wix Sync Error")
        
        # Don't break the transaction, just log the error
        frappe.msgprint(_(f"Failed to sync product '{doc.item_name}' to Wix: {error_msg}"), alert=True)

def should_sync_item(doc):
    """
    Determine if an item should be synced to Wix
    """
    # Add your business logic here
    # For example, only sync items that are stock items and not variants
    if doc.has_variants or doc.variant_of:
        return False
    
    # You can add more conditions here based on your requirements
    # For example, only sync items from certain item groups
    # if doc.item_group not in ['Products', 'Services']:
    #     return False
    
    return True

def prepare_wix_product_data(item_doc):
    """
    Prepare product data in Wix format from Frappe Item
    """
    product_data = {
        "product": {
            "name": item_doc.item_name or item_doc.item_code,
            "description": item_doc.description or "",
            "sku": item_doc.item_code,
            "visible": not item_doc.disabled,
            "productType": "physical",
            "priceData": {
                "currency": frappe.defaults.get_global_default('currency') or 'USD',
                "price": item_doc.standard_rate or 0
            },
            "weight": item_doc.weight_per_unit or 0,
            "costAndProfitData": {
                "itemCost": item_doc.valuation_rate or 0
            }
        }
    }
    
    # Add brand if available
    if item_doc.brand:
        product_data["product"]["brand"] = item_doc.brand
    
    # Add stock information if it's a stock item
    if item_doc.is_stock_item:
        # Get current stock quantity (this would need to be implemented based on your requirements)
        stock_qty = get_item_stock_qty(item_doc.item_code)
        product_data["product"]["manageVariants"] = False
        product_data["product"]["productOptions"] = []
        
        # Add inventory tracking
        if stock_qty is not None:
            product_data["product"]["stock"] = {
                "trackQuantity": True,
                "quantity": stock_qty,
                "inStock": stock_qty > 0
            }
    
    # Add image if available
    if item_doc.image:
        # You might need to convert relative URL to absolute URL
        image_url = frappe.utils.get_url(item_doc.image)
        product_data["product"]["media"] = {
            "mainMedia": {
                "image": {
                    "url": image_url
                }
            }
        }
    
    return product_data

def get_item_stock_qty(item_code):
    """
    Get current stock quantity for an item
    """
    try:
        from erpnext.stock.utils import get_latest_stock_qty
        return get_latest_stock_qty(item_code)
    except ImportError:
        # If ERPNext is not available, return None
        return None

def create_sync_log(item_doc, status, message):
    """
    Create a sync log entry
    """
    try:
        sync_log = frappe.get_doc({
            'doctype': 'Wix Sync Log',
            'item_code': item_doc.item_code,
            'item_name': item_doc.item_name,
            'status': status,
            'message': message,
            'wix_product_id': item_doc.get('wix_product_id'),
            'sync_time': frappe.utils.now()
        })
        sync_log.insert(ignore_permissions=True)
    except Exception as e:
        # If sync log creation fails, just log it
        frappe.log_error(f"Failed to create sync log: {str(e)}", "Sync Log Error")

# Whitelisted function for manual sync
@frappe.whitelist()
def manual_sync_item(item_code):
    """
    Manually sync a specific item to Wix
    """
    item_doc = frappe.get_doc('Item', item_code)
    sync_item_to_wix(item_doc)
    return {'status': 'success', 'message': f'Item {item_code} sync initiated'}

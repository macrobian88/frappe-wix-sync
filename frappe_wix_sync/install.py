"""
Custom fields to be added to existing DocTypes
Run this using: bench execute frappe_wix_sync.install.add_custom_fields
"""

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def add_custom_fields():
    """Add custom fields for Wix integration"""
    
    custom_fields = {
        "Item": [
            {
                "fieldname": "wix_section_break",
                "label": "Wix Integration",
                "fieldtype": "Section Break",
                "insert_after": "brand",
                "collapsible": 1
            },
            {
                "fieldname": "wix_product_id",
                "label": "Wix Product ID",
                "fieldtype": "Data",
                "insert_after": "wix_section_break",
                "read_only": 1,
                "description": "Auto-generated Wix Product ID when synced to Wix store"
            },
            {
                "fieldname": "sync_to_wix",
                "label": "Sync to Wix",
                "fieldtype": "Check",
                "insert_after": "wix_product_id",
                "default": 1,
                "description": "Enable/disable automatic sync to Wix store"
            },
            {
                "fieldname": "wix_last_sync",
                "label": "Last Wix Sync",
                "fieldtype": "Datetime",
                "insert_after": "sync_to_wix",
                "read_only": 1,
                "description": "Last successful sync timestamp"
            }
        ]
    }
    
    create_custom_fields(custom_fields)
    frappe.db.commit()
    print("Custom fields added successfully!")

def remove_custom_fields():
    """Remove custom fields for Wix integration"""
    
    fields_to_remove = [
        "wix_section_break",
        "wix_product_id", 
        "sync_to_wix",
        "wix_last_sync"
    ]
    
    for fieldname in fields_to_remove:
        if frappe.db.exists("Custom Field", {"dt": "Item", "fieldname": fieldname}):
            frappe.delete_doc("Custom Field", {"dt": "Item", "fieldname": fieldname})
    
    frappe.db.commit()
    print("Custom fields removed successfully!")

if __name__ == "__main__":
    add_custom_fields()

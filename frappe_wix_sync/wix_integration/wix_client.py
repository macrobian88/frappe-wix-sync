# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
import requests
import json
from frappe.utils import get_site_config

class WixClient:
    """
    Wix API Client for handling product operations
    """
    
    def __init__(self):
        self.base_url = "https://www.wixapis.com/stores/v1"
        self.site_id = self.get_wix_site_id()
        self.api_key = self.get_wix_api_key()
        self.access_token = self.get_wix_access_token()
        
        if not all([self.site_id, self.api_key, self.access_token]):
            frappe.throw("Wix configuration not found. Please set up Wix API credentials in site config.")
    
    def get_wix_site_id(self):
        """Get Wix Site ID from site config"""
        return frappe.conf.get('wix_site_id') or frappe.db.get_single_value('Wix Settings', 'site_id')
    
    def get_wix_api_key(self):
        """Get Wix API Key from site config"""
        return frappe.conf.get('wix_api_key') or frappe.db.get_single_value('Wix Settings', 'api_key')
    
    def get_wix_access_token(self):
        """Get Wix Access Token from site config"""
        return frappe.conf.get('wix_access_token') or frappe.db.get_single_value('Wix Settings', 'access_token')
    
    def get_headers(self):
        """Get request headers for Wix API"""
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
            'wix-site-id': self.site_id
        }
    
    def create_product(self, product_data):
        """
        Create a product in Wix
        """
        url = f"{self.base_url}/products"
        headers = self.get_headers()
        
        try:
            response = requests.post(url, headers=headers, json=product_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            frappe.log_error(f"Failed to create Wix product: {str(e)}", "Wix API Error")
            raise frappe.ValidationError(f"Failed to create product in Wix: {str(e)}")
    
    def update_product(self, product_id, product_data):
        """
        Update a product in Wix
        """
        url = f"{self.base_url}/products/{product_id}"
        headers = self.get_headers()
        
        try:
            response = requests.patch(url, headers=headers, json=product_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            frappe.log_error(f"Failed to update Wix product: {str(e)}", "Wix API Error")
            raise frappe.ValidationError(f"Failed to update product in Wix: {str(e)}")
    
    def get_product(self, product_id):
        """
        Get a product from Wix
        """
        url = f"{self.base_url}/products/{product_id}"
        headers = self.get_headers()
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            frappe.log_error(f"Failed to get Wix product: {str(e)}", "Wix API Error")
            return None
    
    def delete_product(self, product_id):
        """
        Delete a product from Wix
        """
        url = f"{self.base_url}/products/{product_id}"
        headers = self.get_headers()
        
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            frappe.log_error(f"Failed to delete Wix product: {str(e)}", "Wix API Error")
            return False

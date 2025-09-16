# Frappe Wix Sync

A Frappe application that automatically syncs Items from Frappe/ERPNext with products in Wix e-commerce store.

## Features

- **Automatic Sync**: Automatically creates and updates products in Wix when Items are created or modified in Frappe
- **Real-time Updates**: Uses Frappe hooks to trigger sync immediately after Item operations
- **Configurable**: Easy to configure Wix API credentials
- **Error Logging**: Comprehensive error logging and sync status tracking
- **Manual Sync**: Ability to manually trigger sync for specific items

## Installation

1. Get the app from GitHub:
```bash
bench get-app https://github.com/macrobian88/frappe-wix-sync.git
```

2. Install the app on your site:
```bash
bench --site your-site-name install-app frappe_wix_sync
```

## Configuration

### 1. Wix API Credentials

You need to set up Wix API credentials. You can do this in two ways:

#### Option A: Site Config (Recommended)
Add the following to your `site_config.json`:

```json
{
  "wix_site_id": "your-wix-site-id",
  "wix_api_key": "your-wix-api-key", 
  "wix_access_token": "your-wix-access-token"
}
```

#### Option B: Frappe Single DocType
Create a "Wix Settings" Single DocType with the following fields:
- site_id
- api_key  
- access_token

### 2. Wix API Setup

To get your Wix API credentials:

1. Go to [Wix Developers](https://dev.wix.com/)
2. Create a new app or use an existing one
3. Enable the "Wix Stores" API
4. Get your API key and generate an access token
5. Find your site ID from your Wix dashboard

## How it Works

1. **Item Creation/Update**: When an Item is created or updated in Frappe, the app automatically triggers a sync
2. **Data Mapping**: The app maps Frappe Item fields to Wix Product fields:
   - Item Name → Product Name
   - Item Code → SKU
   - Description → Product Description
   - Standard Rate → Price
   - Brand → Brand
   - Image → Product Image
   - Stock Information → Inventory tracking

3. **Sync Logic**: 
   - Only syncs items that are sales items and not variants
   - Creates new products in Wix for new items
   - Updates existing products when items are modified
   - Stores Wix Product ID in Frappe for future updates

## API

### Manual Sync
You can manually trigger sync for a specific item:

```python
frappe.call({
    method: "frappe_wix_sync.wix_integration.manual_sync_item",
    args: {
        item_code: "ITEM-001"
    }
})
```

## Customization

### Sync Conditions
Modify the `should_sync_item()` function in `sync.py` to customize which items get synced.

### Field Mapping
Update the `prepare_wix_product_data()` function in `sync.py` to change how Frappe fields map to Wix fields.

## Error Handling

- All API errors are logged in Frappe's Error Log
- Sync failures don't break the Item save operation
- Users are notified of sync status via message alerts

## Requirements

- Frappe Framework
- Wix Store with API access
- Valid Wix API credentials

## License

MIT

## Support

For issues and feature requests, please use the GitHub issues tracker.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Changelog

### Version 0.0.1
- Initial release
- Basic Item to Wix Product sync
- Automatic sync on create/update
- Manual sync functionality
- Error logging

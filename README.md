# Frappe Wix Sync

A Frappe application that automatically syncs Items from Frappe/ERPNext with products in Wix e-commerce store.

## Features

- **Automatic Sync**: Automatically creates and updates products in Wix when Items are created or modified in Frappe
- **Real-time Updates**: Uses Frappe hooks to trigger sync immediately after Item operations
- **Configurable**: Easy to configure Wix API credentials and sync settings per item
- **Error Logging**: Comprehensive error logging and sync status tracking
- **Manual Sync**: Ability to manually trigger sync for specific items or bulk sync all items
- **Custom Fields**: Adds Wix-specific fields to Item doctype for better control

## Installation

1. Get the app from GitHub:
```bash
bench get-app https://github.com/macrobian88/frappe-wix-sync.git
```

2. Install the app on your site:
```bash
bench --site your-site-name install-app frappe_wix_sync
```

3. Run bench migrate to apply custom fields:
```bash
bench --site your-site-name migrate
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

## Added Fields

The app automatically adds the following custom fields to the Item DocType:

- **Wix Product ID**: Auto-generated ID when synced to Wix (read-only)
- **Sync to Wix**: Checkbox to enable/disable sync for specific items (default: enabled)
- **Last Wix Sync**: Timestamp of last successful sync (read-only)

## How it Works

1. **Item Creation/Update**: When an Item is created or updated in Frappe, the app automatically triggers a sync if "Sync to Wix" is enabled
2. **Data Mapping**: The app maps Frappe Item fields to Wix Product fields:
   - Item Name → Product Name
   - Item Code → SKU
   - Description → Product Description
   - Standard Rate → Price
   - Brand → Brand
   - Image → Product Image
   - Stock Information → Inventory tracking

3. **Sync Logic**: 
   - Only syncs items where "Sync to Wix" is enabled
   - Skips items that have variants or are variants themselves
   - Creates new products in Wix for new items
   - Updates existing products when items are modified
   - Stores Wix Product ID and last sync timestamp

## API Methods

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

### Bulk Sync
Sync all enabled items:

```python
frappe.call({
    method: "frappe_wix_sync.wix_integration.sync_all_items"
})
```

## Customization

### Sync Conditions
Modify the `should_sync_item()` function in `sync.py` to customize which items get synced.

### Field Mapping
Update the `prepare_wix_product_data()` function in `sync.py` to change how Frappe fields map to Wix fields.

### Custom Fields
Run the following to manually add/remove custom fields:

```bash
# Add custom fields
bench execute frappe_wix_sync.install.add_custom_fields

# Remove custom fields  
bench execute frappe_wix_sync.install.remove_custom_fields
```

## Error Handling

- All API errors are logged in Frappe's Error Log
- Sync failures don't break the Item save operation
- Users are notified of sync status via message alerts
- Last sync timestamp is updated only on successful syncs

## File Structure

```
frappe_wix_sync/
├── __init__.py
├── hooks.py                    # App configuration and hooks
├── install.py                  # Custom field installation
├── modules.txt                 # Module definition
├── config/
│   ├── __init__.py
│   └── desktop.py             # Desktop module configuration
└── wix_integration/
    ├── __init__.py
    ├── wix_client.py          # Wix API client
    ├── sync.py                # Main sync logic
    └── doctype/               # Future DocTypes
        └── __init__.py
```

## Requirements

- Frappe Framework
- Wix Store with API access
- Valid Wix API credentials
- Python requests library

## Troubleshooting

### Common Issues

1. **"Wix configuration not found"**: Make sure you've set up Wix API credentials in site_config.json
2. **API errors**: Check that your Wix API credentials are valid and have proper permissions
3. **Custom fields not showing**: Run `bench migrate` after installation
4. **Sync not triggering**: Check if "Sync to Wix" is enabled for the item

### Debug Mode

Enable debug mode by adding this to site_config.json:
```json
{
  "developer_mode": 1,
  "log_level": "DEBUG"
}
```

## License

MIT

## Support

For issues and feature requests, please use the [GitHub issues tracker](https://github.com/macrobian88/frappe-wix-sync/issues).

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
- Bulk sync functionality  
- Custom fields for sync control
- Error logging and status tracking
- Configurable sync conditions

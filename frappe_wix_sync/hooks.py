# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappe_wix_sync"
app_title = "Frappe Wix Sync"
app_publisher = "Your Company"
app_description = "Sync Frappe Items with Wix Products"
app_email = "developer@yourcompany.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_wix_sync/css/frappe_wix_sync.css"
# app_include_js = "/assets/frappe_wix_sync/js/frappe_wix_sync.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_wix_sync/css/frappe_wix_sync.css"
# web_include_js = "/assets/frappe_wix_sync/js/frappe_wix_sync.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "frappe_wix_sync/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "frappe_wix_sync.utils.jinja_methods",
# 	"filters": "frappe_wix_sync.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "frappe_wix_sync.install.before_install"
# after_install = "frappe_wix_sync.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "frappe_wix_sync.uninstall.before_uninstall"
# after_uninstall = "frappe_wix_sync.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_wix_sync.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Item": {
        "after_insert": "frappe_wix_sync.wix_integration.sync_item_to_wix",
        "on_update": "frappe_wix_sync.wix_integration.sync_item_to_wix"
    }
}

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_wix_sync.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_wix_sync.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_wix_sync.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_wix_sync.tasks.weekly"
# 	],
# 	"monthly": [
# 		"frappe_wix_sync.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappe_wix_sync.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_wix_sync.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappe_wix_sync.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

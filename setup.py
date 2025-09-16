# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="frappe_wix_sync",
    version="0.0.1",
    description="Sync Frappe Items with Wix Products",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Company",
    author_email="developer@yourcompany.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "frappe",
        "requests"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Frappe",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business :: Financial :: Accounting",
    ],
)

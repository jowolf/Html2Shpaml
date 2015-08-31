#!/usr/bin/env python

from distutils.core import setup

setup (
    name         = 'Html2Shpaml',
    packages     = ['html2shpaml','WebElements'],
    version      = '0.2.1',
    description  = 'A forgiving html to shpaml converter.',
    author       = 'Timothy Crosley',
    author_email = 'timothy.crosley@gmail.com',
    url          = 'https://github.com/jowolf/Html2Shpaml',
    download_url = 'https://github.com/jowolf/Html2Shpaml/archive/master.zip',
    license      = "GNU GPLv2",
    #scripts     = ['scripts/html2Shpaml',],
    #install_requires = ['webelements>=1.0.0-beta.2',],
)

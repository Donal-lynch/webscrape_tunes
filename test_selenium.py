# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 08:31:50 2019

@author: Home
"""


from selenium import webdriver
import os

# Setup
gecko = os.path.normpath(r'C:\Users\Home\Documents\Projects\download_certs\gecko_driver\geckodriver')
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')

# Set preferences: 
# 2 main things here are where to download, and to ensure that there are no
# user prompts while downloading.
fp = webdriver.FirefoxProfile()
# 0 means to download to the desktop
# 1 means to download to the default "Downloads" directory
# 2 means to use the directory 
#fp.set_preference("browser.download.folderList", 0)

import os
download_path = ("C:\\Users\\Home\\Desktop\\temp")

fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.dir", download_path) 
fp.set_preference("browser.helperApps.alwaysAsk.force", False)
fp.set_preference("browser.download.manager.showWhenStarting",False)
# This the 'Content-Type' for the midi files:
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/midi");
#fp.set_preference("browser.download.dir", "H:\Downloads") 

# Launch the browser
driver = webdriver.Firefox(firefox_binary=binary,
                           executable_path=gecko+'.exe',
                           firefox_profile = fp)





driver.get('https://thesession.org/tunes/2123')


# find the 'DOWNLOAD' elemnts and the 'midi' elements using css selectors
reveal = driver.find_elements_by_css_selector(".toggle.unrevealed")
downloaders = driver.find_elements_by_css_selector(".listen")

# click the first reveal button and then the midi button
reveal[0].click()
# click the download button now that it is visible
downloaders[0].click()



############################################################################







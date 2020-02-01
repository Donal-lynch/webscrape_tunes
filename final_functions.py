# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:51:42 2020

@author: Home
"""


from selenium import webdriver
import time
#from os import listdir
import os


driver = webdriver.Firefox(firefox_binary=binary,
                           executable_path=gecko+'.exe',
                           firefox_profile = fp)



def get_mid_files(driver, url):
    driver.get(url)
    
    # get all of the buttons which reveal the download buttons
    reveals = driver.find_elements_by_css_selector(".toggle.unrevealed")
    downloaders = driver.find_elements_by_css_selector(".listen")
    
    for i in range(len(reveals)):
        reveals[i].click()
        downloaders[i].click()
        
        # Wait for 5 seconds
        time.sleep(3)
        

#url = 'https://thesession.org/tunes/2123'
#get_mid_files(driver = driver, url = url)


def file_name_to_full_path(directory, file_name):
    # simply takes a directoy path and a file name and combines them into a 
    # path to a file    
    return directory + '\\' + file_name
    

def get_newest_file_name(directory):
    # take a directory as a string and return the name of the
    # newest file in that directory
    
    file_names = os.listdir(directory)
    
    #full_paths = list(map(lambda x:directory + '\\' + x, file_names))
    
    full_paths = [file_name_to_full_path(directory, file_name = f) for f in file_names]
    
    newest_file = max(full_paths, key=os.path.getctime)
    
    newest_file_index = full_paths.index(newest_file)
    
    return file_names[newest_file_index]
    

def rename_newsest_file(directory, new_file_name):
    # take a directory and a new file name.
    # go to that directory and rename the most recently created to new_file_name
    # Nothing returned
    
    newest_file_name = get_newest_file_name(directory)
    
    os.rename(file_name_to_full_path(directory, file_name = newest_file_name),
              file_name_to_full_path(directory, file_name = new_file_name))



#rename_newsest_file(download_path, 'def.mid')




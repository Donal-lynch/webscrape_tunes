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



def get_meta_data(soup_object, index):
    # parse the soup object which comes from thesession
    # index is a number. Each page has a number of versions. index is whcih 
    # version to get the information for.
    # IF index is -1 information on the whole page is returned
    
    if index == -1:
        h1 = soup.h1.get_text()

        # tunesets
        # There is no tag, class or id for the tunesets. Its just in a p tag
        # Just hope that all pages are foramtted the same
        # an alternitive is to check which p tag has the correct words
        
        tunesets_text = soup.find_all('p')[4].get_text()       
        tunesets = int(''.join(re.findall('(?<=added to )\d+(?= tune)', tunesets_text)))
    
        # tunebook
        tunebooks_text = soup.find(id='tunebooking').get_text()
        tunebooks = int(''.join(re.findall('(?<=added to )\d+(?= tune)', tunebooks_text)))

    
        op = [h1, tunesets, tunebooks]
    
    else:
        notes = soup.find_all(class_="notes")[index].get_text()

        # The way these notes are formatted is a bit of a pain. All of the required info is 
        # just floating in the div, it is not in any tags other than the notes div
        
        # As a result just use regex on all these
        #''.join is used to convert a list of 1 string to a string object
        # .strip removes leading and trailing white_space
        
        # Get X
        
        x  = int(''.join(re.findall('(?<=X: )\d+', notes)))
        
        # Get T
        t = ''.join(re.findall('(?<=T:).*', notes)).strip()
        
        # Get R
        r = ''.join(re.findall('(?<=R:).*', notes)).strip()
        
        # Get K
        k = ''.join(re.findall('(?<=K:).*', notes)).strip()
        
        # Get abc notation
        
        # abc comes after K. uses this to build the regex
        regex = '(?<=' + k +'\n' + ')' + '.*$'
        
        # Use re.DOTALL to treat \n as a normal character. Otherwise it treats it as 
        # the end of the string
        abc = re.findall(regex, notes, re.DOTALL)
        
        
        op = [x, t, r, k, abc]    
        
    return op




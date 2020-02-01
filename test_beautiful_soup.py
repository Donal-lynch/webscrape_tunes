# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 20:48:55 2020

@author: Home
"""

import requests
from bs4 import BeautifulSoup
import re


page = requests.get('https://thesession.org/tunes/2123')
page.status_code


soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())



# There are some things to be scraped which are a per page basis, and others 
# which are based on each version.


##################### per page scraping
# title of page
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


#################### per version
notes = soup.find_all(class_="notes")

# The way these notes are formatted is a bit of a pain. All of the required info is 
# just floating in the div, it is not in any tags other than the notes div

# As a result just use regex on all these
#''.join is used to convert a list of 1 string to a string object
# .strip removes leading and trailing white_space

this_notes = notes[0].get_text()
# Get X

x  = int(''.join(re.findall('(?<=X: )\d+', this_notes)))

# Get T
t = ''.join(re.findall('(?<=T:).*', this_notes)).strip()

# Get R
r = ''.join(re.findall('(?<=R:).*', this_notes)).strip()

# Get K
k = ''.join(re.findall('(?<=K:).*', this_notes)).strip()

# Get abc notation

# abc comes after K. uses this to build the regex
regex = '(?<=' + k +'\n' + ')' + '.*$'

# Use re.DOTALL to treat \n as a normal character. Otherwise it treats it as 
# the end of the string
re.findall(regex, this_notes, re.DOTALL)



###########################################

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




#get_meta_data(soup, 3)















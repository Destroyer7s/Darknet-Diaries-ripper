# Darknet-Diaries-ripper
Simple python script to download latest podcasts found on: https://darknetdiaries.com

All that you need to do is run it.

Note: *All audio files downloaded will put in a generated folder ( Darknet Diaries ). It and it's contents will end-up in the directory you run the program from.*


```python



# Import required modules 
from lxml import html 
import requests 
import os
import time



# Request the page 
page = requests.get('https://feeds.megaphone.fm/darknetdiaries') 
  
# Parsing the page 
# (We need to use page.content rather than  
# page.text because html.fromstring implicitly 
# expects bytes as input.) 
tree = html.fromstring(page.content)   
  
# Get element using XPath 
links = tree.xpath('//enclosure[contains(@url,"mp3")]/@url') 
name = tree.xpath('//item/title/text()') 
# Python code to demonstrate readlines() 
  
# Using readlines() 
'''
file1 = open('dark_net_podcast_url_list.txt', 'r') 
Lines = file1.readlines() 
Lines = [line.strip() for line in Lines]
file1.close()
'''


# os.makedirs() method will raise
# an OSError if the directory
# to be created already exists
 
    
# Directory
directory = "Dark Net Diaries"
 
# Parent Directory path
parent_dir = os.path.dirname(os.path.realpath(__file__))
 
# Path
path = os.path.join(parent_dir, directory)
 
# Create the directory

if not os.path.isdir(path):
    os.makedirs(path)
    print("Directory '%s' created" %directory)
os.chdir(path)




CURR_DIR = os.path.dirname(os.path.realpath(__file__))


if (os.path.exists('dark_net_podcast_url_list.txt') == False) or (os.path.isfile('dark_net_podcast_url_list.txt') == False):

    print("Error, couldn't find: dark_net_podcast_url_list.txt")
    makefile = input("Do you want me to make the file for you? (y or n)  ")
    if makefile == "y" or makefile == "Y":
        print("OK... will do")
        time.sleep(2)
        print("Creating file: dark_net_podcast_url_list.txt in current directory")
        open('dark_net_podcast_url_list.txt', 'a').close()
        print("dark_net_podcast_url_list.txt created")
    else:
        print("OK, if you want to thats fine. Make sure the file name is: dark_net_podcast_url_list.txt.")
        time.sleep(2)
        print("<<<Exiting>>>")
        exit()


# Line below does what 4 lines above do
Lines = [line.strip() for line in open('dark_net_podcast_url_list.txt', 'r')]

count = len(Lines)
# Strips the newline character 

my_dict = {}

newlines = [line for line in links if line not in Lines]

# Line above is same as chunk of code below
'''
for line in links: 
    if line in Lines:
        continue
    newlines.append(line)
'''

if newlines:

    print("\nDownloading {} files ".format(len(newlines)))
    print("\nDownload is starting... please be patient as this could take some time\n")

else:
    print("\nNothing needs to be downloaded at this time...\n")

name = name[::2]

for i in range(len(name)):
    # add an item to existing dictionary
    my_dict[links[i]] = name[i].replace(':' , ' -')  

for line in newlines:
    
    #print(line)
    #print(my_dict[line])
    #print(my_dict[line] + ".mp3")
    with open(my_dict[line] + ".mp3", 'wb') as file:
        print(file.name)
        file.write(requests.get(line.strip(), allow_redirects=True).content)


with open('dark_net_podcast_url_list.txt', 'w+') as filehandle:
    for listitem in links:
        filehandle.write('%s\n' % listitem)


```

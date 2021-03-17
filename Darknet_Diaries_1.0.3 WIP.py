# Import required modules 
from lxml import html 
import requests 
import os
import time
import shutil
from shutil import copytree, Error



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
directory = "Darknet_Diaries"

# Parent Directory path
parent_dir = os.path.dirname(os.path.realpath(__file__))

original = parent_dir
# Path
path = os.path.join(parent_dir, directory)



CURR_DIR = os.path.dirname(os.path.realpath(__file__))



Lines = []


if (os.path.exists('dark_net_podcast_url_list.txt') == False) or (os.path.isfile('dark_net_podcast_url_list.txt') == False):

    print("Error, couldn't find: dark_net_podcast_url_list.txt")

    makefile = input("Do you want me to make the file for you? (y or n)  ")

    if makefile == "y" or makefile == "Y":

        curpath = input("Do you want files in current directory? (y , n or exit)  ")


        if(curpath == "y" or curpath == "Y"):

            print("OK, generating directory...")



            # Create the directory
            if not os.path.isdir(path):
                os.makedirs(path)
                print("Directory '%s' created" %directory)
            os.chdir(path)

            open('dark_net_podcast_url_list.txt', 'a').close()



            print(path)


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
                newlines.append(line)y

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



        if(curpath == "n" or curpath == "N"):

            dirpath = input("Where would you like it? Provide full directory path: ")

            if(os.path.isdir(dirpath)):

                print("OK... will do")
                time.sleep(2)

                completeName = os.path.join(dirpath, 'dark_net_podcast_url_list.txt')

                print("Creating file: dark_net_podcast_url_list.txt in: " + dirpath)


                # print("\n")
                # print(os.getcwd()) 
                os.chdir(dirpath)
                # print(os.getcwd()) 
                # print("\n")



                open(completeName, 'a').close()

                print("dark_net_podcast_url_list.txt created at: " + dirpath)



                # print("\n")
                # print("completeName: " + completeName)
                # print("dirpath: " + dirpath)
                # print("\n")
                # print("dir BEFORE file move>>> " + os.path.dirname(os.path.realpath(__file__)))
                # copytree( completeName, dirpath )
                # print("dir AFTER file move>>> " + os.path.dirname(os.path.realpath(__file__)))
                # print("dir BEFORE curdir move>>> " + os.path.dirname(os.path.realpath(__file__)))
                # os.chdir(dirpath)
                # print("dir AFTER curdir move>>> " + os.path.dirname(os.path.realpath(__file__)))

                # print("-----------------------------------")
                # print(completeName)
                # print("-----------------------------------")



                # Line below does what 4 lines above do
                Lines = [line.strip() for line in open(completeName, 'r')]
                count = len(Lines)
                # Strips the newline character 

                my_dict = {}

                newlines = [line for line in links if line not in Lines]

                # Line above is same as chunk of code below
                '''
                for line in links: 
                    if line in Lines:
                        continue
                    newlines.append(line)y

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


                    with open(completeName, 'w+') as filehandle:
                        for listitem in links:
                            filehandle.write('%s\n' % listitem)


            else:
                print("Not a valid path")
                exit()

        if(curpath == "exit"):
            print("<<<Exiting>>>")
            exit()

    else:
        print("OK, if you want to thats fine. Make sure the file name is: dark_net_podcast_url_list.txt.")
        time.sleep(2)
        print("<<<Exiting>>>")
        exit()


# print(path)


# # Line below does what 4 lines above do
# Lines = [line.strip() for line in open('dark_net_podcast_url_list.txt', 'r')]
# count = len(Lines)
# # Strips the newline character 

# my_dict = {}

# newlines = [line for line in links if line not in Lines]

# # Line above is same as chunk of code below
# '''
# for line in links: 
#     if line in Lines:
#         continue
#     newlines.append(line)y

# '''

# if newlines:

#     print("\nDownloading {} files ".format(len(newlines)))
#     print("\nDownload is starting... please be patient as this could take some time\n")

# else:
#     print("\nNothing needs to be downloaded at this time...\n")

# name = name[::2]

# for i in range(len(name)):
#     # add an item to existing dictionary
#     my_dict[links[i]] = name[i].replace(':' , ' -')  

# for line in newlines:
    
#     #print(line)
#     #print(my_dict[line])
#     #print(my_dict[line] + ".mp3")
#     with open(my_dict[line] + ".mp3", 'wb') as file:
#         print(file.name)
#         file.write(requests.get(line.strip(), allow_redirects=True).content)


# with open(completeName, 'w+') as filehandle:
#     for listitem in links:
#         filehandle.write('%s\n' % listitem)
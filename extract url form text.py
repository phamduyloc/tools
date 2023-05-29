import re
import os
import subprocess

# folder path
dir_path = 'D:\\downloads\\inventory-main'
link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)


# Iterate directory
for path in os.listdir(dir_path):       # duyet qua cac folder
    path_servers = dir_path + "\\" + path + "\\servers.txt"
    path_output = dir_path + "\\urls_from_servers.txt"
    if os.path.exists(path_servers):            # kiem tra ton tai file servers.txt
        file = open(path_servers,mode='r',encoding='utf8')
        all_of_it = file.read()
        links = re.findall(link_regex, all_of_it)
        myfile = open(path_output,'a')
        for lnk in links:
            myfile.write(lnk[0]+'\n') 
        myfile.close()
        file.close()




# Open a file: file
#file = open('D:\\recon\\inventory\\Acronis\\servers.txt',mode='r')
 
# read all lines at once
#all_of_it = file.read()
 

#link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
#links = re.findall(link_regex, all_of_it)
#for lnk in links:
#    print(lnk[0])
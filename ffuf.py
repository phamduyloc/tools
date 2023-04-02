import os
import subprocess

FNULL = open(os.devnull, 'w')

# folder path
dir_path = 'D:\\recon\\inventory'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    path_hostname = dir_path + "\\" + path + "\\hostnames.txt"
    if os.path.exists(path_hostname):
        print(path)
        args = 'C:\\Users\\l0cpd\\go\\bin\\ffuf.exe -w "' + path_hostname + '":AAA -u https://AAA/admin/pma/setup/index.php -mc 200 -v -fs 0,2 -t 100 -o "D:/recon/inventory/_results/' + path + '.csv" -of csv'                
        subprocess.call(args)
        
    
    

file1 = open("D:\\tmp\\test1.txt", "r")
file2 = open("D:\\tmp\\test2.txt", "r")
exist_file = "D:\\tmp\\exist_file.txt"
nonexist_file = "D:\\tmp\\nonexist_file.txt"
  
# reading the file

def into_list(input_file):  
    data_into_list = []
    data = input_file.read()
    input_file.close()
    # replacing end splitting the text 
    # when newline ('\n') is seen.
    data_into_list = data.split("\n")
    return  data_into_list


def write_append_file(input_file, content):
    file1 = open(input_file, "a")  # append mode
    file1.write(content + "\n")
    file1.close()
    
data_into_list_1 = into_list(file1)
data_into_list_2 = into_list(file2)
print(data_into_list_1)
print(data_into_list_2)


for x in range(len(data_into_list_1)):
    isExist = False
    for y in range(len(data_into_list_2)):
        if data_into_list_1[x] == data_into_list_2[y]:           # exist
            isExist = True
            write_append_file(exist_file, data_into_list_2[y])  # write file exist_file
            data_into_list_2.remove(data_into_list_2[y])        # remove item from list
            break   # exit for
            
    if isExist == False:     # non exist
        write_append_file(nonexist_file,data_into_list_1[x])
        
for y in range(len(data_into_list_2)):  # write nonexist of data_into_list_2
    write_append_file(nonexist_file,data_into_list_2[y])
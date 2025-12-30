import os
import time
import datetime


filePath = 'C:\\TestJunk\\'
junkList = os.listdir('C:\\TestJunk')

for file_name in junkList: #for each file in the directory
    if file_name.lower().endswith('.txt'): #check if the file ends with ".txt" and if so,
        abJunkList = os.path.join(filePath, file_name) #create an absolute path by combining the name of the path with the name of the file being iterated through
        pathMod = os.path.getmtime(abJunkList) #produce the number of seconds (since the epoch) since that last modification
        print(abJunkList) #print absolute path
        print(pathMod) #print number of seconds since last edit



#print(dir(str))
#print(help(str))
import os

#print(os.getcwd()) #Returns the string representing the path of the current working directory

fName = 'test.txt'

fPath = 'C:\\Users\\nateh\\OneDrive\\Documents\\GitHub\\Python-Projects\\'

abPath = os.path.join(fPath, fName)
print(abPath)

def writeData():
    data = '\nHello World!'
    with open('test.txt', 'a') as f: #Opens a file named test.txt in append mode
        f.write(data) #Adds a new line of 'data'
        f.close()


def openFile():
    with open('test.txt', 'r') as f: #Opens a file named test.txt in read-only mode
        data = f.read() #Reads the contents of the file
        print(data) #Prints the read contents
        f.close()





if __name__ == "__main__":
    writeData()
    openFile()

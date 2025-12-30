#print(dir(str))
#print(help(str))
import os

#print(os.getcwd())

fName = 'test.txt'

fPath = 'C:\\Users\\nateh\\OneDrive\\Documents\\GitHub\\Python-Projects\\'

abPath = os.path.join(fPath, fName)
print(abPath)

def writeData():
    data = '\nHello World!'
    with open('test.txt', 'a') as f:
        f.write(data)
        f.close()


def openFile():
    with open('test.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()





if __name__ == "__main__":
    writeData()
    openFile()

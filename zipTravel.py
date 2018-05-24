import zipfile  
  
def test1():  
  
    for i in range(1, 4):  
        f = open("file" + str(i) + ".txt", 'w')  
        f.write(str(i))  
        f.close()  
  
    f = zipfile.ZipFile('filename.zip', 'w', zipfile.ZIP_DEFLATED)
    f.write('file1.txt')  
    f.write('file2.txt')  
    f.write('file3.txt')  
    f.close()  
  
    f = zipfile.ZipFile('filename.zip')  
    f.extractall()  
    f.close()

def abc():
    f = open("file1.txt",'r')
    binary = f.read()
    zipFile = zipfile.ZipFile("hahaha.zip", "a", zipfile.ZIP_DEFLATED)
    info = zipfile.ZipInfo("hahaha.zip")
    zipFile.writestr("../filehahaha.txt", binary)
    zipFile.close()

    f = zipfile.ZipFile('hahaha.zip')
    f.extractall()
    f.close()
  
if __name__ == "__main__":  
    abc()

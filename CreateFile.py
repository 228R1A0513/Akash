'''

open()
read()
readline()
write()
writeline()
close()
fseek()
tell()


'''

fp=open("cse-a1.txt","w")
if fp:
    print("file is created successfully")

    fp.writelines("hi students welcome to cmrec\n today smart interviews class\n python class is on files")
    print(list())

    fp.close()
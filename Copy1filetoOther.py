fp1=open("cse-a.txt","r")
fp2=open("cse-a1.txt","w+")
if fp1:
    print("file opened sucessfully")
for i in fp1:
    fp2.write(i)
print("file is copyed")
fp2.seek(0,0)
cont=fp2.read()
print(cont)
fp1.close()
fp2.close()
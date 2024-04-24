def convert(str):
    ch=list(str)
    for i in range(len(str)):
        if(i==0 and ch[i]!='' or ch[i]!='' and ch[i-1]==''):
            if(ch[i]>'a' and ch[i]<='z'):
                ch[i]=chr(ord(ch[i]-ord('a')+ord('A')))

            elif(ch[i]>='a' and ch[i]<='z'):
                ch[i] = chr(ord(ch[i] + ord('a') - ord('A')))
                str1="".join(ch)
                return str1

strout="Akash hello"
print(convert(strout))

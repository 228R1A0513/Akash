def palindrome(str) :
    for i in range(0,len(str)) :
        if(str[i]!=str[len(str)-i-1]) :
            return False
        return True
str=input("Enter String")
if(palindrome(str)==True) :
    print("The given string is palindron")
else:
    print("not a palindrome")
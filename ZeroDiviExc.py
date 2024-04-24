try:
   a=int(input("enter a value"))
   b=int(input("enter b value"))
   #c=a/b
   print("value of c:",a+b)
   x=([1,2,3,4])
   print(x[5])
except NameError:
    print("b value is not mentioned")
except ZeroDivisionError:
    print("Arthematic exception")
except ValueError:
    print("Value error")
except IndexError:
    print("Array index out of bounds")
except KeyError:
    print("Key error")
except IOError:
    print("file input or output error")

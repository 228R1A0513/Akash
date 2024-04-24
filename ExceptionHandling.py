try:
   a=int(input("enter a value"))
   b=int(input("enter b value"))
   c=a/b
   print("value of c:",a/b)
except Exception:
    print("cannot divide by zero")
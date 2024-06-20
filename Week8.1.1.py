def AND(a,b):
    if a==1 and b==1:
        return True
    else:
        return False
print(("A=True|B=True|A AND B=True",AND(True,True)))
print(("A=False|B=False|A AND B=False",AND(False,False)))
print(("A=True|B=False|A AND B=False",AND(True,False)))
print(("A=False|B=True|A AND B=False",AND(False,True)))
print(AND(1,1))
def OR(a,b):
    if a==0 and b==0:
        return False
    else:
        return True
print(("A=False|B=False|A OR B=False",OR(False,False)))
print(("A=False|B=True|A OR B=True",OR(False,True)))
print(("A=True|B=False|A OR B=True",OR(True,False)))
print(("A=True|B=True|A OR B=True",OR(True,True)))
print(OR(0,0))
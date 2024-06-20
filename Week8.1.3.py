def XOR(a,b):
    if a==0 and b==0:
        return False
    else:
        return True
print(("A=False|B=False|A XOR B=False",XOR(False,False)))
print(("A=False|B=True|A XOR B=True",XOR(False,True)))
print(("A=True|B=False|A XOR B=True",XOR(True,False)))
print(("A=True|B=True|A XOR B=False",XOR(True,True)))
print(XOR(1,0))
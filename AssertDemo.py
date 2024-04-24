'''
def avg(marks):
    assert len(marks) != 0,"The list is empty."
    return sum(marks)/len(marks)

marks1 = [67,34,56,76,57]
print("The Average of marks1:",avg(marks1))
marks2=[10,20,30,40]
print("The Average of marks2:",avg(marks2))
'''
list123 = [1,2,3,4,55,6,7,0]
x =8
assert x not in list123,"x is not in list"
assert x in list123,"x in list"
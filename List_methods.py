my_list=[1,2,3,4]
'''
List methods:
1.sort()
2.clear()
3.append()
4.count()
5.extend([4])
6.insert()
7.index()
8.len()
9.remove()
10.pop()
11.reverse()
12.copy()
13.len()
14.min()
15.max()
16.del()

'''
mylist=[1,2,3,4,55,6]
mylist.sort()
print(mylist)
mylist.append(99)
print(mylist)
mylist.extend([44,77,88])
print(mylist)
print(mylist.count(4))
#mylist.insert(__index=1,__object=22)
print(mylist)
max=max(mylist)
print(max)
min=min(mylist)
print(mylist)
del mylist[2]
print(mylist)
copylist=mylist.copy()
print(" copied list= ",copylist)


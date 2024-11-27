dict1={1:"orange",3:"red",2:"yellow",4:"green"}
list1=list(dict1.items())
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
dict2={5:"violet",6:"white"}
dict1.update(dict2)
print(dict1)


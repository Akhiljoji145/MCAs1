list1=["orange","black","red","white"]
first_element=list1[0]
last_element=list1[-1]
print(f"first element: {first_element}")
print(f"last element: {last_element}")
list2=["blue","red","white","violet"]
for i in list1:
    if i not in list2:
        print(i)
list1[0]=1
list1[1]=2
list1[2]=3
list1[3]=4
print(list1)
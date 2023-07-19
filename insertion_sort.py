def insertion_sort(list1):
    for i in range(0, n):
        temp =list1[i]
        j=i
        while j>0 and temp<list1[j-1]:
            list1[j] = list1[j-1]
            j = j-1
        list1[j] = temp
    print(list1)
    print(list2)
    
    
    
n = int(input())
list1 =(input().split(" "))
list2 = list1[:]
list3 = []
insertion_sort(list1)


for i in range(0,n):
    for j in range(0,n):
        if list2[i]==list1[j]:
           pos = j+1
           list3.append(pos)
            
print(*list3 , sep = " ")


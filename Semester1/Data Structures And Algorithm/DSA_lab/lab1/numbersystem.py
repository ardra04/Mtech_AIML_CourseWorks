def conversion(n,j):
    if j==0:
        list.append(0)
        return list
    else:
        for b in range (j):
            if j==0:
                break
            else:
                a =int(j%n)
                list.append(a)
                j = int(j/n)
        return list
final = []
n = int(input("the base value"))
k = int(input("Enter the value"))
for i in range(0,k):
    list =[]
    result = conversion(n,i)
    testlist = list.copy()
    testlist.reverse()
    newlist =''.join((str(p) for p in testlist))
    final.append(newlist)
print(final)
    
                
            


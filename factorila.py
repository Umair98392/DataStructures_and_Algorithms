def factorial(m):
    if m< len(fact):
        return (fact[m])
    else:
        for i in range(m,m+1):
            fact.append(i*fact[i-1])
        return (fact[m])

t = int(input())
a =[]
for i in range(t):
    ele = int(input())
    a.append(ele)
fact = [1,1,2]
for i in a:
    #print(i)
    print(factorial(i)%1000000007)
    #print(fact)

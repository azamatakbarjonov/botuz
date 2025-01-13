
number = lambda x: x * 10
result = number(23)
print(result) 


def daraja(n):
    return lambda x: x ** n
kv = daraja(10)  
print(kv(2))  








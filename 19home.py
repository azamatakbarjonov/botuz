# n = int(input("Butun sonni kiriting: "))

# for i in range(1, n + 1):
#     print(i, end=" ")











n = int(input("Butun soni kiriting:"))
numbers = list(range(n+1))


numbers = [son for son in numbers if son % 2 != 0]
print(numbers)




























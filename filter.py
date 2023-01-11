a = [10,50,60,80,90,5,45,65]
def high_marks(n):
    if n>=60:
        return True
result = list(filter(high_marks, a))
print(result)
for i in result:
    print(i)

print("Using lambda function")
a = [10,50,60,80,90,5,45,65]

result = list(filter(lambda n : (n>=60), a))
print(result)
for i in result:
    print(i)

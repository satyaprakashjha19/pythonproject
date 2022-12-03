# f-string  f-string empty expression not allowed
# integer
print("*****integer*****")
a = 10
b = 20
value = f"{a}"
print(f"{a}")
print(f"{a}   {b}")
print(f"{b} {a}")
print(value)

# float
print("*****float*****")
c = 15.50
d = 20.80
value = f"{c}"
print(f"{d}")
print(f"{c}   {d}")
print(f"{d} {c}")
print(value)

# string
print("*****string*****")
f_name = "satyaprakash"
l_name = "jha"
print(f"{f_name}")
print(f"{l_name}")
print(f"{f_name} {l_name}")
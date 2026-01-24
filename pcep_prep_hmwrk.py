temp = (32, 35, 31, 33, 36, 34)
print(temp)

print(len(temp))

print(temp[0])
print(temp[-1])

print(temp[1:-1])

if 35 in temp:
    print("Temperature found")
else:
    print("Temperature not found")

for t in temp:
    print(t)

extra_days = (30, 37)
updated = temp + extra_days
print(updated)

print(extra_days * 2)

single = (40,)
print(single)

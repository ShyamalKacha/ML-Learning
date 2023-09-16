a=[1,2,3,4]
high=0
for i in a:
    if i>high:
        high=i
print(high)
second_high=0
for j in a:
    if i> second_high and i<high:
        second_high=i
        print(second_high)
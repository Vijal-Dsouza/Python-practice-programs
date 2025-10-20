test =  [12,24,35,24,88,120,155,88,120,155]
unique  = set()
res =  []

for num in test :
    if num not in unique :
        res.append(num) 
    unique.add(num)

print(res[::-1])
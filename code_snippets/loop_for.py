for i in range(10):
    print(i)

print('\n -------- continue -------- \n')
for i in range(5):
    if i == 3:
        continue
    else:
        print(i)


print('\n -------- break -------- \n')

for i in range(5):
    if i == 3:
        break
    else:
        print(i)

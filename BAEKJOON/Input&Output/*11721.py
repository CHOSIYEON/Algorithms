list = input()

for i in range(len(list)//10):
    print(list[10*i:10*i+10])

if len(list)%10 != 0:
    print(list[10 * (len(list) // 10):])

# ////////////////////////////////////////////////

for i in range(0, len(list), 10):
    print(list[i:i+10])
sum = 0
for i in range(5):
    n = int(input())
    if(n<40):
        n = 40
    sum = sum + n
print("%2d" %(sum/5))
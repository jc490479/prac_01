import random
rows=int(input("How many quick picks? "))
randomlist=[]

for i in range(rows): #new lines.......print differnt lines
    print("")
    randomlist=[]
    for j in range(6):
        num= random.randrange(1,46)
        if num not in randomlist:
            randomlist.append(num)
        else:
            j-=1
        randomlist.sort()
    for k in randomlist:
        print ("{:2}".format(k),end=" ")



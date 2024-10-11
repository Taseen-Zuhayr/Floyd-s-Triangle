n = int(input("Enter the number of rows you want"))
numb = 1

for row in range(1,n+1):
    for col in range(1,row+1):
        print(numb,end="  ")
        numb = numb + 1
    print("\n")
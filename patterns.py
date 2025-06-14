#Square Pattern
n = int(input("enter n:"))
for i in range(1,n):
    print("*" * n)

#Right angled Triangle

n=int(input("enter n:"))
for i in range(1,n):
    print("*" * i)

#Pyramids

print("Pyramid Pattern:")
for i in range(1, levels + 1):
    spaces = " " * (levels - i)
    stars = "* " * i
    print(spaces + stars.strip())
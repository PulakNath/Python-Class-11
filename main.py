s = input("Enter your word: ")
c = input("Enter your character: ")
i = 0
v = 0
while (i < (len(s))):
    if (s[i] == c):
        v = v + 1
    i = i + 1
print("The amount of times that", c, "occurs in", s, "is: ", v)
l = int(input("Enter your lower limit: "))
u = int(input("Enter your upper limit: "))
print("Prime numbers between", l, "and", u, "are: ")
for num in range(l, (u + 1)):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
number = (input("Enter a number: "))
if len(number) >= 4:
    mid = len(number) // 2
    midOne = int(number[mid - 1])
    midTwo = int(number[mid])
    product = midOne * midTwo
    print("The product of the middle two digits is:", product)
elif len(number) == 3:
    mid = len(number) // 2
    print("There's only one middle digit")
else:
    print("Your number isn't more than 3 digits long")
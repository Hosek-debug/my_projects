print("=============The Welcome System================")
print("Hi world, welcome to the prototype for a site or software")
print("please user, input your data base about every topic below")

name = str(input("Write your name"))

print("welcome:", name)

print("In this site, we need to know if you is old enough to enter")

age = int(input("Write your age"))

print("your age is:", age)

if age >= 18:
    print("Welcome to the site")
else:
    print("Sorry, you are under 18 years old")
    
print("in this site, you could buy something, there are apple, banana and orange")
print("Which of them you want to buy?")
print("apple - 1, banana - 2, orange - 3")

for i in range(1, 2, 3):

    buy = int(input("choose a fruit"))

    if buy == 1:
        print("you choose apple")
    elif buy == 2:
        print("you choose banana")
    elif buy == 3:
        print("you choose orange")

print("thank you to enter in my site, wait for more projects in my Github!")        
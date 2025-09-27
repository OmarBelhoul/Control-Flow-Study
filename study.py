# if elif else
user_age_check=int(input("type your age "))

if user_age_check >=18:
    print("welcome")
else :
    ("you're too young")

# exercise 1
age = int(input("how old are you? "))

if age <12 :
    print("you are a kid")
elif 12 <= age <= 17:
    print("you are a teenager")
elif age>= 18 :
    print("you are an adult")
else:
    print("unknow")

#exercise 2
print("welcome user")

password_check =input("type the password ")

if password_check =="python123":
    print("welcome")
else :
    print("access denied")

#exercise 3
number =int(input("type a number "))

if number > 0 :
    print("positive")
elif number < 0 :
    print("negative")
elif number == 0 :
    print("it's a zero")
else :
    print("unknown")



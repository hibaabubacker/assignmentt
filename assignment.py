# question_1
number=input("enter a number ")
print("entered number is "+number)


# question_2
num1=int(input("enter a number"))
num2=float(input("enter another number"))
result=float(num1+num2)
print("added number is "+str(result))


# question_3
num1=int(input("enter principal"))
num2=float(input("enter rate"))
num3=float(input("enter time"))

result=float((num1*num2*num3)/100)
print("your interest is "+str(result))


# question_4
num1=float(input("enter mark :"))

if num1>=50:
    print("passed")
else:
    print("failed")



# question_5
num1=float(input("enter mark :"))

if num1>=90:
    print("A+")
elif num1>=80:
    print("B")
elif num1>=70:
    print("C")
elif num1>=60:
    print("D")
elif num1>=50:
    print("E")
else :
    print("failed")



# question_6
def switch(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Invalid entry"

day = int(input("Enter a number (1-7): ")) 
print(switch(day))


# question_7
number = 5
i = 1

while i <= 10:
    print(f"{i} * {number} = {number * i}")
    i += 1

# question_8

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

sum_of_odds = 0

for num in range(start, end + 1):
    if num % 2 != 0:
        sum_of_odds += num

print("Sum of odd numbers:", sum_of_odds)


# question_9
rows=5
for i in range (rows+1):
    for j in range (1,i+1):
        print(j,end=" ")
    print()


# question_13
reverse_word=input("enter a word ")
reverse=reverse_word[::-1]

if reverse_word == reverse:
    print( f" {reverse_word} a palindrome")
else:
    print( f" {reverse_word} its not palindrome")


# question_20

number=1

for i in range(1,5):
    for j in range (i):
        print(number,end="\t")
        number+=1
    print()

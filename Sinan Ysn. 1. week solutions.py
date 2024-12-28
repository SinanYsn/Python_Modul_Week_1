#1. week 3. Question 
#Write a Python code that receives a start and end value from the user and prints all the numbers between these values ​​(including the end value) on the screen.
a = int(input("Write a number: "))
b = int(input("Write one more number:"))
if a<b:
    for i in range (a, b+1):
        print (i)
elif b<a:
    for i in range (b, a+1):
        print (i)

#1.week 7. Question
#### How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?
fb = [1,1]
fb_index = 2
fb_son = 0
while len(str(fb_son)) < 100:
    fb.append(fb[fb_index-2]+fb[fb_index-1])
    fb_son = fb[fb_index-2]+fb[fb_index-1]
    fb_index += 1
print(fb_index)
print (fb_son)
print (fb)

#1. wekk 11. Question
#How to write a Python program that finds the largest of three numbers entered by a user?

first= int(input( "Write a number:"))
second = int(input (" Write another number :"))
third = int(input(" Write one another number:"))

#print (f"The largest number is {(max(first, second, third))}")

#print ("the largest number is:", max(first, second, third))

if first >= second and first>third:
    print (first,"  is the largest number" )

elif second > first and second> third:
    print (second, "  is the largest number ")

else:
    print (f"{third} is the largest number")

#Hackerrank 3.Question
#The included code stub will read an integer, , from STDIN.
#Without using any string methods, try to print the following:
#Note that "" represents the consecutive values in between.
#Print the list of integers from  through  as a string, without spaces.
#Sample Input 3
#Sample Output 123
#straints 1<= n<=150

number= int(input("write a number:"))
while  number<1 or number>150:
    number= int(input("write a number:"))
for i in range(1, number+1):
    print (i, end="")

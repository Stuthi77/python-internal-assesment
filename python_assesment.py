# -*- coding: utf-8 -*-
"""python_assesment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EwYwhDik2quJSKBAjaexxHsb6GlFcP38

#1
"""

def rectangle_area(l,b):
  a=l*b
  return a
l=int(input("Give length value:"))
b=int(input("Give width value:"))
print(rectangle_area(l,b))

"""#2"""

def BMI(h,w):
  bmi=w/(h**2)
  return bmi
h=float(input("height in meters:"))
w=float(input("weight in kg:"))
print(BMI(h,w))

"""#3"""

d={}
for i in range(3):
  student_id=int(input("Enter student id:"))
  student_name=input("Enter student name:")
  class1=int(input("Enter student class:"))
  student_score=int(input("Enter student score:"))
  d[student_id]=student_name,class1,student_score
print(d)

"""#4"""

n=int(input("Enter your Age:"))
if n<18:
  print("You are a minor you,you are not eligible to vote for the election")
elif n>=18 and n<40:
  print("You are a adult you,you are eligible to vote for the election")
else:
  print("You are a senier citizen and you are eligible to vote for the election")

"""#5"""

i=1
for i in range(1,50):
  if (i)%2==0:
    print(i," - is a even number")
  else:
    pass

"""#6"""

password='internalAssesment12$'
user_password=input("Enter the correct password")

while(password!=user_password):
  print("incorrect password try again")
  user_password=input("Enter the correct password:")
  if(password==user_password):
    print("succesfully logined to website!!!")
    break

"""#7"""

def average(list_values):
  sum=0
  for i in range(len(list_values)):
    sum+=list_values[i];
  print("sum=",sum)
  return sum/len(list_values)

list_values=[]
for i in range(10):
  list_values.append(int(input("Enter values:689")))
print("Average=",average(list_values))

"""#8"""

a=input()
k=0
k=a.count('a',0,len(a))
k=k+a.count('e',0,len(a))
k=k+a.count('i',0,len(a))
k=k+a.count('o',0,len(a))
k=k+a.count('u',0,len(a))
print("no of vowels-",k)

"""#9"""

import datetime

print(datetime.datetime)

"""#10"""

n=input()
try

   if type(n)=='int':

finally

"""11"""



"""#12"""



"""#13"""

file=open("C:\Users\danduprolu.stuthi.lv\Downloads\python.txt",'w')
file.write('Hello python!!')
content=file.read()

"""#14"""

file=open("C:\Users\danduprolu.stuthi.lv\Downloads\python.txt",'w')
file.write('Hello python!!')
content=file.read()
print(content)
a = "+"
b = "-"
c = "×"
d = "÷"
num1 = float(input("Enter number:"))
sign = str(input ("Enter sign:"))
num2 = float(input ("Enter 2nd number:"))
if(a==sign):
      print (num1+num2)
elif(b==sign):
      print (num1-num2)
elif(c==sign):
      print (num1*num2)
elif(d==sign):
      print (num1/num2)
else:
      print ("Error")
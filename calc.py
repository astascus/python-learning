#building a basic 4-function calculator
print('4-function Calculator')

num1=float(input('First number: '))
oper=input('Operator: ')
num2=float(input('Second Number: '))

if oper == '+':
  print(num1+num2)
elif oper == '-':
  print(num1-num2)
elif oper == '*':
  print(num1*num2)
elif oper=='/':
  print(num1/num2)
else:
  print('Invalid operator')
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
n1 = 0
if name1.count('t') > 0:
  n1 += name1.count('t')
if name1.count('r') > 0:
  n1 += name1.count('r')
if name1.count('u') > 0:
  n1 += name1.count('u')
if name1.count('e') > 0:
  n1 += name1.count('e')
if name1.count('l') > 0:
  n1 += name1.count('l')
if name1.count('o') > 0:
  n1 += name1.count('o')
if name1.count('v') > 0:
  n1 += name1.count('v')
if name1.count('e') > 0:
  n1 += name1.count('e')


n2 = 0
if name2.count('t') > 0:
  n2 += name2.count('t')
if name2.count('r') > 0:
  n2 += name2.count('r')
if name2.count('u') > 0:
  n2 += name2.count('u')
if name2.count('e') > 0:
  n2 += name2.count('e')
if name2.count('l') > 0:
  n2 += name2.count('l')
if name2.count('o') > 0:
  n2 += name2.count('o')
if name2.count('v') > 0:
  n2 += name2.count('v')
if name2.count('e') > 0:
  n2 += name2.count('e')


total = n1 + n2


if total < 10 or total > 90:
  print(f"your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}")

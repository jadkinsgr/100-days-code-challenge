# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
  b = 15
elif size == "M":
  b = 20
elif size == "L":
  b = 25
  if add_pepperoni == "Y":
    b += 2
    if extra_cheese == "Y":
      b += 2

print(f"Your size selected was {size}, your final bill is ${b}")

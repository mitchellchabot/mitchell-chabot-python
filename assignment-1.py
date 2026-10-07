# Section 1
name = "Mitchell"
birth_year = 1999
shoe_size = 10.5
drinks_coffee = False
current_year = 2026

print(name, type(name))
print(birth_year, type(birth_year))
print(shoe_size, type(shoe_size))
print(drinks_coffee, type(drinks_coffee))


#Section 2
user_name = input("What is your name?")
user_age = int(input("What year were you born?"))

print("Hi, " + user_name + "! + You are approximatly " + str(current_year - user_age) + " years old.")



# Section 3
first_number = float(input("Please enter a number."))
second_number = float(input("Please enter a second number."))
result = (first_number * second_number)


print(f"Your result is {result}")


#Section 4
item_name = ("Python textbook")
item_price = float(29.99)
item_qty = float(2)
item_total = (item_price * item_qty)



print("===========================")
print("RECEIPT")
print("===========================")
print("Item:      " + item_name)
print(f"Price:      + {item_price}")
print(f"Quantity:   + {item_qty}")
print("---------------------------")
print(f"Total:      {item_total}")
print("===========================")



#Section 5

user_name2 = input("What is your name?")
hometown = input("What is your hometowm?")
hobby = input("What is your favorite hobby?")
fact = input("What is one fact about you?")
year_born = int(input("What year were you born?"))
age = (2026 - year_born)


print ("╔══════════════════════════════╗")
print("    PROFILE:  " + user_name2)
print ("╚══════════════════════════════╝")
print("HOMETOWN:      " + hometown)
print("HOBBY:         " + hobby)
print("FUN FACT:     " + fact)
print(f"AGE:           {age}")



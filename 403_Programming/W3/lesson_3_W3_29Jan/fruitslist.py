fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
#fruits[1] replaces the list elements in the list with the defined new item in the same space in the list (1)
fruits.append("pineapple")
#.append adds item to the end of the list
print(fruits)

fruits.insert(3, "grape")
#.insert inserts an element into the selected location in the list
print(fruits)

fruits.remove("mango")
#.remove removes the first matching value
print(fruits)

popped_fruit = fruits.pop(0)
#pop removes an item by index and returns it
print(popped_fruit)
print(fruits)

print(fruits[1:3])

print(fruits[:2])

for fruit in fruits:
    print(fruit)
    
fruits.clear()
#clears list
print(fruits)




grades = [2, 45, 73, 15, 10]
print(grades)

grades.sort()
print(grades)

grades.reverse()
print(grades)

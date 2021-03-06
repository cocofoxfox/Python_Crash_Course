print("Hello Python World!")

message = "Hello Python world"
print(message)

#Variable names can contain only letters, numbers and underscores. No spaces
#They can start with a letter or an underscore, but not with a number.
#message_1 is right, 1_message is wrong
#Be careful when using the lowercase l and uppercase letter O, becuase they could be confused with the numbers 1 and 0

name = "ada loveace"
print(name.title())

first_name = "ada"
last_name = "lovelace"
#using f
full_name = f"{first_name} cool {last_name}"
print(full_name)
full_name = "{} {}".format(first_name, last_name)

#Add white space :\t, new line : \n
print("\tPython")

#Stripping Whitespace: lstrip(), rstrip(), strip()
favorite_language = 'python '
favorite_language.rstrip()

#use apostrophe in single quote will cause a error
print("one's")
#print('two's')

#mix integer and float you will get float

#You can group digits using underscore
universe_age = 14_000_000_000

#Multiple Assigment
x,y,z = 0, 0, 0

#Constants
MAX_CONNECTIONS = 5000

#list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
#last element in the list
print(bicycles[-1])
#second element from the end
print(bicycles[-2])

#append elements to the end of a list
bicycles.append('qqq')
print(bicycles)

#insert elements
bicycles.insert(0, 'aaa')
bicycles.insert(2, 'third')
print(bicycles)

#delete element and no use element
del bicycles[0]
#pop() removes the last item in the list, return this element
print(bicycles.pop())
print(bicycles)

first_bike = bicycles.pop(0)
print(first_bike)

#remove element by value
bicycles.remove('third')   #return none
print(bicycles)

#sorting a list permanently: sort()
cars = ['bmw', 'audi', 'toyota', 'subaru', 'autuo']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#sorting a list temporarily: sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru', 'autuo']
print(f"Here is the original list: \n{cars}")

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list agian:")
print(cars)


cars.reverse()

len(cars)

#request last item from an empty list cause a error
# motorcycles = []
# print(motorcycles[-1])

#loop a list
cars = ['bmw', 'audi', 'toyota', 'subaru', 'autuo']
for car in cars:
    print(car)


#using the rang() function
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

#using range() to skip numbers

even_numbers = list(range(2, 11, 2))
print(even_numbers)

#two asterisks(**) represent exponents
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

min(squares)
max(squares)
sum(squares)

#list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)

#slice a list
print(squares[0 : 3])
print(squares[:4])
print(squares[2:])
print(squares[-3:])

#looping a slice
for square in squares[:3]:
    print(square)

#copying a list
squares_copy = squares[:]

#tuples: immutable list
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#write over(redefine a tuple)
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#Python Enhancement Proposal(PEP) : the style guide
#Indentation: 4 spaces, no TABs
#line length limit 80-character


#If statement
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Testing for equality is case sensitive in Python.




















#this is for largest number

numbers = [4, 7, 1, 9, 3]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("largest:", largest)


# this is for smallest number
numbers = [4, 7, 1, 9, 3]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("smallest:", smallest)

# this is for sum 

numbers = [4, 7, 1, 9, 3]

total = 0

for num in numbers:
    total = total + num

print("sum:", total)

# this is for sum of squares

numbers = [3,4, 7, 1, 9,]

sum_squares = 0

for num in numbers:
    sum_squares = sum_squares + num**2

print("sum of squares:", sum_squares)

#this is for prime numbers 

numbers = [3,4, 7, 1, 9]
primes = []

for num in numbers:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)

print("primes :",primes)
#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def print_hello_with_username(USERNAME):
  message = "Hello_" + USERNAME + "!"
  print(message)

print_hello_with_username("Amber")

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for number in range(1, 101):
        if number % 2 != 0:
            print(number)
first_odds()

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    if not a_list:
        return None

    max_num = a_list[0]

    for num in a_list:
        if num > max_num:
            max_num = num

    return max_num

# Example list
numbers = [43, 12, 17, 10, 99, 67]

max_number = max_num_in_list(numbers)
print("The maximum number in the list is:", max_number)


#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
print(is_leap_year(2024))

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean.
def are_consecutive_numbers(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i+1] - a_list[i] != 1:
            return False
    return True
numbers1 = [2, 3, 4, 5, 6, 7]
numbers2 = [7, 9, 5, 11]

print(are_consecutive_numbers(numbers1))
print(are_consecutive_numbers(numbers2))

This repository contains different directories with each directory containing files that achieve certain milestones in the learning process:
The followig are the directories with the files within and what the objective of each task:
## 0x00-python-hello_world
  1. ### 0-run:
     This task is used for testing the ability of leaners to run simple shell script and how to access environment variables in the script.
  2. ### 1-run_inline:
     Here we are supposed to run a python code specified in an environment variable using a shell script. This task teaches us how to use python3 -c command.
  3. ### 2-print.py:
    using the print() function
  4. ### 3-print_number.py:
     In this task we are using format specifier concept that specifies how values are formatted when they are inserted into a string. In this case
     we are using %d format specifier to ensure the value is represented as a decimal integer.
  5. ### 4-print_float.py:
     In this task we are supposed to use format specier to specify the number of digit that a float should have


# FINDING THE FIRST AND THE LAST DIGIT OF A NUMBER

## finding the last digit
To find the last digit in a number we will use the modulo operator (%).
for instance lets say we have n = 12345 so the last digit will be n % 10 = 5

## finding the first digit
To find the first digit is a little bit expensive we will divide the given number by 10 until the number is less than or equal to 10 and then we will print its int

e.g n = 12345
while n >= 10:
    n = n / 10

print(int(n))

The time complexity of this problem is O(log10n) this means that it reduces the size of the problem by a constant factor in each step
The auxilliary space complexity is O(1) this means that the algorithm use a constant amount of extra space regardless of the input size means the algorithm does not require an additional memory in proportional to the input size

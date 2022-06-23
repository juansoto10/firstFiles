def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
        num = input('Type a number: ')
        assert num.isnumeric() and int(num) > 0, 'Strings, negative numbers and Zero are not allowed'
        print(divisors(int(num)))  # (1)
        print(':::My program has ended:::')


if __name__ == '__main__':
    run()

# If we type 'a' this would be the output:

# (1) --> 

# Traceback (most recent call last):
#   File "/home/juansoto23/personalProjects/firstFiles/python_course_1/assert_statements.py", line 17, in <module>
#     run()
#   File "/home/juansoto23/personalProjects/firstFiles/python_course_1/assert_statements.py", line 11, in run
#     assert num.isnumeric() and int(num) > 0, 'Strings, negative numbers and Zero are not allowed'
# AssertionError: Strings, negative numbers and Zero are not allowed
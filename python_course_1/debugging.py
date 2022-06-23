def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Type a number: '))
        print(divisors(num))
        print(':::My program has ended:::')
    except ValueError:
        print('You must type a number')


if __name__ == '__main__':
    run()
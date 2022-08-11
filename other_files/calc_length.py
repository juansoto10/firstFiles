def calc_dist(l, h1, h2):
    """Calculates the horizontal distance projected by a line with a certain slope.
    l, h1, h2: float > 0
    """
    
    hor_dist = float((l**2 - (h1 - h2)**2)**0.5)

    print(f'Horizontal distance = {hor_dist} m\nh1 = {h1} m\nh2 = {h2} m\nΔh = {h1-h2}, L = {l} m')


if __name__ == '__main__':

    l = float(input('Enter L: '))
    h1 = float(input('Enter h1: '))
    h2 = float(input('Enter h2: '))

    print('-' * 50)
    calc_dist(l, h1, h2)
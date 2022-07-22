import re


def read_heights():
    """This function reads the files wich contains the heights of the points and creates a list with that data"""

    list_of_heights = []

    with open('./files/heights.txt', 'r') as f:
        for line in f:
            not_allowed = '\n'

            if not_allowed in line:
                new_line = re.sub('\n', '', line)
                # print(new_line)
                list_of_heights.append(float(new_line))
            else:
                # print(line)
                list_of_heights.append(float(line))
    
    return list_of_heights


def read_horizontal_dist():
    """This function reads the file wich contains the horizontal distances between the points and creates a list with that data"""

    list_of_horizontal_distances = []

    with open('./files/horizontal_dist.txt', 'r') as f:
        for line in f:
            not_allowed = '\n'

            if not_allowed in line:
                new_line = re.sub('\n', '', line)
                # print(new_line)
                list_of_horizontal_distances.append(float(new_line))
            else:
                # print(line)
                list_of_horizontal_distances.append(float(line))
    
    return list_of_horizontal_distances

    # print(heights)
    # print(len(heights))
    
    # print(horizontal_distances)
    # print(len(horizontal_distances))


heights = read_heights()
horizontal_dist = read_horizontal_dist()


def calc_slope(h1, h2, horizontal_dist):
    """This function calculates the slope of a line given the heights of two known points and the horizontal distance that separates them
    h1, h2, horizontal_dist: int > 0"""

    slope = float((h1 - h2) / horizontal_dist * 100)
    print(slope)


def main():
    calc_slope(heights[0], heights[1], horizontal_dist[0])
    calc_slope(heights[1], heights[2], horizontal_dist[1])
    calc_slope(heights[2], heights[3], horizontal_dist[2])
    calc_slope(heights[3], heights[4], horizontal_dist[3])
    calc_slope(heights[4], heights[5], horizontal_dist[4])
    calc_slope(heights[5], heights[6], horizontal_dist[5])
    calc_slope(heights[6], heights[7], horizontal_dist[6])
    calc_slope(heights[6], heights[9], horizontal_dist[7])
    calc_slope(heights[7], heights[8], horizontal_dist[8])
    calc_slope(heights[8], heights[9], horizontal_dist[9])
    calc_slope(heights[9], heights[10], horizontal_dist[10])
    calc_slope(heights[10], heights[11], horizontal_dist[11])
    calc_slope(heights[11], heights[12], horizontal_dist[12])
    calc_slope(heights[12], heights[13], horizontal_dist[13])
    calc_slope(heights[13], heights[14], horizontal_dist[14])
    calc_slope(heights[14], heights[15], horizontal_dist[15])
    calc_slope(heights[15], heights[16], horizontal_dist[16])
    calc_slope(heights[16], heights[17], horizontal_dist[17])
    calc_slope(heights[17], heights[13], horizontal_dist[18])
    calc_slope(heights[17], heights[18], horizontal_dist[19])
    calc_slope(heights[18], heights[12], horizontal_dist[20])
    calc_slope(heights[18], heights[19], horizontal_dist[21])
    calc_slope(heights[19], heights[1], horizontal_dist[22])
    calc_slope(heights[19], heights[20], horizontal_dist[23])
    calc_slope(heights[20], heights[4], horizontal_dist[24])
    calc_slope(heights[20], heights[11], horizontal_dist[25])


if __name__ == '__main__':
    main()

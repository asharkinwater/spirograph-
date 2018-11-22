import math as m
import csv


def main():
    R = 125  # R = radius of larger circle
    r = 85  # r = radius of circle traveling within larger circle
    d = 125  # d = distance from the center of the larger circle

    with(open('spirograph.gcode', 'w')) as f:

        me = csv.writer(f)

        me.writerow(["G28"])  # home command
        me.writerow(["G1 Z10"])  # pen up

        angle = 5
        theta = 0.2
        steps = 8 * int(6*3.14/theta)
        i = 1
        for t in range(0, steps):  # loop to generate gcode
            angle += theta
            x = (R - r) * m.cos(angle) + d * m.cos(((R-r)/r)*angle)+60  # changes shape
            y = (2*R - r) * m.sin(angle) - d * m.sin(((R-r)/r)*angle)+60
            x = round(x, 1)  # so you don't crash the 3D printer
            y = round(y, 1)
            if i < 2:  # drop pen at start
                me.writerow(["G1 " + "X" + str(x) + " Y" + str(y)])
                me.writerow(["G1 Z0"])
                i = i + 1
            else:
                me.writerow(["G1 " + "X" + str(x) + " Y" + str(y)])
                i = i + 1
        me.writerow(["G1 Z10"])
        me.writerow(["G28"])


main()


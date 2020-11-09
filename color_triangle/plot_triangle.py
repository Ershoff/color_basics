import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

def read_sens_from_cvs(path_to_file):
    wavelenghts = np.zeros([830-390+1], dtype=float)
    X = np.zeros([830-390+1], dtype=float)
    Y = np.zeros([830-390+1], dtype=float)
    Z = np.zeros([830-390+1], dtype=float)

    with open(path_to_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(csv_reader):
            wavelenghts[i] = int(row[0])
            X[i] = float(row[1])
            Y[i] = float(row[2])
            Z[i] = float(row[3])

    return wavelenghts, [X,Y,Z]
            

def plot_sens(wavelenghts, sens):
    plt.plot(wavelenghts, sens[0], color='red')
    plt.plot(wavelenghts, sens[1], color='green')
    plt.plot(wavelenghts, sens[2], color='blue')
    plt.grid()
    plt.xlabel('wavelenghts')
    plt.ylabel('Sensitivity')
    plt.title('Standard observer sens. functions')
    plt.legend(['longwave', 'middlewave', 'shortvawe'])
    plt.show()
    

def plot_triangle(sens, planc_curve=False, sources=False):
    pass

if __name__ == "__main__":
    path_to_file = '/home/ruff/work/color/color_basics/color_triangle/lin2012xyz2e_1_7sf.csv'
    wavelenghts, [X,Y,Z] = read_sens_from_cvs(path_to_file)

    plot_sens(wavelenghts, [X,Y,Z])



# TODO: find proper lib for triangle vis
# TODO: Plot locus with wavelenghts
# TODO: Plot colors inside triangle
# TODO: Plot planck curve
# TODO: Plot source points
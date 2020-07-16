# This program calculates the viscosity temperatur graph
# with the Ubbelohde-Walther-Algorithm

import math
import numpy as np
import matplotlib.pyplot as plt

# Get the Viscosity Temperature Plot with linear axis scaling
#### x1: x axis minimum
#### x2: x axis maximum
#### n: number of values on the x axis
def get_visc_temp_graph_lin(visc1, visc2, x1, x2, n=50, temp1=40, temp2=100):
    x_values = np.linspace(x1, x2, n)
    y_values = []
    for x in x_values:
        visc = get_visc(visc1, visc2, x, temp1, temp2)
        y_values.append(visc)
    plot_visc_temp_graph_lin(x_values, y_values, x1, x2)

# Plot the Viscosity Temperature Graph with linear axis scaling
def plot_visc_temp_graph_lin(x_values, y_values, x1, x2):
    plt.plot(x_values, y_values)
    plt.xlim(x1, x2)
    plt.grid()
    plt.show()

# Calculate the viscosity at a specific temperature
def get_visc(visc1, visc2, temp, temp1=40, temp2=100):
    # Convert temperatures to Kelvin
    temp = celsius_to_kelvin(temp)
    temp1 = celsius_to_kelvin(temp1)
    temp2 = celsius_to_kelvin(temp2)

    # Calculate the W for both viscosities
    w1 = calc_w(visc1)
    w2 = calc_w(visc2)

    # Calculate m
    m = calc_m(w1, w2, temp1, temp2)

    # Calculate W for specific temperature
    w = w1 + m * (log10(temp1) - log10(temp))

    # Convert W to viscosity
    visc = w_to_visc(w)

    return visc

def celsius_to_kelvin(temp):
    return temp + 273.15

def calc_w(visc):
    # W = log(log(visc + 0.8))
    return log10(log10(visc+0.8))

def calc_m(w1, w2, temp1, temp2):
    return (w1 - w2) / (log10(temp2) - log10(temp1))

def w_to_visc(w):
    return math.pow(10, math.pow(10, w)) - 0.8

def log10(num):
    return math.log(num, 10)


if __name__ == '__main__':
    visc1 = 327
    temp1 = 20
    visc2 = 11.8
    temp2 = 99
    temp = 150
    x1 = 0
    x2 = 140
    n = 50
    print(get_visc(visc1, visc2, temp, temp1, temp2))
    get_visc_temp_graph_lin(visc1, visc2, x1, x2, n, temp1, temp2)

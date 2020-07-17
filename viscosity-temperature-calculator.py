# This program calculates the viscosity temperatur graph
# with the Ubbelohde-Walther-Algorithm

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator

# Get the Viscosity Temperature Plot with linear axis scaling
#### x1: x axis minimum
#### x2: x axis maximum
#### n: number of values on the x axis
def get_visc_temp_graph_lin(visc1, visc2, x1, x2, n=50, temp1=40, temp2=100, scaling="lin"):
    x_values = np.linspace(x1, x2, n)
    y_values = []
    for x in x_values:
        visc = get_visc(visc1, visc2, x, temp1, temp2)
        y_values.append(visc)
    #plot_visc_temp_graph_lin(x_values, y_values, x1, x2)
    plot_visc_temp_graph(x_values, y_values, x1, x2, scaling)

# Plot the Viscosity Temperature Graph with linear axis scaling
# def plot_visc_temp_graph_lin(x_values, y_values, x1, x2):
#     plt.plot(x_values, y_values)
#     plt.xlim(x1, x2)
#     plt.grid()
#     plt.show()

# Plot the Viscosity Temperature Graph with a specific scaling (linear or log)
def plot_visc_temp_graph(x_values, y_values, x1, x2, scaling):
    plt.plot(x_values, y_values)
    plt.xlim(x1, x2)
    plt.ylim()
    ax = plt.gca()

    # Scale the y axis if scaling is "log"
    if scaling == "log":
        # Set the y axis scaling to log log
        ax.set_yscale("function", functions=(forward, inverse))

    # Set the tick marks
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='both', width=1)
    ax.tick_params(which='major', length=6)
    ax.tick_params(which='minor', length=3)

    #plt.gca().set_xscale("log")

    # Label the diagram
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Kinematic Viscosity ($" + r"\f" + "rac{mm^2}{s}$)")
    plt.title("Temperature dependence of viscosity")

    # Color Formatting
    blue = "#002d72"
    grey = "#8a8d8f"
    

    # Font formatting

    plt.grid()
    plt.show()

# Both functions scale the y axis with log log
def forward(x):
    print(x)
    return np.log10(np.abs(np.log10(x)))
    #return [[log10(log10(i))] for i in x]

def inverse(x):
    print(x)
    return np.power(10, np.power(10, x))
    #return [[math.pow(10, math.pow(10, i))] for i in x]


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
    visc1 = 94.72
    temp1 = 40
    visc2 = 10.778
    temp2 = 100
    temp = -50
    x1 = 90
    x2 = 150
    n = 50
    scaling = "log"
    print(get_visc(visc1, visc2, temp, temp1, temp2))
    get_visc_temp_graph_lin(visc1, visc2, x1, x2, n, temp1, temp2, scaling)

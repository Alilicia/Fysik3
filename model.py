# Import av nödvändiga bibliotek
import numpy as np
import PySimpleGUI as psg
import matplotlib.pyplot as plt
import math

# Definerar funktionen som ska estimeras
def dy_dx(x, y):
    return -2 * y # dy_dx = funktionen

# Eulers stegmetod
def euler_method(dy_dx, initial_x, initial_y, step_size, number_steps):

    # Skapar listor där startvärdet för x och y är de första i respektive lista
    x_values = [initial_x]
    y_values = [initial_y]
    
    # Eulers stegmetod-funktion
    for i in range(number_steps):
        # Sätter att nuvarande x och y är lista elementet i respektive lista
        current_x = x_values[-1]
        current_y = y_values[-1]

        # Kalkylerar nästkommande värde genom Eulers stegmetod
        next_y = current_y + dy_dx(current_x, current_y) * step_size
        next_x = current_x + step_size

        # Lägger in x och y värden som nya element i respektive lista
        x_values.append(next_x)
        y_values.append(next_y)
    
    # Returnerar listor med respektive x och y värden
    return x_values, y_values

def physical_model_eulers_method(m, initial_x, initial_v, delta_t, number_steps, alpha, v):

    # Definerar parametrar och villkor
    t = 0
    x = initial_x
    y = 0
    v_x = initial_v * np.cos(np.radians(alpha))
    v_y = initial_v * np.sin(np.radians(alpha))
    theta = np.radians(alpha)
    positions = [(x, y)]
    g = 9.82

    # Genomför fysikalisk modell för projektil enligt eulers stegmetod
    for i in range(number_steps):
    
        F = m * -g
        a_y = F / m 

        # Tar ut hastighets komposanterna
        v_x = v * np.cos(theta)
        v_y = v * np.sin(theta)

        # Uppdaterar hasigheter
        v_x = v_x
        v_y = v_y + a_y * delta_t

        # Uppdaterar positionen
        x = x + v_x * delta_t
        y = y + v_y * delta_t

        # Tar fram ny vilken och ny hasighet
        v = np.sqrt(v_x ** 2 + v_y ** 2)
        theta = np.arctan2(v_y, v_x)

        print(f"{x},{y}")

        if y < 0:
            break

        positions.append((x, y))

    return positions

def euler_cromer_method(m, initial_x, initial_v, delta_t, number_steps, alpha, v):
    # Definerar parametrar och villkor
    t = 0
    x = initial_x
    y = 0
    v_x = initial_v * np.cos(np.radians(alpha))
    v_y = initial_v * np.sin(np.radians(alpha))
    theta = np.radians(alpha)
    positions = [(x, y)]
    g = 9.82

    # Genomför fysikalisk modell för projektil enligt eulers stegmetod
    for i in range(number_steps):
    
        F = m * -g
        a_y = F / m 

        # Tar ut hastighets komposanterna
        v_x = v * np.cos(theta)
        v_y = v * np.sin(theta)

        # Uppdaterar hasigheter
        v_x = v_x
        v_y = v_y + a_y * delta_t

        # Uppdaterar positionen
        x = x + v_x * delta_t
        y = y + v_y * delta_t

        # Tar fram ny vinkel och ny hasighet
        v = np.sqrt(v_x ** 2 + v_y ** 2)
        theta = np.arctan2(v_y, v_x)

        print(f"{x},{y}")

        if y < 0:
            break

        positions.append((x, y))

    return positions

def plot_solution(x_values, y_values, title):
    plt.plot(x_values, y_values, label='Approximated Solution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    initial_x = 0
    initial_v = 30
    initial_y = 0
    delta_t = 0.1
    number_steps = 100
    m = 0.5
    alpha = 45
    step_size = 0.1

    answer = input()

    if answer == "euler-cromer":
        positions = euler_cromer_method(m, initial_x, initial_v, delta_t, number_steps, alpha, initial_v)

        # Tar ut x och y koordninaterna
        x_values = [pos[0] for pos in positions]
        y_values = [pos[1] for pos in positions]

    elif answer == "euler":
        x_values, y_values = euler_method(dy_dx, initial_x, initial_y, step_size, number_steps)
    elif answer == "euler-physical":
        # Plockar ut koordninatvärden
        positions = physical_model_eulers_method(m, initial_x, initial_v, delta_t, number_steps, alpha, initial_v)

        # Tar ut x och y koordninaterna
        x_values = [pos[0] for pos in positions]
        y_values = [pos[1] for pos in positions]

        # Kallar på funktionen
        physical_model_eulers_method(m, initial_x, initial_v, delta_t, number_steps, alpha, initial_v)
    else:
        return

    plot_solution(x_values, y_values, answer)
                

if __name__ == "__main__":
    main()
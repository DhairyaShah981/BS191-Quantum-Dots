# import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt
import imageio

# Create the wave function for a particle in a box of length L and energy level n (n=1,2,3,...)
def psi(x, n, L):
    return np.sqrt(2/L)*np.sin(n*np.pi*x/L)


def create_plt(L, n):
    (ax1, ax2) = plt.subplots(2, sharex=True)
    plt.subplots_adjust(hspace=0)
    ax1.cla()
    ax2.cla()
    x = np.linspace(0, L, num=1000)

    plt.sca(ax1)
    plt.plot(x, psi(x, n, L))
    plt.title('Particle in a 1D box\n'+r'$L$='+str(L)+' bohr, $n$='+str(n))
    # Add y Label
    plt.ylabel(r'$\psi$')
    # Draw the walls of the box
    ymin = -np.sqrt(2/L)
    ymax = np.sqrt(2/L)
    margin = 0.1  # Allow 10% of margin for the x and y axis in both directions
    ylo = ymin*(1+margin)  # lower boundary for y axis
    yup = ymax*(1+margin)  # upper boundary for y axis
    # Left wall
    plt.plot([0, 0], [ylo, yup], 'gray', linewidth=5)
    # Right wall
    plt.plot([L, L], [ylo, yup], 'gray', linewidth=5)

    # Set grid
    plt.grid(True)
    plt.sca(ax2)
    plt.plot(x, psi(x, n, L)**2, c='r')
    plt.fill_between(x, psi(x, n, L)**2, color='r', alpha=0.5)
    # Add X and y Label
    plt.xlabel(r'$x$ (bohr)')
    plt.ylabel(r'$|\psi|^2$')

    # Draw the walls of the box
    ymin = -2/L
    ymax = 2/L
    margin = 0.1  # Allow 10% of margin for the x and y axis in both directions
    ylo = ymin*(1+margin)  # lower boundary for y axis
    yup = ymax*(1+margin)  # upper boundary for y axis
    # Left wall
    plt.plot([0, 0], [ylo, yup], 'gray', linewidth=5)
    # Right wall
    plt.plot([L, L], [ylo, yup], 'gray', linewidth=5)

    # Set the x and y ranges to display
    plt.ylim(ylo, yup)
    plt.xlim(-L*margin, L+L*margin)
    plt.grid(True)
    name = 'L='+str(L)+'_n='+str(n)+'.png'
    plt.savefig(name)
    return


frames = []

L_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for L in L_array:
    for n in N_array:
        create_plt(L, n)
        name = 'L='+str(L)+'_n='+str(n)+'.png'
        frames.append(imageio.imread(name))

imageio.mimsave('movie.gif', frames, fps=5)

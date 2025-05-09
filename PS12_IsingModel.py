import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

T = 2.27
B = 0.
iterations = 1000000
Nx, Ny = 200, 200
#Note: Curie point is 2.27
Nframes = 10
Ipf = iterations/Nframes
#Iterations per frame

fig, axes = plt.subplots(1, 2)
#initialize two plots
Model_frames = np.zeros((Nframes, Nx, Ny))
x_Magnetization = np.linspace(0, Nframes, Nframes)
#x-coordinate of magnetization
Mag_frames = np.zeros((Nframes, Nframes))
Mag_value = np.empty(Nframes)
Mag_value[:] = np.nan
#initial plot/value of magnetization: like numpy zero arrays for matplot
#This "nan method" is inspired by stackoverflow: 
#https://stackoverflow.com/questions/18697417/not-plotting-zero-in-matplotlib-or-change-zero-to-none-python


g = (-1)**np.random.randint(1, 3, size=(Nx, Ny))
#Set the initial model


for n in range(iterations):
    i, j = np.random.randint(Nx-1), np.random.randint(Ny-1)
    deltaU = 2*g[i,j]*(g[i-1, j]+g[i+1, j]+g[i, j+1]+g[i, j-1]) + 2*B*g[i,j]
    if deltaU <= 0:
        g[i,j] *= -1
    if deltaU > 0:
        if np.random.random() <= np.exp(-deltaU/T):
            g[i, j] *= -1
    if n%Ipf == 0:
        index = int(n/Ipf)
        Model_frames[index,:,:] = g
        #This animation starts with the image that has done alignment once. It
        #is not technical, but I don't wantbother complicating the problem.
        Mag_value[index] = np.sum(g)
        #updating the initial
        Mag_frames[index,:] = Mag_value
        # print(f'frame {index+1}')


Model_im = axes[0].imshow(Model_frames[0,:,:])
axes[0].set_title(f"{Nx}*{Ny} Simulation of the Ising Model, T = {T}")
axes[0].set_axis_off()
Mag_plot, = axes[1].plot(x_Magnetization, Mag_frames[0,:], color='c')
axes[1].set_title('Overall Magnetization')
axes[1].set_xlabel('Nth update (updates every 10,000 iterations)')
axes[1].set_ylabel('Value of Magnetization')
#Miscellaneous initial settings
ylim = np.amax(np.abs(Mag_value))
xlim = int(iterations/Nframes)
axes[1].set_ylim(-np.abs(ylim), np.abs(ylim))
axes[1].set_xlim(0, Nframes)
#Set proper x and y limit

def animate(i):
    Model_im.set_data(Model_frames[i,:,:])
    Mag_plot.set_ydata(Mag_frames[i,:])
    return Mag_plot, Model_im,
#This synchronous animate plot is a suggestion from Rob Owen :)

ani = animation.FuncAnimation(
    fig, animate, frames=range(Nframes), interval=100, blit=True, repeat=False)
plt.show()

Mean_Mag = Mag_value[-1]
print(f'Mean Magnetization = {Mean_Mag}')
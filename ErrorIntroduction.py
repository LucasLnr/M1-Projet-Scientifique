import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300

#%% Functions
    
def Epsilon(d,s):
    v = np.random.uniform(-d,d)
    return v*s
    
#%% Main 
delta_t = 0.71

tau = 1.2
N = 1
error_size = 2
scale = 10**(-0)

dotsize = 0.15

pick = 0

x = N

#%% Error distribution 

f_error = np.linspace(0, 100000,100001)
for x in range(len(f_error)):
    f_error[x] = Epsilon(2,1)

fig, (ax1,ax2) = plt.subplots(1,2,figsize=[12,5])
ax1.plot(f_error)
ax1.set_title("Error Samples")
ax1.set_xlabel('Sample')
ax1.set_ylabel('Error value in micrometers')
ax2.hist(f_error,bins=32)
ax2.set_title('Distribution')
ax2.set_xlabel('Error value in micrometers')
ax2.set_ylabel('Occurrences')
plt.show()

#%% Error introduction

parent_dir = 'C:\\Users\\orosi\\Desktop\\M1\\Projet scientifique\\Results'

lenght = N

for pick in range(lenght):
    
    directory = "Cell_"+str(pick)+" for N = "+str(x)
            
    file = open(parent_dir+'\\'+directory+'\\Cell_'+str(pick)+'_Px.txt','r')
    
    Pxread = file.readlines()
    Pxread_array = np.zeros(len(Pxread))
    
    for i in range(len(Pxread)):
        Pxread_array[i] = float(Pxread[i])
    file.close()
    
    Px_epsilon = np.zeros(len(Pxread))
    for i in range(len(Px_epsilon)):
        error = Epsilon(error_size,scale) 
        Px_epsilon[i] = Pxread_array[i] + error
    
#%% Computation of the velocity
    Vx_array = np.zeros(len(Pxread_array)-1)
    for i in range(len(Pxread_array)-1):
        Vx_array[i] = (Pxread_array[i+1] - Pxread_array[i])/delta_t
    
    Vx_epsilon = np.zeros(len(Px_epsilon)-1)
    for i in range(len(Px_epsilon)-1):
        Vx_epsilon[i] = (Px_epsilon[i+1] - Px_epsilon[i])/delta_t
    
#%% Computation of the acceleration
    Ax_array = np.zeros(len(Vx_array)-1)
    for i in range(len(Vx_array)-1):
        Ax_array[i] = (Vx_array[i+1] - Vx_array[i])/delta_t
    
    Ax_epsilon = np.zeros(len(Vx_epsilon)-1)
    for i in range(len(Vx_epsilon)-1):
        Ax_epsilon[i] = (Vx_epsilon[i+1] - Vx_epsilon[i])/delta_t
    
#%% Plotting acceleration against velocity
    plt.scatter(Vx_epsilon[:-1], Ax_epsilon, s = dotsize, marker = 'd', color = 'blue')
    plt.scatter(Vx_array[:-1], Ax_array, s = dotsize, color = 'red')

plt.title('Acceleration against velocities comparison')
plt.ylabel('Ax')
plt.xlabel('Vx')
plt.legend(['With errors','Classic'])
plt.savefig('1DRWEAVlong.png', dpi=200)
plt.show()

#%% 1D Random Walk Analysis

t = np.linspace(0,len(Pxread_array)-1,len(Pxread_array))

fig, ((ax1,ax2,ax3),(ax4,ax5,ax6)) = plt.subplots(2,3,figsize=[16,12])

for pick in range(1):
    
    directory = "Cell_"+str(pick)+" for N = "+str(x)
            
    file = open(parent_dir+'\\'+directory+'\\Cell_'+str(pick)+'_Px.txt','r')
    
    Pxread = file.readlines()
    Pxread_array = np.zeros(len(Pxread))
    
    for i in range(len(Pxread)):
        Pxread_array[i] = float(Pxread[i])
    file.close()
    
    Px_epsilon = np.zeros(len(Pxread))
    for i in range(len(Px_epsilon)):
        error = Epsilon(error_size,scale) 
        Px_epsilon[i] = Pxread_array[i] + error
    
    Vx_array = np.zeros(len(Pxread_array)-1)
    for i in range(len(Pxread_array)-1):
        Vx_array[i] = (Pxread_array[i+1] - Pxread_array[i])/delta_t
    
    Vx_epsilon = np.zeros(len(Px_epsilon)-1)
    for i in range(len(Px_epsilon)-1):
        Vx_epsilon[i] = (Px_epsilon[i+1] - Px_epsilon[i])/delta_t
    
    Ax_array = np.zeros(len(Vx_array)-1)
    for i in range(len(Vx_array)-1):
        Ax_array[i] = (Vx_array[i+1] - Vx_array[i])/delta_t
    
    Ax_epsilon = np.zeros(len(Vx_epsilon)-1)
    for i in range(len(Vx_epsilon)-1):
        Ax_epsilon[i] = (Vx_epsilon[i+1] - Vx_epsilon[i])/delta_t
    
    ax1.plot(t,Px_epsilon,color='cornflowerblue')
    ax1.plot(t,Pxread_array,color='lightcoral')

    ax2.plot(t[:-1],Vx_epsilon,color='blue')
    ax2.plot(t[:-1],Vx_array,color='red')
    
    ax3.plot(t[:-2],Ax_epsilon,color='midnightblue')
    ax3.plot(t[:-2],Ax_array,color='darkred')
    
    ax4.plot(t,Pxread_array-Px_epsilon,color='limegreen')
    
    ax5.plot(t[:-1],Vx_array-Vx_epsilon,color='forestgreen')
    
    ax6.plot(t[:-2],Ax_array-Ax_epsilon,color='darkgreen')
    
ax1.set_ylabel('x')
ax1.set_xlabel('timesteps')
ax1.set_title('Positions')
ax1.legend(['With errors','Classic'],loc=8)

ax2.set_title('Velocities')
ax2.set_xlabel('timesteps')
ax2.set_ylabel('Vx')
ax2.legend(['With errors','Classic'],loc=8)

ax3.set_xlabel('timesteps')
ax3.set_ylabel('Ax')
ax3.set_title('Accelerations')
ax3.legend(['With errors','Classic'],loc=8)

ax4.set_title('Errors on positions')
ax4.set_xlabel('timesteps')

ax5.set_title('Errors on velocities')
ax5.set_xlabel('timesteps')

ax6.set_title('Errors on accelerations')
ax6.set_xlabel('timesteps')

plt.savefig('1DRWElong.png', dpi = 300)
plt.show()

#%%

bin_a = int(max(Ax_epsilon))-int(min(Ax_epsilon))

plt.hist(Ax_epsilon,bins=3*bin_a,color='blue')
plt.hist(Ax_array,bins=3*bin_a, color='red')
plt.title("Acceleration distribution comparison")
plt.xlabel("Acceleration value")
plt.ylabel("Occurence")
plt.legend(['With errors','Classic'],loc=8)

plt.savefig("1DRWElongD.png",dpi=250)

plt.show()

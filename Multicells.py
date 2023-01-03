#%% Extensions

import numpy as np
import os
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300

#%% Functions
    
def unrv_sampling(): #unrd stand for : Unit Normal Random Variable
    return np.random.normal(0,1,1)
    
#%% Initialization

N = [1] #array containing the size of each population to simulate (N=[4] 1 simulation of 4 cells)

parent_dir = 'C:\\Users\\orosi\\Desktop\\M1\\Projet scientifique\\Results'

for x in N: 

    for w in range(x):
        
        directory = "Cell_"+str(w)+" for N = "+str(x)
        
        path = os.path.join(parent_dir,directory)
        
        os.makedirs(path)
        
        tau = 1.2
        
        Vx = 0
        # Vy = 0
        
        Px = 0
        # Py = 0
        
        t = 0
        
        delta_t = 0.71*10**(-0)
        delta_t_rsq=(delta_t)**0.5

        # t_stop = 135.2*(10**(-0))
        t_stop = 1000000
        
        Dsq=12.36
        
        Ax_array = list()
        # Ay_array = list()
        
        Vx_array = list()
        # Vy_array = list()
        
        Px_array = list()
        # Py_array = list()
        
        t_array = list()
        
        Vx_array.append(Vx)
        # Vy_array.append(Vy)
        
        Px_array.append(Px)
        # Py_array.append(Py)
        
        t_array.append(t)
    
#%% Calculation
        
        while t < t_stop:
            print(t)
            t += delta_t
            t_array.append(t)
        
            Px = Px + Vx*delta_t
            Px_array.append(Px)    
            unrv_sample = unrv_sampling()
            Vx = Vx - delta_t*Vx/tau + Dsq*unrv_sample*delta_t_rsq
            Vx_array.append(Vx)
        
            # Py = Py + Vy*delta_t
            # Py_array.append(Py)
            # unrv_sample = unrv_sampling()
            # Vy = Vy - delta_t*Vy/tau + Dsq*unrv_sample*delta_t_rsq
            # Vy_array.append(Vy)

        
        #print(w)
        
#%% Files creation
        
        np.savetxt("C:\\Users\\orosi\\Desktop\\M1\\Projet scientifique\\Results\\"+directory+"\\Cell_"+str(w)+"_Px.txt",Px_array)
        # np.savetxt("C:\\Users\\orosi\\Desktop\\M1\\Projet scientifique\\Results\\"+directory+"\\Cell_"+str(w)+"_Py.txt",Py_array)
        np.savetxt("C:\\Users\\orosi\\Desktop\\M1\\Projet scientifique\\Results\\"+directory+"\\Cell_"+str(w)+"_Vx.txt",Vx_array)
        # np.savetxt("C:\\Users\\orosi\\Desktop\\M1\\Projet scientifique\\Results\\"+directory+"\\Cell_"+str(w)+"_Vy.txt",Vy_array)
        
        # CALCUL DE AX
        
        file = open(parent_dir+'\\'+directory+'\\Cell_'+str(w)+'_Vx.txt','r')
    
        Vxtemp = file.readlines()
        Vxtemp_array = np.zeros(len(Vxtemp))
        for i in range(len(Vxtemp)):
            Vxtemp_array[i] = float(Vxtemp[i])
    
        Ax_array = list()
        for i in range(len(Vx_array)-1):
            Ax_array.append((Vxtemp_array[i+1]-Vxtemp_array[i])/delta_t)
            
        file.close()
        
        # CALCUL DE AY
        
        # file = open(parent_dir+'\\'+directory+'\\Cell_'+str(w)+'_Vy.txt','r')
    
        # Vytemp = file.readlines()
        # Vytemp_array = np.zeros(len(Vytemp))
        # for i in range(len(Vytemp)):
        #     Vytemp_array[i] = float(Vytemp[i])
    
        # Ay_array = list()
        # for i in range(len(Vy_array)-1):
        #     Ay_array.append((Vytemp_array[i+1]-Vytemp_array[i])/delta_t)    
        
        # file.close()
        
        np.savetxt("C:\\Users\\orosi\\Desktop\\M1\\Projet scientifique\\Results\\"+directory+"\\Cell_"+str(w)+"_Ax.txt",Ax_array)
        # np.savetxt("C:\\Users\\orosi\\Desktop\\M1\\Projet scientifique\\Results\\"+directory+"\\Cell_"+str(w)+"_Ay.txt",Ay_array)
    
#%% Plots : a(v)
    
    pick = 0
    
    for pick in range(x):
        
        directory = "Cell_"+str(pick)+" for N = "+str(x)
        
        file = open(parent_dir+'\\'+directory+'\\Cell_'+str(pick)+'_Vx.txt','r')
        Vxplot = file.readlines()
        Vxplot_array = np.zeros(len(Vxplot))
        for i in range(len(Vxplot)):
            Vxplot_array[i] = float(Vxplot[i])
        file.close()
        
        file = open(parent_dir+'\\'+directory+'\\Cell_'+str(pick)+'_Ax.txt','r')
        Axplot = file.readlines()
        Axplot_array = np.zeros(len(Axplot))
        for i in range(len(Axplot)):
            Axplot_array[i] = float(Axplot[i])
        file.close()        
            
        plt.scatter(Vxplot_array[:-1],Axplot_array,s=0.1)
    
    plt.title('Ax(Vx) for '+str(x)+' cells')
    plt.xlabel('Vx')
    plt.ylabel('Ax')
    plt.savefig('a',dpi=200)
    
    plt.show()


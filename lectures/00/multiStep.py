import numpy as np

## explicit Adams Bashforth method
def multiAB(flux, tspan, y_0, b):
    # Solving u'=F(u,t)
    # input: flux=F, tspan is a vector of times determining the RK steps
    # input: y_0 the initial condition with the first k values of the solution
    # input: b are k+1 b_j coefficients where the last one is 0
    N_time=len(tspan)  # N+1
    dim=y_0.shape[0]          # S
    y=np.zeros((dim,N_time))    # initializing the variable of solutions
    k = len(b)-1                # size of AB
    if y_0.shape[1] < k:
        raise ValueError("Input vector is too small")
    y[:,:k]=y_0                  # first timesteps 
    n0=k-1                       # last index assigned
    Fu=np.zeros((dim,k))         # Flux at internal stages
    for j in range(k):
        Fu[:,j]=flux(y[:,j])
    for n in range(n0,N_time-1):    # n=0,..., N-1
        delta_t=tspan[n+1]-tspan[n]
        y[:,n+1]=y[:,n]
        for j in range(k):
            y[:,n+1]=y[:,n+1]+delta_t*b[j]*Fu[:,j]
        Fu[:,:k-1] = Fu[:,1:]
        Fu[:,k-1] = flux(y[:,n+1])
    return tspan, y 



### ADAMS moulton Bashforth
# We combine the two methods, in order to get something positive
## explicit Adams Bashforth method
def multiAMB(flux, tspan, y_0, bAB, bAM):
    # Solving u'=F(u,t)
    # input: flux=F, tspan is a vector of times determining the RK steps
    # input: y_0 the initial condition with the first k values of the solution
    # input: bAB are k+1 b_j coefficients where the last one is 0 of Adam Bashforth
    # input: bAB are k b_j coefficients of Adams Moulton
    N_time=len(tspan)  # N+1
    dim=y_0.shape[0]          # S
    y=np.zeros((dim,N_time))    # initializing the variable of solutions
    k = len(bAB)-1                # size of AB
    if y_0.shape[1] < k:
        raise ValueError("Input vector is too small")
    y[:,:k]=y_0                  # first timesteps 
    n0=k-1                       # last index assigned
    Fu=np.zeros((dim,k))         # Flux at internal stages
    for j in range(k):
        Fu[:,j]=flux(y[:,j])
    for n in range(n0,N_time-1):    # n=0,..., N-1
        delta_t=tspan[n+1]-tspan[n]
        y[:,n+1]=y[:,n]
        for j in range(k):
            y[:,n+1]=y[:,n+1]+delta_t*bAB[j]*Fu[:,j]
        Fu[:,:k-1] = Fu[:,1:]
        Fu[:,k-1] = flux(y[:,n+1])
        y[:,n+1] = y[:,n]
        for j in range(k):
            y[:,n+1] =y[:,n+1] +delta_t*bAM[j]*Fu[:,j]
        Fu[:,k-1] =flux(y[:,n+1])
    return tspan, y 
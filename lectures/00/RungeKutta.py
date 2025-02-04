import numpy as np
from scipy import optimize

## explicit RK method
def explicitRK(flux, tspan, y_0, A, b, c):
    """
    # Solving u'=F(u,t)
    # input: flux=F, tspan is a vector of times determining the RK steps
    # input: y_0 the initial condition
    # input: A,b,c are matrix and vectors of RK methods
    """
    N_time=len(tspan)  # N+1
    dim=len(y_0)          # S
    y=np.zeros((dim,N_time))    # initializing the variable of solutions    
    y[:,0]=y_0                 # first timestep 
    S=np.shape(A)[0]
    u=np.zeros((dim,S))       # Internal stages
    Fu=np.zeros((dim,S))       # Flux at internal stages
    for n in range(N_time-1):    # n=0,..., N-1
        delta_t=tspan[n+1]-tspan[n]
        for k in range(S):
            u[:,k]=y[:,n] 
            for j in range(k):
                u[:,k] =u[:,k]+ delta_t*A[k,j]*Fu[:,j]
            Fu[:,k] = flux(u[:,k],tspan[n]+delta_t*c[k])
        y[:,n+1]=y[:,n]
        for j in range(S):
            y[:,n+1]=y[:,n+1]+delta_t*b[j]*Fu[:,j]
    return tspan, y 

## explicit RK method
def explicitRelaxRK(flux, y_0, dt0, T_fin, KtMax,  A, b, c):
    # Solving u'=F(u,t)
    # input: flux=F, tspan is a vector of times determining the RK steps
    # input: y_0 the initial condition
    # dt0 is the basic time interval, that will be modified along the steps
    # T_fin is the final time
    # KtMax is maximum number of timesteps
    # input: A,b,c are matrix and vectors of RK methods
    dim=len(y_0)          # S
    y=np.zeros((dim,KtMax))    # initializing the variable of solutions
    tspan=np.zeros(KtMax)      # times will be stored here
    gammas = np.zeros(KtMax)   # Gamma relaxation coefficients
    time= 0.
    gammas[0] = 1
    n=0                        # Time step index
    tspan[0] = time
    y[:,0]=y_0                 # first timestep 
    S=np.shape(A)[0]
    u=np.zeros((dim,S))       # Internal stages
    Fu=np.zeros((dim,S))       # Flux at internal stages
    while(time<T_fin and n<KtMax):    # n=0,..., N-1
        delta_t=min(dt0,T_fin-time)
        #Classic RK step
        for k in range(S):
            u[:,k]=y[:,n] 
            for j in range(k):
                u[:,k] = u[:,k]+ delta_t*A[k,j]*Fu[:,j]
            Fu[:,k] = flux(u[:,k],tspan[n]+delta_t*c[k])
        yn1=y[:,n]
        for j in range(S):
            yn1=yn1+delta_t*b[j]*Fu[:,j]
        # Compute the relaxation gamma
        deltay = yn1-y[:,n]
        sumBScal=0.
        for j in range(S):
            sumBScal=sumBScal + b[j]* np.dot(u[:,j]-y[:,n],Fu[:,j])
        gamma = 2* delta_t* sumBScal/np.dot(deltay,deltay)
        # Update the n+1 values
        y[:,n+1]=y[:,n] +gamma*deltay
        if (time+delta_t<T_fin -10**-16):
            time = time + gamma*delta_t
        else:
            time=T_fin
        tspan[n+1]=time
        gammas[n+1]=gamma
        n=n+1
        
    return tspan[:n+1], y[:,:n+1] , gammas[:n+1]


## explicit RK method
def explicitRelaxRKEntropy(flux, entropy, e_v, y_0, dt0, T_fin, KtMax,  A, b, c):
    # Solving u'=F(u,t)
    # input: flux=F, tspan is a vector of times determining the RK steps
    # entropy: scalar function of y
    # entropy variable e_v: vector function of y
    # input: y_0 the initial condition
    # dt0 is the basic time interval, that will be modified along the steps
    # T_fin is the final time
    # KtMax is maximum number of timesteps
    # input: A,b,c are matrix and vectors of RK methods
    dim=len(y_0)          # S
    y=np.zeros((dim,KtMax))    # initializing the variable of solutions
    tspan=np.zeros(KtMax)      # times will be stored here
    gammas = np.zeros(KtMax)   # Gamma relaxation coefficients
    time= 0.
    gammas[0] = 1
    n=0                        # Time step index
    tspan[0] = time
    y[:,0]=y_0                 # first timestep 
    S=np.shape(A)[0]
    u=np.zeros((dim,S))       # Internal stages
    Fu=np.zeros((dim,S))       # Flux at internal stages
    while(time<T_fin and n<KtMax):    # n=0,..., N-1
        ent0=entropy(y[:,n])
        e_v0 = e_v(y[:,n])
        delta_t=min(dt0,T_fin-time)
        #Classic RK step
        for k in range(S):
            u[:,k]=y[:,n] 
            for j in range(k):
                u[:,k] = u[:,k]+ delta_t*A[k,j]*Fu[:,j]
            Fu[:,k] = flux(u[:,k],tspan[n]+delta_t*c[k])
        yn1=y[:,n]
        for j in range(S):
            yn1=yn1+delta_t*b[j]*Fu[:,j]
        # Compute the relaxation gamma
        deltay = yn1-y[:,n]
        sumBScal=0.
        for j in range(S):
            sumBScal=sumBScal + b[j]* np.dot(e_v(u[:,j]),Fu[:,j])
        residual = lambda gamma: np.array(entropy(np.array(y[:,n]+gamma*deltay,dtype=np.float))-ent0-gamma*delta_t*sumBScal, dtype=float)
        deriv_res = lambda gamma: np.array(np.dot(e_v(np.array(y[:,n]+gamma*deltay,dtype=np.float)),deltay)-delta_t*sumBScal, dtype=float)
        gamma = optimize.newton(residual,np.array([1.]),fprime=deriv_res,tol=10**-13) #broyden1(residual,1.,f_tol=10**-13)
        # Update the n+1 values
        y[:,n+1]=y[:,n] +gamma*deltay
        if (time+delta_t<T_fin -10**-16):
            time = time + gamma*delta_t
        else:
            time=T_fin
        tspan[n+1]=time
        gammas[n+1]=gamma
        n=n+1
        
    return tspan[:n+1], y[:,:n+1] , gammas[:n+1]

# Simple implementation of the method
# Input are F, (t^0,...,t^N), y_0
def explicitEuler(func, tspan, y_0):
    N_time=len(tspan)  # N+1
    dim=len(y_0)          # S
    y=np.zeros((dim,N_time))    # initializing the variable of solutions    
    y[:,0]=y_0                 # first timestep 
    for n in range(N_time-1):    # n=0,..., N-1
        y[:,n+1]=y[:,n]+(tspan[n+1]-tspan[n])*func(y[:,n],tspan[n])
    return tspan, y 



# Simple implementation of the method
# Input are F, (t^0,...,t^N), y_0
def implicitEuler(func, jac_func, tspan, y_0):
    '''
    Implicit Euler method with a nonlinear solver
    Input:
    func (nonlinear) function of the ODE, takes input u, t
    jac_func jacobian wrt to u of func, takes input u, t
    tspan vector of timesteps (t^0,...,t^N)
    y_0 initial value    
    '''
    N_time=len(tspan)  # N+1
    dim=len(y_0)          # S
    y=np.zeros((dim,N_time))    # initializing the variable of solutions    
    y[:,0]=y_0                 # first timestep 
    for n in range(N_time-1):    # loop through timesteps n=0,..., N-1
        # define the nonlinear function to be solved
        res = lambda yn1: yn1 -y[:,n] -(tspan[n+1]-tspan[n])*func(yn1,tspan[n+1])
        jacRes = lambda yn1: np.eye(dim) - (tspan[n+1]-tspan[n])*jac_func(yn1,tspan[n+1])
        z = optimize.newton(res, y[:,n], fprime=jacRes) # using Newton's method from scipy.optimize
        y[:,n+1] = z
    return tspan, y 

def CrankNicolson(func, jac_func, tspan, y_0):
    '''
    Crank-Nicolson method with a nonlinear solver
    Input:
    func (nonlinear) function of the ODE, takes input u, t
    jac_func jacobian wrt to u of func, takes input u, t
    tspan vector of timesteps (t^0,...,t^N)
    y_0 initial value    
    '''
    N_time=len(tspan)  # N+1
    dim=len(y_0)          # S
    y=np.zeros((dim,N_time))    # initializing the variable of solutions    
    y[:,0]=y_0                 # first timestep 
    for n in range(N_time-1):    # loop through timesteps n=0,..., N-1
        # define the nonlinear function to be solved
        res = lambda yn1: yn1 -y[:,n] -(tspan[n+1]-tspan[n])*0.5*(func(yn1,tspan[n+1])+func(y[:,n],tspan[n]))
        jacRes = lambda yn1: np.eye(dim) - 0.5*(tspan[n+1]-tspan[n])*jac_func(yn1,tspan[n+1])
        z = optimize.root(res, y[:,n], jac=jacRes) # using Newton's method from scipy.optimize
        y[:,n+1] = z.x
    return tspan, y 

def IRK(func, jac_func, A, b, tspan, y_0):
    '''
    Implicit RK method with a nonlinear solver
    Input:
    func (nonlinear) function of the ODE, takes input u, t
    jac_func jacobian wrt to u of func, takes input u, t
    tspan vector of timesteps (t^0,...,t^N)
    y_0 initial value    
    '''
    N_time=len(tspan)  # N+1
    dim=len(y_0)          # S
    y=np.zeros((dim,N_time))    # initializing the variable of solutions   
    RKdim = np.shape(A)[0]     # RK dimension 
    c = np.sum(A,axis=1)       # c RK
    y[:,0]=y_0                 # first timestep
    un = np.zeros((dim * RKdim)) # vector of previous value for RK
    t_loc = np.zeros(RKdim)


    for n in range(N_time-1):    # loop through timesteps n=0,..., N-1
        dt = tspan[n+1]-tspan[n] #timestep
        for i in range(RKdim):  # creating vector dimension dim*NRK with un everywhere
            un[i*dim:(i+1)*dim] = y[:,n]
            t_loc[i] = tspan[n] + dt*c[i]  # times of stages

        def res_RK(u):
            """residual equation of implicit RK """
            res = np.zeros(len(u))
            ff = np.zeros(len(u)) # [func(u^{(1)}),...,func(u^{(NRK)})]
            for i in range(RKdim):
                ff[i*dim:(i+1)*dim] = func(u[i*dim:(i+1)*dim],t_loc[i])
            for i in range(RKdim): # U-y^n-A F(U)
                res[i*dim:(i+1)*dim] = u[i*dim:(i+1)*dim] - y[:,n] 
                for j in range(RKdim):
                    res[i*dim:(i+1)*dim] = res[i*dim:(i+1)*dim]\
                        -dt*A[i,j]*ff[j*dim:(j+1)*dim]
            return res
        
        def jac_res_RK(u):
            """jacobian of the residual equation"""
            jac = np.zeros((len(u),len(u))) # dimension (dim*NRK)^2
            jj = np.zeros((len(u),dim))
            for i in range(RKdim): # jacobian of rhs in each variable u^{(i)}
                jj[i*dim:(i+1)*dim,:] = jac_func(u[i*dim:(i+1)*dim],t_loc[i])
            for i in range(RKdim): 
                # jacobian in cell [i,j] of dimension dim x dim
                # is \delta_{ij} I_dim -dt A_ij J_u F(u^{(j)})
                jac[i*dim:(i+1)*dim,i*dim:(i+1)*dim] = np.eye(dim)
                for j in range(RKdim):
                    jac[i*dim:(i+1)*dim,j*dim:(j+1)*dim]=\
                        jac[i*dim:(i+1)*dim,j*dim:(j+1)*dim] \
                        -dt*A[i,j]*jj[j*dim:(j+1)*dim,:]
            return jac

        # finding the solution of the residual equation 
        z = optimize.root(res_RK, un, jac=jac_res_RK, method="lm")
        
        # reconstructing at new timestep
        y[:,n+1] = y[:,n]
        for i in range(RKdim):
            y[:,n+1] = y[:,n+1] + dt*b[i]*func(z.x[i*dim:(i+1)*dim],t_loc[i])
    return tspan, y 

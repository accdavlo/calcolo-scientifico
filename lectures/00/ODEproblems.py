import numpy as np
from nodepy import ivp
C5ivp = ivp.detest('C5')

## Linear scalar Dahlquist's equation
def linear_scalar_flux(u,t=0,k_coef=10):
    ff=np.zeros(np.shape(u))
    ff[0]= -k_coef*u[0]
    return ff

def linear_scalar_exact_solution(u0,t,k_coef=10):
    return np.array([np.exp(-k_coef*u0[0]*t)])


def linear_scalar_jacobian(u,t=0,k_coef=10):
    Jf=np.zeros((len(u),len(u)))
    Jf[0,0]=-k_coef
    return Jf


## Stiff scalar 
def stiff_scalar_flux(u,t=0.,k_coef=2000.):
    ff=np.zeros(len(u))
    ff[0]= -k_coef*(u[0]-np.cos(t))
    return ff

def stiff_scalar_jacobian(u,t=0,k_coef=2000.):
    Jf=np.zeros((len(u),len(u)))
    Jf[0,0]=-k_coef
    return Jf

#nonlinear problem y'=-ky|y| +1  
def nonlinear_scalar_flux(u,t=0,k_coef=10):
    ff=np.zeros(np.shape(u))
    ff[0]=-k_coef*abs(u[0])*u[0] +1
    return ff


def nonlinear_scalar_exact_solution(u0,t,k_coef = 10):
        sqrtk = np.sqrt(k_coef)
        ustar = 1 / sqrtk
        if u0[0] >= ustar:
            uex=np.array([1./np.tanh(sqrtk * t + np.arctanh(1/sqrtk /u0[0])) / sqrtk])
        elif u0[0] < 0 and t < - np.atan(sqrtk * u0[0]) / sqrtk:
            uex=np.array([np.tan(sqrtk * t + np.arctan(sqrtk * u0[0])) / sqrtk])
        else:
            uex=np.array([np.tanh(sqrtk * t + np.arctanh(sqrtk * u0[0])) / sqrtk])
        return uex

def nonlinear_scalar_jacobian(u,t=0,k_coef=10):
    Jf=np.zeros((len(u),len(u)))
    Jf[0,0]=-k_coef*abs(u[0])
    return Jf


# SYSTEMS


# linear systems
def linear_system2_flux(u,t=0):
    d=np.zeros(len(u))
    d[0]= -5*u[0] + u[1]
    d[1]= 5*u[0] -u[1]
    return d


def linear_system2_exact_solution(u0,t):
    A=np.array([[-5,1],[5,-1]])
    u_e=u0+(1-np.exp(-6*t))/6*np.dot(A,u0)
    return u_e

def linear_system2_jacobian(u,t=0):
    Jf=np.array([[-5,1],[5,-1]])
    return Jf

linear_system2_matrix = np.array([[-5,1],[5,-1]])

def linear_system2_production_destruction(u,t=0):
    p=np.zeros((len(u),len(u)))
    d=np.zeros((len(u),len(u)))
    p[0,1]=u[1]
    d[1,0]=u[1]
    p[1,0]=5*u[0]
    d[0,1]=5*u[0]
    return p,d

#lin system 3 x3

def linear_system3_flux(u,t=0):
    d=np.zeros(len(u))
    d[0]= -u[0] + 3*u[1]
    d[1]= -3*u[1] + 5*u[2]
    d[2]= -5*u[2] 
    return d


def linear_system3_exact_solution(u0,t=0):
    u_e = np.zeros(len(u0))
    u_e[0] = 15.0/8.0*u0[2]*(np.exp(-5*t) - 2*np.exp(-3*t)+np.exp(-t))
    u_e[1] = 5.0/2.0*u0[2]*(-np.exp(-5*t) + np.exp(-3*t))
    u_e[2] = u0[2]*np.exp(-5*t)
    return u_e
def linear_system3_jacobian(u,t=0):
    Jf=np.zeros((len(u),len(u)))
    Jf[0,0]=-1.
    Jf[0,1]=3
    Jf[1,1] = -3
    Jf[1,2] = 5
    Jf[2,2] = -5 
    return Jf


#lin system 3 x3

def linear_system3_speeds_flux(u,t=0):
    A =  np.array([[0, -1,1],[1,1,3],[-1,1,0]])
    A1 = 1./15.*np.array([[-9, 3 ,-12],[-9,3,3],[6,3,3]])

    Ma= np.array([[0, 0,1],[0,0,0],[-1,0,0]])
    Mb= np.array([[0, 0,0],[0,-100,0],[0,0,0]])
    Na = A@Ma@A1
    Nb = A@Mb@A1

    return (Na+Nb)@u


def linear_system3_speeds_exact_solution(u0,t=0):
    A =  np.array([[0, -1,1],[1,1,3],[-1,1,0]])
    A1 = 1./15.*np.array([[-9, 3 ,-12],[-9,3,3],[6,3,3]])

    Ma= np.array([[0, 0,1],[0,0,0],[-1,0,0]])
    Mb= np.array([[0, 0,0],[0,-100,0],[0,0,0]])
    Na = A@Ma@A1
    Nb = A@Mb@A1

    x0 = A1@u0
    x = np.zeros(3)
    x[1] = np.exp(-100*t)*x0[1]
    x[0] = np.sin(t)*x0[2] + np.cos(t)*x0[0]
    x[2] = np.cos(t)*x0[2] - np.sin(t)*x0[0]
    return A@x

def linear_system3_speeds_jacobian(u,t=0):
    A =  np.array([[0, -1,1],[1,1,3],[-1,1,0]])
    A1 = 1./15.*np.array([[-9, 3 ,-12],[-9,3,3],[6,3,3]])

    Ma= np.array([[0, 0,1],[0,0,0],[-1,0,0]])
    Mb= np.array([[0, 0,0],[0,-100,0],[0,0,0]])
    Na = A@Ma@A1
    Nb = A@Mb@A1
    return Na+Nb



## Nonlinear 3x3 system production destruction
def nonlinear_system3_flux(u,t=0):
    ff=np.zeros(len(u))
    ff[0]= -u[0]*u[1]/(u[0]+1)
    ff[1]= u[0]*u[1]/(u[0]+1) -0.3*u[1]
    ff[2]= 0.3*u[1]
    return ff

def nonlinear_system3_production_destruction(u,t=0):
    p=np.zeros((len(u),len(u)))
    d=np.zeros((len(u),len(u)))
    p[1,0]=u[0]*u[1]/(u[0]+1)
    d[0,1]=p[1,0]
    p[2,1]=0.3*u[1]
    d[1,2]=p[2,1]
    return p,d


# SIR Model
def SIR_flux(u,t=0,beta=3,gamma=1):
    ff=np.zeros(len(u))
    N=np.sum(u)
    ff[0]=-beta*u[0]*u[1]/N
    ff[1]=+beta*u[0]*u[1]/N - gamma*u[1]
    ff[2]= gamma*u[1]
    return ff

def SIR_jacobian(u,t=0,beta=3,gamma=1):
    Jf=np.zeros((len(u),len(u)))
    N=np.sum(u)
    Jf[0,0]=-beta*u[1]/N
    Jf[0,1]=-beta*u[0]/N
    Jf[1,0]= beta*u[1]/N
    Jf[1,1]= beta*u[0]/N - gamma
    Jf[2,1] = gamma 
    return Jf

def SIR_production_destruction(u,t=0,beta=3,gamma=1):
    p=np.zeros((len(u),len(u)))
    d=np.zeros((len(u),len(u)))
    N=np.sum(u)
    p[1,0]=beta*u[0]*u[1]/N
    d[0,1]=p[1,0]
    p[2,1]=gamma*u[1]
    d[1,2]=p[2,1]
    return p,d

# Nonlinear_oscillator
def nonLinearOscillator_flux(u,t=0.,alpha=0.):
    ff=np.zeros(np.shape(u))
    n=np.sqrt(np.dot(u,u))
    ff[0]=-u[1]/n-alpha*u[0]
    ff[1]=u[0]/n - alpha*u[1]
    return ff

def nonLinearOscillator_jacobian(u,t=0.,alpha=0.):
    n=np.sqrt(np.dot(u,u))
    Jf = np.array([
        [u[0]*u[1]/n**3-alpha, u[1]**2/n**3-1./n],
        [-u[0]**2/n**3+1./n, -u[0]*u[1]/n**3-alpha]
    ])
    return Jf

def nonLinearOscillator_exact_solution(u0,t=0.,alpha=0.):
    u_ex=np.zeros(np.shape(u0))
    n=np.sqrt(np.dot(u0,u0))
    if abs(alpha)<1e-14:
        theta=t/n
    else:
        theta = (np.exp(alpha*t)-1.)/alpha/n
    A = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
    u_ex = np.exp(-alpha *t )*A@u0
    return u_ex

def nonLinearOscillator_entropy(u,t=0,alpha=0.):
    return np.dot(u,u)/2.

def nonLinearOscillator_entropy_variable(u,t=0,alpha=0.):
    return u



# pendulum
def pendulum_flux(u,t=0):
    ff=np.zeros(np.shape(u))
    ff[0]=u[1]
    ff[1]=-np.sin(u[0])
    return ff

def pendulum_jacobian(u,t=0):
    Jf=np.zeros((2,2))
    Jf[0,1]=1.
    Jf[1,0]=np.cos(u[0])
    return Jf

def pendulum_entropy(u,t=0):
    return np.array(0.5*u[1]**2.-np.cos(u[0]), dtype=np.float)

def pendulum_entropy_variables(u,t=0):
    v=np.zeros(np.shape(u))
    v[0]=np.sin(u[0])
    v[1]=u[1]
    return v


# Robertson
def Robertson_flux(u,t=0,alpha=10**4,beta=0.04, gamma=3*10**7):
    ff=np.zeros(np.shape(u))
    ff[0] = alpha*u[1]*u[2]-beta*u[0]
    ff[1] = beta*u[0]-alpha*u[1]*u[2] - gamma*u[1]**2
    ff[2] = gamma*u[1]**2
    return ff

def Robertson_jacobian(u,t=0,alpha=10**4,beta=0.04, gamma=3*10**7):
    Jf=np.zeros((3,3))
    Jf[0,0]= -beta 
    Jf[0,1]= alpha*u[2]
    Jf[0,2]= alpha*u[1]
    Jf[1,0]= beta
    Jf[1,1]= -alpha*u[2]-2*gamma*u[1]
    Jf[1,2]= -alpha*u[1]
    Jf[2,1] = 2*gamma*u[1] 
    return Jf

def Robertson_production_destruction(u,t=0,alpha=10**4,beta=0.04, gamma=3*10**7):
    p=np.zeros((len(u),len(u)))
    d=np.zeros((len(u),len(u)))
    p[0,1]=alpha*u[1]*u[2]
    d[1,0]=p[0,1]
    p[1,0]=beta*u[0]
    d[0,1]=p[1,0]
    p[2,1]=gamma*u[1]**2
    d[1,2]=p[2,1]
    return p,d

def Robertson_rhs(u,t=0):
    return np.zeros(3)

  
# Lotka:
def lotka_flux(u,t=0,alpha=1,beta=0.2,delta=0.5,gamma=0.2):
    ff=np.zeros(np.shape(u))
    ff[0]=alpha*u[0]-beta*u[0]*u[1]
    ff[1]=delta*beta*u[0]*u[1]-gamma*u[1]
    return ff

def lotka_jacobian(u,t=0,alpha=1,beta=0.2,delta=0.5,gamma=0.2):
    Jf=np.zeros((2,2))
    Jf[0,0] = alpha -beta*u[1]
    Jf[0,1] = -beta*u[0]
    Jf[1,0] = delta*beta*u[1]
    Jf[1,1] = delta*beta*u[0] -gamma
    return Jf

def lotka_entropy(u,t=0,alpha=1,beta=0.2,delta=0.5,gamma=0.2):
    return np.array(delta*beta*u[0]-gamma*np.log(u[0])+beta*u[1]-alpha*np.log(u[1]), dtype=np.float)

def lotka_entropy_variables(u,t=0,alpha=1,beta=0.2,delta=0.5,gamma=0.2):
    v=np.zeros(np.shape(u))
    v[0]=delta*beta-gamma/u[0]
    v[1]=beta-alpha/u[1]
    return v

#3 bodies problem in 2D: U=(x_1,x_2,v_1,v_2,y_1,y_2,w_1,w_2,z_1,z_2,s_1,s_2)
# where x is the 2D position of body1 and v is speed body1 sun
# y, w are position and velocity body2 earth
# z, s are position and velocity body3 mars

def threeBodies_flux(u,t=0):
    m1=1.98892*10**30
    m2=5.9722*10**24
    m3=6.4185*10**23
    G=6.67*10**(-11)
    f=np.zeros(np.shape(u))
    x=u[0:2]
    v=u[2:4]
    y=u[4:6]
    w=u[6:8]
    z=u[8:10]
    s=u[10:12]
    dxy3=sum(abs(x-y)**2)**(3./2.)#np.linalg.norm(x-y)**3
    dxz3=sum(abs(x-z)**2)**(3./2.)#np.linalg.norm(x-z)**3
    dyz3=sum(abs(z-y)**2)**(3./2.)#np.linalg.norm(y-z)**3
    f[0:2]=v
    f[2:4]=-m2*G/dxy3*(x-y)-m3*G/dxz3*(x-z)
    f[4:6]=w
    f[6:8]=-m1*G/dxy3*(y-x)-m3*G/dyz3*(y-z)
    f[8:10]=s
    f[10:12]=-m1*G/dxz3*(z-x)-m2*G/dyz3*(z-y)
    return f

def square_entropy(u):
    return sum(u**2)/2.


def square_entropy_variable(u):
    return u



def vibratingDamped_flux(u,t, m_coef,r_coef, k_coef, f_coef, omega_coef, phi_coef):
    f=np.zeros(np.shape(u))
    f[0] = u[1]
    f[1] = -r_coef/m_coef*u[1] - k_coef/m_coef*u[0] + f_coef/m_coef*np.cos(omega_coef*t+phi_coef)
    return f

def vibratingDamped_exact_solution(u0,t, m_coef,r_coef, k_coef, f_coef, omega_coef, phi_coef):
    Y_p = f_coef/np.sqrt((-m_coef*omega_coef**2+k_coef)**2+omega_coef**2*r_coef**2)
    psi = phi_coef - np.arctan2(omega_coef*r_coef,-m_coef*omega_coef**2+k_coef)
    y_p = Y_p*np.cos(omega_coef*t+psi)
    alpha = r_coef/m_coef
    beta = k_coef/m_coef
    delta = alpha**2 -4*beta
    if delta > 0:
        l1 = 0.5*(-alpha - np.sqrt(delta))
        l2 = 0.5*(-alpha + np.sqrt(delta)) 
        bb = np.array([u0[0]-Y_p*np.cos(psi),\
                       u0[1]+Y_p*omega_coef*np.sin(psi)])
        AA = np.array([[1. , 1.],[ l1, l2 ]])
        cc = np.linalg.solve(AA,bb)
        y = cc[0]*np.exp(l1*t) + cc[1]*np.exp(l2*t)
    elif delta ==0:
        l = 0.5*(-alpha)
        c1 = u0[0] - Y_p*np.cos(psi)
        c2 = u0[1] +Y_p * omega_coef*np.sin(psi) -c1*l
        y = c1*np.exp(l*t) + c2*t*np.exp(l*t)
    elif delta <0:
        theta = np.sqrt(-delta)/2
        c1 = u0[0] - Y_p *np.cos(psi) 
        c2 = (u0[1] +Y_p*omega_coef * np.sin(psi)+ alpha/2*c1 )/theta 
        y = np.exp(-alpha/2*t)*(c1*np.cos(theta*t)+c2*np.sin(theta*t))
    u_e = y+y_p
    return u_e

class ODEproblem:
    def __init__(self,name):
        self.name=name
        if self.name=="linear_scalar":
            self.u0 = np.array([1.])
            self.T_fin= 2.
            self.k_coef=10
            self.matrix=np.array([-self.k_coef])
        elif self.name=="stiff_scalar":
            self.k_coef=2000.
            self.u0 = np.array([0.])
            self.T_fin= 1.5
        elif self.name=="nonlinear_scalar":
            self.k_coef=10
            self.u0 = np.array([1.1/np.sqrt(self.k_coef)])
            self.T_fin= 1.
        elif self.name=="linear_system2":
            self.u0 = np.array([0.9,0.1])
            self.T_fin= 1.
            self.matrix = np.array([[-5,1],[5,-1]])
        elif self.name=="linear_system3":
            self.u0 = np.array([0,0.,10.])
            self.T_fin= 10.
        elif self.name=="linear_system3_speeds":
            self.u0 = np.array([-1.,2.,0.])
            self.T_fin= 10.
        elif self.name=="nonlinear_system3":
            self.u0 = np.array([9.98,0.01,0.01])
            self.T_fin= 30.
        elif self.name=="SIR":
            self.u0 = np.array([1000.,1,10**-20])
            self.T_fin= 10.
        elif self.name=="nonLinearOscillator":
            self.u0 = np.array([1.,0.])
            self.T_fin= 50
            self.alpha = 0.
        elif self.name=="nonLinearOscillatorDamped":
            self.u0 = np.array([1.,0.])
            self.T_fin= 50
            self.alpha = 0.01
        elif self.name=="pendulum":
            self.u0 = np.array([2.,0.])
            self.T_fin= 50
        elif self.name=="Robertson":
            self.u0 = np.array([1.,10**-20,10**-20])
            self.T_fin= 10.**10.
        elif self.name=="lotka":
            self.u0 = np.array([1.,2.])
            self.T_fin= 100.
        elif self.name=="threeBodies":
            self.u0 = np.array([0,0,0,0,149*10**9,0,0,30*10**3,-226*10**9,0,0,-24.0*10**3])
            self.T_fin= 10.**8.
        elif self.name == "vibratingDamped":
            self.u0 = np.array([0.5, 0.25])
            self.T_fin = 4.
            self.m_coef = 5.
            self.r_coef = 2
            self.k_coef = 5.
            self.f_coef = 1.
            self.omega_coef = 2.
            self.phi_coef = 0.1
        elif self.name == "C5":
            self.u0 = C5ivp.u0
            self.u0 = C5ivp.u0
            self.T_fin = C5ivp.T
        else:
            raise ValueError("Problem not defined")

    def flux(self,u,t=0):
        if self.name=="linear_scalar":
            return linear_scalar_flux(u,t,self.k_coef)
        elif self.name=="stiff_scalar":
            return stiff_scalar_flux(u,t,self.k_coef)
        elif self.name=="nonlinear_scalar":
            return nonlinear_scalar_flux(u,t,self.k_coef)
        elif self.name=="linear_system2":
            return linear_system2_flux(u,t)
        elif self.name=="linear_system3":
            return linear_system3_flux(u,t)
        elif self.name=="linear_system3_speeds":
            return linear_system3_speeds_flux(u,t)
        elif self.name=="nonlinear_system3":
            return nonlinear_system3_flux(u,t)
        elif self.name=="SIR":
            return SIR_flux(u,t)
        elif self.name=="nonLinearOscillator":
            return nonLinearOscillator_flux(u,t,self.alpha)
        elif self.name=="nonLinearOscillatorDamped":
            return nonLinearOscillator_flux(u,t,self.alpha)
        elif self.name=="pendulum":
            return pendulum_flux(u,t)
        elif self.name=="Robertson":
            return Robertson_flux(u,t)
        elif self.name=="lotka":
            return lotka_flux(u,t)
        elif self.name=="threeBodies":
            return threeBodies_flux(u,t)
        elif self.name=="vibratingDamped":
            return vibratingDamped_flux(u,t,self.m_coef,self.r_coef, self.k_coef, self.f_coef, self.omega_coef, self.phi_coef)
        elif self.name == "C5":
            return C5ivp.rhs(t,u)
        else:
            raise ValueError("Flux not defined for this problem")
        
    def jacobian(self,u,t=0):
        if self.name=="linear_scalar":
            return linear_scalar_jacobian(u,t,self.k_coef)
        elif self.name=="stiff_scalar":
            return nonlinear_scalar_jacobian(u,t,self.k_coef)
        elif self.name=="nonlinear_scalar":
            return nonlinear_scalar_jacobian(u,t,self.k_coef)
        elif self.name=="linear_system2":
            return linear_system2_jacobian(u,t)
        elif self.name=="linear_system3":
            return linear_system3_jacobian(u,t)
        elif self.name=="linear_system3_speeds":
            return linear_system3_speeds_jacobian(u,t)
        elif self.name=="pendulum":
            return pendulum_jacobian(u,t)
        elif self.name=="SIR":
            return SIR_jacobian(u,t)
        elif self.name=="nonLinearOscillator":
            return nonLinearOscillator_jacobian(u,t,self.alpha)
        elif self.name=="nonLinearOscillatorDamped":
            return nonLinearOscillator_jacobian(u,t,self.alpha)
        elif self.name=="Robertson":
            return Robertson_jacobian(u,t)
        elif self.name=="lotka":
            return lotka_jacobian(u,t)
        else:
            raise ValueError("Jacobian not defined for this problem")

    def exact(self,u,t):
        if self.name=="linear_scalar":
            return linear_scalar_exact_solution(u,t,self.k_coef)
        elif self.name=="nonlinear_scalar":
            return nonlinear_scalar_exact_solution(u,t,self.k_coef)
        elif self.name=="linear_system2":
            return linear_system2_exact_solution(u,t)
        elif self.name=="linear_system3":
            return linear_system3_exact_solution(u,t)
        elif self.name=="linear_system3_speeds":
            return linear_system3_speeds_exact_solution(u,t)
        elif self.name=="nonLinearOscillator":
            return nonLinearOscillator_exact_solution(u,t,self.alpha)
        elif self.name=="nonLinearOscillatorDamped":
            return nonLinearOscillator_exact_solution(u,t,self.alpha)
        elif self.name=="vibratingDamped":
            return vibratingDamped_exact_solution(u,t,self.m_coef,self.r_coef, self.k_coef, self.f_coef, self.omega_coef, self.phi_coef)
        else:
            raise ValueError("Exact solution not defined for this problem")
            
    def exact_solution_times(self,u0,tt):
        exact_solution=np.zeros((len(u0),len(tt)))
        for it, t in enumerate(tt):
            exact_solution[:,it]=self.exact(u0,t)
        return exact_solution

    def prod_dest(self,u,t=0):
        if self.name=="linear_system2":
            return linear_system2_production_destruction(u,t)
        if self.name=="nonlinear_system3":
            return nonlinear_system3_production_destruction(u,t)
        elif self.name=="Robertson":
            return Robertson_production_destruction(u,t)
        elif self.name=="SIR":
            return SIR_production_destruction(u,t)
        else:
            raise ValueError("Prod Dest not defined for this problem")

    def entropy(self,u,t=0):
        if self.name =="pendulum":
            return pendulum_entropy(u,t)
        elif self.name == "lotka":
            return lotka_entropy(u,t=t)
        elif self.name in ["nonLinearOscillator","nonLinearOscillatorDamped", "linear_system2"]:
            return square_entropy(u)
        else:
            raise ValueError("Entropy not defined for this problem")
    
    def entropy_variable(self,u,t=0):
        if self.name =="pendulum":
            return pendulum_entropy_variables(u,t)
        elif self.name == "lotka":
            return lotka_entropy_variables(u,t=t)
        elif self.name in ["nonLinearOscillator","nonLinearOscillatorDamped", "linear_system2"]:
            return square_entropy_variable(u)
        else:
            raise ValueError("Entropy variable not defined for this problem")

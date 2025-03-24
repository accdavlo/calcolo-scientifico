import numpy as np
import matplotlib.pyplot as plt
from solvers import *

class ConvergenceAnalysis:
    def __init__(self, problem, Ns=None):
        self.problem = problem
        if Ns is None:
            self.Ns = np.int64(2**np.linspace(3,10,8))
        else:
            self.Ns = Ns
        self.Ns = np.array(self.Ns)
    
    def analyse(self):
        self.errors = np.zeros(len(self.Ns))
        self.orders = np.zeros(len(self.Ns)-1)
        
        for iN, N in enumerate(self.Ns):
            _,_,self.errors[iN] =self.problem.solve(N)
            if iN>0:
                self.orders[iN-1] = np.log(self.errors[iN]/self.errors[iN-1])/np.log(self.Ns[iN-1]/self.Ns[iN])
            
    def plot_error_convergence(self):
        if not hasattr(self,"errors"):
            self.analyse()
        fig, ax = plt.subplots(1,1)
        ax.loglog(self.Ns, self.errors, label ="errors")
        average_order = np.mean(self.orders)
        order_plus = np.ceil(average_order)
        order_minus = np.floor(average_order)
        ax.loglog(self.Ns, (self.Ns/self.Ns[0])**(-order_plus)*self.errors[0],"--", label =f"order {order_plus}")
        ax.loglog(self.Ns, (self.Ns/self.Ns[0])**(-order_minus)*self.errors[0],"--", label =f"order {order_minus}")
        ax.set_xlabel("Number of points in mesh")
        ax.set_ylabel("Relative error")
        plt.legend()
        
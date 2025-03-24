import numpy as np

class Geometry1D:
    def __init__(self, x_left, x_right, N=None):
        self.x_left = x_left
        self.x_right = x_right
        if N is not None:
            self.set_N(N)
    def set_linspace(self, xx):
        self.xx = xx
        self.x_left = self.xx[0]
        self.x_right = self.xx[-1]
        self.N = len(self.xx)
    
    def set_N(self,N):
        self.N = N
        self.xx = np.linspace(self.x_left,self.x_right, N)
        self.dx = self.xx[1]-self.xx[0]
     
     
class Geometry2D:
    def __init__(self, x_left, x_right, y_bottom, y_top, Nx=None, Ny=None):
        self.x_left = x_left
        self.x_right = x_right
        self.y_bottom = y_bottom
        self.y_top = y_top
        if Nx is not None and Ny is not None:
            self.set_Ns(Nx,Ny)
        elif Nx is not None:
            self.set_Ns(Nx,Nx)
            
    def set_Ns(self,Nx,Ny):
        self.Nx = Nx
        self.Ny = Ny
        self.xx = np.linspace(self.x_left,self.x_right, self.Nx)
        self.yy = np.linspace(self.y_bottom,self.y_top, self.Ny)
        self.dx = self.xx[1]-self.xx[0]
        self.dy = self.yy[1]-self.yy[0]

        self.XX, self.YY = np.meshgrid(self.xx, self.yy, indexing="ij")

    def map_1D_to_2D(self, alpha):
        return alpha%self.Nx, alpha//self.Nx
    def map_2D_to_1D(self, i,j):
        return i*self.Ny+j
import numpy as np
import scipy.sparse as sp
from geometry import *

class Poisson_Finite_Difference_1D:
    def __init__(self, geometry, boundary, f_lambda):
        self.geometry = geometry
        self.boundary = boundary
        self.f_lambda = f_lambda

    def set_exact_solution(self, uex_lambda):
        self.uex_lambda = uex_lambda
    def assemble_matrix(self):
        Nx = self.geometry.N
        dx = self.geometry.dx
        self.A = np.zeros((Nx,Nx))
        self.f = np.zeros(Nx)

        for i in range(1,Nx-1):
            self.A[i,i-1] = -1./dx**2
            self.A[i,i]   =  2./dx**2
            self.A[i,i+1] = -1./dx**2
            self.f[i]     = self.f_lambda(self.geometry.xx[i])
            
        self.apply_BC()
    
    def apply_BC(self, boundary=None):
        # Boundary conditions
        
        if boundary is not None:
            self.boundary = boundary
        if not hasattr(self,"boundary"):
            raise ValueError("Boundaries are not set yet")
        
        if self.boundary["left"][0]=="dirichlet":
            # Homogeneous Dirichlet in x_left
            self.A[0,:] = 0.
            self.A[0,0] = 1.
            self.f[0]   = self.boundary["left"][1]
        elif self.boundary["left"][0]=="neumann":
            # Homogeneous Dirichlet in x_left
            self.A[0,:] = 0.
            self.A[0,0] = -1./self.geometry.dx
            self.A[0,1] =  1./self.geometry.dx
            self.f[0]   = self.boundary["left"][1]
        else:
            raise ValueError("Boundary %s not implemented"%(self.boundary["left"][0]))
            
        if self.boundary["right"][0]=="dirichlet":
            # Homogeneous Dirichlet in x_right
            self.A[-1,:] = 0.
            self.A[-1,-1] = 1.
            self.f[-1]   = self.boundary["right"][1]
        elif self.boundary["right"][0]=="neumann":
            # Homogeneous Dirichlet in x_right
            self.A[-1,:] = 0.
            # First order
            self.A[-1,-2] = -1./self.geometry.dx
            self.A[-1,-1] =  1./self.geometry.dx
            
            # # Second order
            # self.A[-1,-3] = 1./2./self.geometry.dx
            # self.A[-1,-2] = -2./self.geometry.dx
            # self.A[-1,-1] =  3./2./self.geometry.dx
            
            self.f[-1]   = self.boundary["right"][1]

    def solve(self, N=None):
        if N is not None:
            self.geometry.set_N(N)
            self.assemble_matrix()
        if not hasattr(self,"A") or not hasattr(self,"f"):
            self.assemble_matrix()
        self.uu = np.linalg.solve(self.A, self.f)
        if hasattr(self,"uex_lambda"):
            uex = self.uex_lambda(self.geometry.xx)
            self.error = np.linalg.norm(self.uu-uex)/np.linalg.norm(uex)
        else:
            self.error = np.nan
        return self.geometry, self.uu, self.error


class Poisson_FiniteDifference_2D:
    def __init__(self, geometry, boundary, f_lambda):
        self.geometry = geometry
        self.boundary = boundary
        self.f_lambda = f_lambda

    def set_exact_solution(self, uex_lambda):
        self.uex_lambda = uex_lambda
    def assemble_matrix(self):
        Nx = self.geometry.Nx
        Ny = self.geometry.Ny
        self.N = Nx*Ny
        dx = self.geometry.dx
        dy = self.geometry.dy

        self.f = np.zeros(self.N)

        main_diag = np.ones(self.N)*(2/dx**2+2/dy**2)
        off_diag_x = np.ones(self.N-Ny)*(-1/dx**2)
        off_diag_y = np.ones(self.N-1)*(-1/dy**2)

        self.A = sp.diags([main_diag, off_diag_x, off_diag_x, off_diag_y, off_diag_y],\
                           [0, -Ny, Ny, -1, 1], shape=(self.N,self.N), format="csr")

        # for i in range(1,Nx-1):
        #     for j in range(1,Ny-1):
        #         alpha = geom2D.map_2D_to_1D(i,j)
                
        #         self.A[alpha,alpha-Ny] =  -1./dx**2
        #         self.A[alpha,alpha  ]+=   2./dx**2
        #         self.A[alpha,alpha+Ny] =  -1./dx**2
        #         self.A[alpha,alpha-1] =  -1./dy**2
        #         self.A[alpha,alpha   ]+=   2./dy**2
        #         self.A[alpha,alpha+1] =  -1./dy**2
        #         self.f[alpha]     = self.f_lambda(np.array([self.geometry.XX[i,j],self.geometry.YY[i,j]]))

        self.f = self.f_lambda(np.array([self.geometry.XX.reshape(-1),self.geometry.YY.reshape(-1)]))

        self.apply_BC()
    
    def apply_BC(self, boundary=None):
        # Boundary conditions
        
        if boundary is not None:
            self.boundary = boundary
        if not hasattr(self,"boundary"):
            raise ValueError("Boundaries are not set yet")
        
        if self.boundary["left"][0]=="dirichlet":
            # Dirichlet in x_left
            for j in range(self.geometry.Ny):
                alpha = self.geometry.map_2D_to_1D(0,j)
                put_zero_row_in_csr(self.A,alpha)
                self.A[alpha,alpha] = 1.
                self.f[alpha] = self.boundary["left"][1](np.array([self.geometry.XX[0,j],self.geometry.YY[0,j]]))

        elif self.boundary["left"][0]=="neumann":
            # Neumann in x_left
            for j in range(self.geometry.Ny):
                alpha = self.geometry.map_2D_to_1D(0,j)
                alpha1= self.geometry.map_2D_to_1D(1,j)
                put_zero_row_in_csr(self.A,alpha)
                self.A[alpha,alpha] = -1./self.geometry.dx
                self.A[alpha,alpha1] = 1./self.geometry.dx
                self.f[alpha] = self.boundary["left"][1](np.array([self.geometry.XX[0,j],self.geometry.YY[0,j]]))
        else:
            raise ValueError("Boundary %s not implemented"%(self.boundary["left"][0]))
            
        if self.boundary["right"][0]=="dirichlet":
            # Dirichlet in x_right
            for j in range(self.geometry.Ny):
                alpha = self.geometry.map_2D_to_1D(self.geometry.Nx-1,j)
                put_zero_row_in_csr(self.A,alpha)
                self.A[alpha,alpha] = 1.
                self.f[alpha] = self.boundary["right"][1](np.array([self.geometry.XX[self.geometry.Nx-1,j],self.geometry.YY[self.geometry.Nx-1,j]]))
        elif self.boundary["right"][0]=="neumann":
            # Neumann in x_right
            for j in range(self.geometry.Ny):
                alpha = self.geometry.map_2D_to_1D(self.geometry.Nx-1,j)
                alpha1= self.geometry.map_2D_to_1D(self.geometry.Nx-2,j)
                put_zero_row_in_csr(self.A,alpha)
                self.A[alpha,alpha] =   1./self.geometry.dy
                self.A[alpha,alpha1] = -1./self.geometry.dy
                self.f[alpha] = self.boundary["right"][1](np.array([self.geometry.XX[self.geometry.Nx-1,j],self.geometry.YY[self.geometry.Nx-1,j]]))
        else:
            raise ValueError("Boundary %s not implemented"%(self.boundary["right"][0]))

        if self.boundary["top"][0]=="dirichlet":
            # Dirichlet in y_top
            for i in range(self.geometry.Nx):
                alpha = self.geometry.map_2D_to_1D(i,self.geometry.Ny-1)
                put_zero_row_in_csr(self.A,alpha)
                self.A[alpha,alpha] = 1.
                self.f[alpha] = self.boundary["top"][1](np.array([self.geometry.XX[i,self.geometry.Ny-1],self.geometry.YY[i,self.geometry.Ny-1]]))
        elif self.boundary["top"][0]=="neumann":
            # Neumann in y_top
            for i in range(self.geometry.Nx):
                alpha = self.geometry.map_2D_to_1D(i,self.geometry.Ny-1)
                alpha1= self.geometry.map_2D_to_1D(i,self.geometry.Ny-2)
                put_zero_row_in_csr(self.A,alpha)
                self.A[alpha,alpha] =   1./self.geometry.dy
                self.A[alpha,alpha1] = -1./self.geometry.dy
                self.f[alpha] = self.boundary["top"][1](np.array([self.geometry.XX[i,self.geometry.Ny-1],self.geometry.YY[i,self.geometry.Ny-1]]))
        else:
            raise ValueError("Boundary %s not implemented"%(self.boundary["top"][0]))

        if self.boundary["bottom"][0]=="dirichlet":
            # Dirichlet in y_bottom
            for i in range(self.geometry.Nx):
                alpha = self.geometry.map_2D_to_1D(i,0)
                put_zero_row_in_csr(self.A,alpha)
                self.A[alpha,alpha] = 1.
                self.f[alpha] = self.boundary["bottom"][1](np.array([self.geometry.XX[i,0],self.geometry.YY[i,0]]))
        elif self.boundary["bottom"][0]=="neumann":
            # Neumann in y_bottom
            for i in range(self.geometry.Nx):
                alpha = self.geometry.map_2D_to_1D(i,0)
                alpha1= self.geometry.map_2D_to_1D(i,1)
                put_zero_row_in_csr(self.A,alpha)
                self.A[alpha,alpha] = -1./self.geometry.dy
                self.A[alpha,alpha1] = 1./self.geometry.dy
                self.f[alpha] = self.boundary["bottom"][1](np.array([self.geometry.XX[i,0],self.geometry.YY[i,0]]))
        else:
            raise ValueError("Boundary %s not implemented"%(self.boundary["bottom"][0]))

    def solve(self, Nx=None, Ny=None):
        if Nx is not None:
            if Ny is None:
                Ny = Nx
            self.geometry.set_Ns(Nx,Ny)
            self.assemble_matrix()
        if not hasattr(self,"A") or not hasattr(self,"f"):
            self.assemble_matrix()
        self.uu = sp.linalg.spsolve(self.A, self.f)
        if hasattr(self,"uex_lambda"):
            self.uex = self.uex_lambda(np.array([self.geometry.XX.reshape(-1),self.geometry.YY.reshape(-1)]))
            self.error = np.linalg.norm(self.uu-self.uex)/np.linalg.norm(self.uex)
        else:
            self.error = np.nan
        return self.geometry, self.uu, self.error
    

def put_zero_row_in_csr(A, i):
    A.data[A.indptr[i]:A.indptr[i+1]] = 0

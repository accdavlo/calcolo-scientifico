1. Intro to PDE
    1. Intro
    1. PDE
        * Classification: stationary, unsteady, linear, nonlinear, quasi-linear, semi-linear, examples
        * First order linear, characteristics, general coefficients
        * Second order linear, classification, invariant by change of variables
        * Hyperbolic canonical form
        * Parabolic and elliptic canonical
        * Cauchy problem
        * Well-posedness
        * Theorem of existence and uniqueness (Cauchy Kovalesvskaya)
    1. Functional analysis
        * Linear, bilinear forms, dual space, Hilbert spaces, Riesz representative
        * Distributions
        * Convergence in D(\Omega)
        * Dirac delta
        * L2
        * Distributional derivatives
        * Sobolev spaces
        * Norms, seminorms in Sobolev spaces
        * Boundaries
        * Poincarè inequality
1. Elliptic
    1. Elliptic PDE
        * Poisson, physical derivation
        * BOundary conditions
        * Regularity of the solution
        * Weak formulation
        * Variational form
        * BC in Weak form
        * Weak in 2D
        * Lax-Milgram: existence and uniqueness of solution to a=F and boundness of the solution        
    1. FD for elliptic
        * Divided differences
        * Order with taylor
        * Higher derivatives recipes
        * Poisson 1D with FD
        * BC
        * Discrete maximum principle for 2nd order
        * A priori error estimation
        * existence and uniqueness (Sketch)
    1. FEM for elliptic
        * Variational discrete form
        * Basis functions
        * Poisson A in FEM is positive definite
        * Existence and uniqueness (from Lax-Milgram)
        * Stability
        * Convergence (Orthogonality + Céa's Lemma + Order)
        * FEM 1D piece-wise linear/polynomials
        * Reference element, assembly
        * Error estimation with polynomials
        * BC
        * 2D geometry
        * 2D meshes
        * Basis on triangle
        * Assembly
        * Error estimates
1. Other PDEs
    1. Parabolic
        * Heat equation
        * Exact solution
        * Fourier series
        * Finite Difference for heat with implicit, explicit euler and Crank-Nicolson
        * Consistency error
        * Method of lines, semidiscretization, stability region split
        * Eigenvalues of spatial discretization
        * Convergence: Lax-Richtmyer stability, Lax equivalence theorem
        * Von Neumann stability vs ODE stability region
        * Weak formulation of heat and FEM
    1. Transport
        * Conservation laws, integral form
        * Transport
        * Euler/Navier Stokes
        * Linear advection equation
        * Variable velocity linear advection (characteristics) (conservative and non-conservative form)
        * Weak formulation
        * Energy stability
        * Vanishing viscosity solution
        * Finite difference
            * Central + explicit euler + von Neumann
            * Central + implicit euler + von Neumann
            * Lax-Friedrichs + von Neumann
            * CFL
            * Upwind
            * Consistency of LxF and upwind
            * Lax-Wendroff + von Neumann
            * Beam-Warming
            * BC (ghosts)
    1. Non linear hyperbolic
        * Nonlinear conservation laws
        * Burgers (inviscid and viscous)
        * Exact solution for viscous
        * Breaking point
        * Weak solution
        * Riemann problem
        * Shock
        * Rankine-Hugoniot
        * Dependence on conserved variable
        * Rarefaction wave
        * Non-uniqueness of weak solution
        * Vanishing-viscosity to entropy solution
        * Existence and uniqueness of weak entropy solution
        * Finite volume
            * Godunov method
            * Numerical fluxes (Rusanov, Lax-Friedrichs, linearized Roe)
1. PINN 

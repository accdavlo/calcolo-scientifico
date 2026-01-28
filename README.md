# Calcolo Scientifico
Repository for the course Calcolo Scientifico for Scienze Matematiche per l'Intelligenza Artificiale A.A. 2025/2026

### OPIS code

## Useful links
* [Course page on Sapienza Website](https://corsidilaurea.uniroma1.it/it/view-course-details/2024/31778/20220331104432/3b541170-a744-497b-8354-6947c3438fe3/f4687f41-3295-4d30-b113-0c147078c2ab/d522d305-a6c6-4020-ab5e-d760222a4ab5/bcac70c7-281d-4ab1-ba19-85d9792bc311?guid_cv=f4687f41-3295-4d30-b113-0c147078c2ab&current_erogata=3b541170-a744-497b-8354-6947c3438fe3)


## Logbook, Notes and Recordings
| Date | Topics  | Notes | Recording link | Password |
|:-----|:------|:---------------|:------|:------|
|03/03/26| Introduction to the course, derivatives notation| | | |
|04/03/26| Classification of PDEs, first order linear PDEs |  |  | |
|10/03/26| Canonical form of first order linear PDE, classification of second order linear PDEs, Cauchy Problem | See above | |
|11/03/26| Cauchy-Kovaleskaya, well posedness, functional spaces, linear functional, bilinear functionals, Hilbert spaces, distributions |  | |
|17/03/26| Derivatives of distributions, Sobolev spaces, Poincare, intro to elliptic |   | | |
|18/03/26| Weak formulation of elliptic problems, Lax-Milgram |  |  |  |
|24/03/26| Divided differences, finite differences for 1D poisson, error analysis |  | |
|25/03/26| Coding finite difference 1D for Poisson | [Notebook](/codes/poisson_FD.ipynb)   |  |   |
|31/03/26| Coding finite difference 2D for Poisson |  [Notebook](/codes/poisson_FD.ipynb)| |  |
|01/04/26| Finite Element in 1D for Poisson |  | | |
|14/04/26| Finite Element in 1D for Poisson | See above | |
|15/04/26| Coding Finite Element 1D for Poisson |  [Notebook](/codes/poisson_FEM.ipynb) |  | |
|21/04/26| Finite element for multi-D |  | | |
|22/04/26| Coding finite element 2D for Poisson with FEniCS |   [Notebook](/codes/FEM_with_FEniCS.ipynb) |  |
|28/04/26| Model order reduction |  [Notebook](/codes/ROM_with_FEniCS.ipynb) |  |
|29/04/26| Parabolic equations  |  |  | |
|12/05/26| FD and FEM for parabolic equations |  | | |
|13/05/26| Advection equation |  |  | |
|19/05/26| FD for advection equation  |  | | |
|20/05/26| Coding FD for advection and nonlinear laws | [Notebook](/codes/transport_FD.ipynb)  |  | |
|26/05/26| Scalar hyperbolic conservation laws (nonlinear) |  | | |
|27/05/26| Coding hyperbolic conservation laws |   |  | |
|03/06/26| Physics Informed Neural Networks |  |  | |
|10/06/26| Projects presentation


## Slides

|Number |Topic| PDF slides | HTML slides | Markdown slides |
|:-----|:------|:---------|:-----------|:-----------|
| 1| Introduction | | | |
| 1.0| Introduction to the course| [PDF](lectures/01/010_intro.pdf?raw=true)| [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/01/010_intro.html) | [md](lectures/01/010_intro.md) |
| 1.1 | Introduction to `git`(hub)| [PDF](lectures/00/004_git.pdf?raw=true)| [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/00/004_git.html) | [md](lectures/00/004_git.md) |
| 1.2 | Introduction to PDEs| [PDF](lectures/01/011_PDE.pdf?raw=true)| [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/01/011_PDE.html) | [md](lectures/01/011_PDE.md) |
| 1.3 | Introduction to functional analysis| [PDF](lectures/01/012_functional_analysis.pdf?raw=true)| [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/01/012_functional_analysis.html) | [md](lectures/01/012_functional_analysis.md) |
| 2 | Elliptic problems ||||
| 2.1 | Elliptic problems| [PDF](lectures/02/020_elliptic.pdf?raw=true)| [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/02/020_elliptic.html) | [md](lectures/02/020_elliptic.md) |
| 2.2 | Finite differences for elliptic problems| [PDF](lectures/02/021_finite_difference_elliptic.pdf?raw=true)| [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/02/021_finite_difference_elliptic.html) | [md](lectures/02/021_finite_difference_elliptic.md) |
| 2.3 | Finite elements for elliptic problems| [PDF](lectures/02/022_finite_element_elliptic.pdf?raw=true)| [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/02/022_finite_element_elliptic.html) | [md](lectures/02/022_finite_element_elliptic.md) |
| 2.4 | Reduced order methods for elliptic problems |[Notebook](/codes/ROM_with_FEniCS.ipynb) | | | |
| 3 | Parabolic problems ||||
| 3.1 | Parabolic problems and their discretization| [PDF](lectures/03/030_parabolic.pdf?raw=true)| [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/03/030_parabolic.html) | [md](lectures/03/030_parabolic.md) |
| 4 | Hyperbolic equations||||
| 4.1 | Linear Transport equation problems and finite difference| [PDF](lectures/03/031_transport.pdf?raw=true)| [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/03/031_transport.html) | [md](lectures/03/031_transport.md) |
| 4.2 | Nonlinear conservation laws | [PDF](lectures/03/032_non_linear_hyperbolic.pdf?raw=true)| [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/03/032_non_linear_hyperbolic.html) | [md](lectures/03/032_non_linear_hyperbolic.md) |
| 5 | PINN| [PDF](lectures/04/040_PINN.pdf?raw=true)| [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/04/040_PINN.html) | [md](lectures/04/040_PINN.md) |

## Notebooks
| Date | Topic | Notebook |Solutions   |  Last save | 
|:-----|:------|:---------|:-----------|:-----------|
|26/03/25| Finite difference for Poisson | [Notebook](/codes/poisson_FD.ipynb) | [Solutions](/codes/solutions/poisson_FD.ipynb)|
|04/04/25| Finite element 1D for Poisson | [Notebook](/codes/poisson_FEM.ipynb) | [Solutions](/codes/solutions/poisson_FEM.ipynb)| |
|11/04/25| Finite element 2D for Poisson with FEniCS| [Notebook](/codes/FEM_with_FEniCS.ipynb) |[Solutions](/codes/solutions/FEM_with_FEniCS.ipynb)|
|23/04/25| Reduced order models for parametric problems with FEniCS| [Notebook](/codes/ROM_with_FEniCS.ipynb) |-|
|02/05/25| Finite difference for Heat equation | [Notebook](/codes/heat_FD.ipynb) | [Solutions](/codes/solutions/heat_FD.ipynb)|
|14/05/25| Finite difference for transport equation | [Notebook](/codes/transport_FD.ipynb) | [Solutions](/codes/solutions/transport_FD.ipynb)|
|21/05/25| Finite volume for conservation laws | [Notebook](/codes/hyperbolic_FD.ipynb) | [Solutions](/codes/solutions/hyperbolic_FD.ipynb)|
|23/05/25| PINN | [Notebook](/codes/PINN.ipynb) | [Solutions](/codes/solutions/PINN.ipynb)|


## Projects ideas (contact me for more details)
1. Finite element with naive basis functions (e.g. trigonometric functions) (in 1D/2D)
1. Spectral element method (Chapter of Quarteroni)
1. Navier-Stokes with FEniCS on a complex geometry (Chapter of Quarteroni)
1. Reduced basis for elastic block [Problem from this RBniCS test](https://colab.research.google.com/github/RBniCS/RBniCS/blob/open-in-colab/tutorials/02_elastic_block/tutorial_elastic_block.ipynb)
1. ~~Error control for reduced order models (a posteriori error estimator) (Hesthaven book)~~
1. SUPG for advection-diffusion time dependent problem (1D or 2D with FEniCS), with energy stability analysis (Chapter of Quarteroni)
1. Von Neumann stability analysis for a Finite Difference discretization of the wave equation
1. Von Neumann stability analysis for FEM $\mathbb P^p$ for parabolic equations
1. Wave equations in 2D (with compatible Finite Difference discretization)
1. High order FD discretization of Burgers' equations in 1D with WENO
1. Hyperbolic system of conservation laws (Euler equations) in 1D with finite difference methods
1. 2D Euler equations solved on a Cartesian grid for a DMR test
1. Comparison of PINN with classical solvers (for various problems)

## Literature
* Quarteroni, Alfio. Modellistica Numerica per Problemi Differenziali. Springer Science & Business Media, 2016. [Intro alle PDE, Metodi agli elementi finiti, Metodi alle differenze finite, Riduzione del Modello]
* Evans, Lawrence C. Partial differential equations. Vol. 19. American Mathematical Society, 2010. [Introduzione alle PDE]
* LeVeque, Randall J. Finite difference methods for ordinary and partial differential equations: steady-state and time-dependent problems. Society for Industrial and Applied Mathematics, 2007. [Metodi alle differenze finite]
* LeVeque, Randall J. Finite volume methods for hyperbolic problems. Vol. 31. Cambridge university press, 2002. [Metodi ai volumi finiti]
* Langtangen, Hans Petter, and Anders Logg. Solving PDEs in python: the FEniCS tutorial I. Springer Nature, 2017. [Manuale per usare FEniCS]
* Hesthaven, J., Rozza G. and Stamm B. Certified Reduced Basis Methods for Parametrized Partial Differential Equations. Springer, 2016. [Riduzione del Modello] [https://link.springer.com/book/10.1007/978-3-319-22470-1](https://link.springer.com/book/10.1007/978-3-319-22470-1)

# Program
The course studies partial differential equations (PDEs) and some numerical methods for approximating their solutions.

The course is divided into:
- review of ODEs [2h];
- introduction to PDEs [6h];
- finite difference methods [8h = 4h classes + 4h lab];
- finite element methods [18h = 12h classes + 6h lab];
- finite volume methods [10h = 7h classes + 3h lab];
- physics informed neural networks [2h = 1h class + 1h lab];
- model order reduction [2h = 1h class + 1h lab].

At first, we will introduce PDEs with some examples from various physical problems, the concept of weak derivatives and Sobolev spaces. For some classes of PDEs, we will verify the existence, uniqueness and/or regularity of PDEs' solution (transport equation, Poisson equation, heat equation, Stokes problem for incompressible fluids, conservation laws, Burgers equations, Euler for fluid dynamics).

We will see different types of discretization of PDEs starting from finite differences (FD). We will define finite difference discretization, their consistency, their accuracy, and we will apply it to 1D, 2D, time-independent, and time-dependent problems. We will see how to implement and solve these problems in Python by defining sparse matrix structures. We will study the stability of these methods and derive the CFL conditions.

Subsequently, we will study finite element methods (FEM) starting from the definition of the approximation spaces and their properties, the quadratures and a priori estimates for some problems. We will study the convergence of methods for coercive linear problems and for linear problems in saddle point formulations. Finally, we will see the onset of instabilities due to advection-dominated problems and some stabilization techniques. We will implement finite elements for 1D and 2D problems. Moreover, we will use the FEniCS library for problems with more complicated geometries.

Then, we will study the finite volume method for conservation laws, introducing the discretization and the concept of consistency for numerical fluxes. We will study the stability of the method and see different types of reconstructions and numerical fluxes. Moreover, we will implement the method on nonlinear problems.

The final classes will be devoted to less standard methods as physics informed neural networks and model order reduction techniques for parametrised PDEs.

## Tools
- [git](https://git-scm.com/) ([github](https://github.com))
- [python](https://www.python.org/)
- [FEniCS](https://fenicsproject.org/) Finite Element python library
- [PINA](https://mathlab.github.io/PINA/) Physics Informed Neural Network library based on PyTorch 

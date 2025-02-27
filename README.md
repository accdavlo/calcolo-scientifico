# Calcolo Scientifico
Repository for the course Calcolo Scientifico for Scienze Matematiche per l'Intelligenza Artificiale

## Useful links
* [Course page on Sapienza Website](https://corsidilaurea.uniroma1.it/it/view-course-details/2024/31778/20220331104432/3b541170-a744-497b-8354-6947c3438fe3/f4687f41-3295-4d30-b113-0c147078c2ab/d522d305-a6c6-4020-ab5e-d760222a4ab5/bcac70c7-281d-4ab1-ba19-85d9792bc311?guid_cv=f4687f41-3295-4d30-b113-0c147078c2ab&current_erogata=3b541170-a744-497b-8354-6947c3438fe3)
* [Recursive Zoom Link for classes](https://uniroma1.zoom.us/j/84367160394?pwd=0dqEUWrQYECMEy6h8Jk5RNnJ5KRFp8.1)

## Logbook, Notes and Recordings
| Date | Topics  | Notes | Recording link | Password |
|:-----|:------|:---------------|:------|:------|
|26/02/25| Introduction to the course, derivatives notation, ODE existence and uniqueness| [Notes](/notes/2025-02-26-Notes.pdf)| [Recording](https://uniroma1.zoom.us/rec/share/S6oSkizEydLBuid6I77BZo0rqpL6orAh0-da0559uM31wNzJBIB_EbUUytpY3IW_.QSjCBG2ap0n4nMH2)| yL6wR@#D |
|28/02/25| Explicit and implicit Euler for ODEs, classification of nonlinear PDEs, general solution for first order PDE| Notes| Recording |

## Next Lessons Schedule
* 28/02/25 16:00-18:00 Friday
* 28/02/25 16:00-18:00 Friday



## Notes

1. Introduction
    1. Introduction to the course [PDF](lectures/01/010_intro.pdf) [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/01/010_intro.html) [md](lectures/01/010_intro.md)
    1. Introduction to PDEs [PDF](lectures/01/011_PDE.pdf) [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/01/011_PDE.html) [md](lectures/01/011_PDE.md)
    1. Introduction to functional analysis [PDF](lectures/01/012_functional_analysis.pdf) [html](https://html-preview.github.io/?url=https://github.com/accdavlo/calcolo-scientifico/blob/main/lectures/01/012_functional_analysis.html) [md](lectures/01/012_functional_analysis.md)

## Literature
* Quarteroni, Alfio. Modellistica Numerica per Problemi Differenziali. Springer Science & Business Media, 2016. [Intro alle PDE, Metodi agli elementi finiti, Metodi alle differenze finite, Riduzione del Modello]
* Evans, Lawrence C. Partial differential equations. Vol. 19. American Mathematical Society, 2010. [Introduzione alle PDE]
* LeVeque, Randall J. Finite difference methods for ordinary and partial differential equations: steady-state and time-dependent problems. Society for Industrial and Applied Mathematics, 2007. [Metodi alle differenze finite]
* LeVeque, Randall J. Finite volume methods for hyperbolic problems. Vol. 31. Cambridge university press, 2002. [Metodi ai volumi finiti]
* Langtangen, Hans Petter, and Anders Logg. Solving PDEs in python: the FEniCS tutorial I. Springer Nature, 2017. [Manuale per usare FEniCS]

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

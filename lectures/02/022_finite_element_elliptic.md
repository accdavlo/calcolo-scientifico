---
marp: true
math: mathjax
---
<!--
title: Lecture 022 Finite Elements Elliptic
paginate: true
_class: titlepage
-->

# Finite Element Method for Elliptic Differential Equations



---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>


## Pro and cons of the Finite Differences methods

### Pro
* Easy to setup
* Simple implementation
* Easy high order stencils
* Easy truncation error analysis with Taylor expansion

### Cons
* Difficult to generlize to more complex geometries
* Difficult to deal with boundaries + high order
* No general analysis of stability, existence, uniqueness


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Can we write a discrete formulation of the type $a(u,v)=F(v)\,\forall v \in V$?
Goals:
1. find a discrete Hilbert space $V_h\subset V\subset H^1(\Omega)$
2. find a discrete bilinear form $a_h(\cdot,\cdot):V_h\times V_h\to \mathbb R$ continuous and coercive that approximates $a$
3. find a discrete linear form $F_h:V_h\to \mathbb R$ bounded that approximates $F$.

$h>0$ is a parameter that describes the discretization scale of the discrete space (e.g. the minimum of the $\Delta x$ in the mesh).

So, let's suppose that we have $V_h\subset V$ : $\text{dim} (V_h) = N_h<\infty \, \forall h>0$. 
Now, we can simply take $a_h$ as the restriction of $a$ on $V_h$ and $F_h$ as the restriction on $V_h$ as well. This means that we can simply look for a solution $u_h\in V_h$ such that for every $v_h\in V_h$
$$
a(u_h,v_h)=F(v_h).
$$
This is called **Galerkin problem**. 

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>


## Let's move to a basis of $V_h$

Let's consider a basis for $V_h$ given by $\lbrace \varphi_i \rbrace_{j=1}^{N_h}$, since we are talking about linear and bilinear operators, we can instead look for the approximation $u_h\in V_h$ such that
$$
a(u_h,\varphi_i) = F(\varphi_i),\qquad \forall i=1,\dots, N_h.
$$
Moreover, also $u_h(x)=\sum_{j=1}^{N_h} u_j \varphi_j(x),$ we have
$$
\sum_{j=1}^{N_h} a(\varphi_j,\varphi_i) u_j = F(\varphi_i),\qquad \forall i=1,\dots, N_h.
$$

We can denote with $A$ the *stiffness* matrix and with $\mathbf{f}\in\mathbb R^{N_h}$ the right-hand-side vector defined as 
$$
a_{ij} = a(\varphi_j,\varphi_i),\qquad f_i = F(\varphi_i).
$$

The Galerkin problem can be written as a linear system for the vector $\mathbf{u}\in \mathbb R^{N_h}$
$$
A \mathbf{u} = \mathbf{f}.
$$


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## $A$ is positive definite
$A$ associated to the elliptic problem $a(u,v)=F(v)\, \forall v\in V$ where $a(\cdot,\cdot)$ is bilinear and coercive, then $A$ is positive definite.
### Proof
Recall that $B$ is positive definite if $\mathbf{v}^\top B \mathbf{v} \geq 0 \forall \mathbf{v} \in \mathbb R^n$ and $\mathbf{v}^\top B \mathbf{v}=0 \Leftrightarrow \mathbf{v}=0.$
$$

$$
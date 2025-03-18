---
marp: true
math: mathjax
---
<!--
title: Lecture 021 Finite Difference Elliptic
paginate: true
_class: titlepage
-->

# Finite Difference for Elliptic Differential Equations



---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

We have seen how the equations are defined. In some cases there are exact solutions, and we have found some. But in many other cases there is no known analytical solution.

Numerical analysis comes in help to find **approximations** of such solutions. 

We start with the simplest approach one can think of: 
## Finite Difference



---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>


## Finite Difference

Consider a boundary value 1D problem on $\Omega=[a,b]$ defined as 
$$F(x,u,\partial_x u , \partial_{x}^2 u,\dots ,\partial^{k}_x u)=0 + BCs.$$

Since the computer represents only discrete states and we want to approximate a function $u$, we can do it on a simple grid:
$$
a=x_0<x_1<\dots<x_i<\dots x_N = b
$$
with values 
$$
u_i\approx u(x_i).
$$

To transform the PDE into a system of $N+1$ equations for our $N+1$ unknown, we have to decide how to deal with the derivatives in a discrete sense.

For simplicity, we will consider regular grids with $x_{i+1}-x_i=h$ for all $i=0,\dots,N-1$.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

Let's start with the first derivative $\partial_x u(x)$!

### Definition: divided difference for first derivative
Let $u:[a,b]\to \mathbb R$ be a bounded function, let $x\in [a,b]$ and $h\in\mathbb R^+$. We define the **forward divided difference** of $f$ in $x$ with spacing $h$ by
$$
\delta_{h,+}u(x) = \frac{u(x+h)-u(x)}{h},
$$
for $x+h\in[a,b]$ and, we define the **backward divided difference** of $f$ in $x$ with spacing $h$ by
$$
\delta_{h,-}u(x) = \frac{u(x)-u(x-h)}{h},
$$
for $x-h\in[a,b]$ and the **central divided difference** of $f$ in $x$ with spacing $h$ by
$$
\delta_{h}u(x) = \frac{u(x+h/2)-u(x-h/2)}{h},
$$
for $x+h/2,x-h/2\in[a,b]$.


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>


### Property
If $u$ is has the left derivative $u'_-(x)$, the right derivative $u'_+(x)$ and the derivative $u'(x)$ in $x$, then
$$\lim_{h\to 0} \delta_{h,-}u(x) = u'_-(x),\qquad \lim_{h\to 0} \delta_{h,+}u(x) = u'_+(x),\qquad \lim_{h\to 0} \delta_{h}u(x) = u'(x).$$

So, given a fixed $h$, we can use these divided differences as approximations of the derivatives. 
* How good are these approximations?
* Which one is preferable?

### Taylor expansion!
Suppose that $u$ is regular enough, let's expand the divided differences in $x$ and see what we get.
$$
\begin{align*}
&\delta_{h,-}u(x) - u'(x) = \frac{u(x)-u(x-h)}{h}-u'(h) = \frac{u(x) - \left(u(x) - h u'(x) +\frac{h^2}2 u''(\xi)  \right)}{h} - u'(x)=\frac{h}{2} u''(\xi)\\
&\lvert\delta_{h,-}u(x) - u'(x) \rvert \leq \frac{h}{2} \max_{\xi\in [a,b] } |u''(\xi)|. 
\end{align*}
$$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Lemma
$$
\begin{align*}
&\lvert\delta_{h,-}u(x) - u'(x) \rvert \leq \frac{h}{2} \max_{\xi\in [a,b] } |u''(\xi)|;\\
&\lvert\delta_{h,+}u(x) - u'(x) \rvert \leq \frac{h}{2} \max_{\xi\in [a,b] } |u''(\xi)|;\\
&\lvert\delta_{h}u(x) - u'(x) \rvert \leq \frac{h^2}{24} \max_{\xi\in [a,b] } |u'''(\xi)|.
\end{align*}
$$

### Proof: exercise

### Errors of divided difference
* Central divided difference has a quadratic error
* Sided divided differences have a linear error

Error-wise central is better, but physics may not be central, time for example flows in one direction, so it's complicated to use values of $u$ in the future (see Explicit Euler), also in space one might have favorite directions (we will see strong transport phenomena).


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Order of accuracy
The order of accuracy of an approximation of a function $f$ describes how the error decreases as the grid spacing or time step decreases. The order of accuracy is determined by the leading term in the error expansion.

### Definition
Let $f_h(x)$ be an approximation of a bounded function $f:[a,b]\to \mathbb R$ in a point $x$ with discretization parameter $h>0$. We say that $f_h(x)$ is convergent if 
$$
\lim_{h\to 0} (f_h(x)-f(x))=0.
$$


We say that $f_h(x)$ converges to $f(x)$ with order $p$ with respect to $h$ if 
$$
|f_h(x) - f(x)| = O( h^p).
$$

* $\delta_{h,-}u$ and $\delta_{h,+}u$ are first order approximations of $\partial_x u$
* $\delta_{h}u$ is a second order approximation of $\partial_x u$
 


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## How to make higher order of accuracy
How can we build higher order accurate approximations of the derivatives? 

Suppose that we want to do a backward approximation of the first derivative, we have seen that using 2 points stencils we would get a first order approximation.
Let's **add** more points to the stencil.

### Example 3-point backward stencil
Let's consider the points $x,x-h,x-2h$ and let's try to approximate at the best the first derivative.
$$
\begin{align*}
f'(x)&\approx a_0 f(x) + a_1 f(x-h) + a_2 f(x-2h) =\\
    &= a_0 f(x) + a_1 \left[ f(x) -h f'(x) + \frac{h^2}{2} f''(x) - \frac{h^3}{6}f'''(x) \right]+ a_2 \left[ f(x) -2h f'(x) + 2h^2 f''(x) - \frac{4h^3}{3}f'''(x) \right]+O(h^4)\\
    &=(a_0+a_1+a_2)f(x) + h(-a_1-2a_2)f'(x) +h^2\left(\frac{a_1}2+2a_2\right)f''(x)+h^3 \left(-\frac{a_1}{6}-\frac{4a_2}{3} \right)+O(h^4). 
\end{align*}
$$
3 unknowns $a_0, a_1, a_2$, let's use the first three equations:
$$
\begin{cases}
    a_0+a_1+a_2=0\\
    h(-a_1-2a_2)=1\\
    h^2\left(\frac{a_1}2+2a_2\right)=0
\end{cases} \Longrightarrow
\begin{cases}
    a_0=\frac32 \frac{1}{h}\\
    a_1=-2\frac{1}{h}\\
    a_2=\frac12 \frac{1}{h}\\
\end{cases}\Longrightarrow \frac{3f(x)-2f(x-h)+f(x-2h)}{2h}\approx f'(x) -\frac13 h^2f'''(x) +O(h^4) 
$$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

### Taylor expansion and linear systems

Generalization: given a sencil of length $p+q+1$ with $p,q \in \mathbb N$, i.e., $x-ph, \dots, x-h, x, x+h, \dots, x+qh$, one has to find $p+q+1$ coefficients and, hence, should impose $p+q+1$ linear constraints. 

In particular, for approximating the first derivative, we aim at getting a $(p+q)$-th order accurate approximation from a $p+q+1$ stencil, because for each new term we add, we can cancel a new term of the Taylor expansion.


$$
f'(x) \approx \frac{1}{h} \left( a_{-p}f(x-ph) +\dots + a_0 f(x) + a_1 f(x+h) +\dots +a_q f(x+qh) \right) = \frac{1}{h} \sum_{\ell = -q}^p a_\ell f(x+\ell h).
$$



---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>


### Central stencils
| Accuracy | -4     | -3     | -2     | -1     | 0      | 1      | 2      | 3      | 4      |
|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 2        |        |        |        | -1/2   | 0      | 1/2    |        |        |        | 
| 4        |        |        | 1/12   | -2/3   | 0      | 2/3    | -1/12  |        |        | 
| 6        |        | -1/60  | 3/20   | -3/4   | 0      | 3/4    | -3/20  | 1/60   |        | 
| 8        | 1/280  | -4/105 | 1/5    | -4/5   | 0      | 4/5    | -1/5   | 4/105  | -1/280 | 
### Backward stencils
| Accuracy | -4     | -3     | -2     | -1     | 0      |
|----------|--------|--------|--------|--------|--------|
| 1        |        |        |        | -1     | 1      |
| 2        |        |        | 1/2    | -2     | 3/2    |
| 3        |        | -1/3   | 3/2    | -3     | 11/6   |
| 4        | 1/4    | -4/3   | 3      | -4     | 25/12  |


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Higher derivatives
How can we approximate higher order derivatives?

### With divided differences

We know how to do the first derivative of a function, we can compute the second derivative by applying two times this operator.

### Example central difference
$$
\begin{align*}
\delta_{h/2} f(x) &= \frac{1}{h} \left( f(x+h/2) -  f(x-h/2)\right) \approx f'(x)\\
\delta^2_h f(x):&= \delta_{h/2} (\delta_{h/2} f)(x) = \frac{1}{h} \delta_h \left(  f(x+h/2) -  f(x-h/2)\right) = \\
&=\frac{1}{h^2} \left( f(x+h)-f(x)  - \left(f(x)-f(x-h)\right)  \right)= \frac{f(x+h)-2f(x)+f(x-h)}{h^2}.
\end{align*}
$$

#### Error with Taylor
$$
\delta^2_hf(x) \approx f''(x) +\frac{h^2}{24}(f^{(4)}(\xi)+f^{(4)}(\zeta)) \Longrightarrow \lvert \delta^2_hf(x) - f''(x)\rvert \leq \frac{h^2}{12}\max_{y\in[x-h,x+h]}|f^{(4)}(y)|
$$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Higher derivative with Taylor expansion

Same as before, we can fix a stencil and check the higher derivatives terms and match them.

$$
\begin{align*}
f^{(k)}(x) & \approx \frac{1}{h^k} \left( a_{-p} f(x-ph) + \dots + a_{q} f(x+qh)\right)=\\
&=\frac{1}{h^k} \sum_{\ell=-q}^p a_{\ell} f(x+\ell h)\\
&=\frac{1}{h^k} \sum_{\ell=-q}^p a_{\ell} \sum_{j=0}^\infty \frac{f^{(j)}(x)\ell^j h^j}{j!} \\
&=\frac{1}{h^k}  \sum_{j=0}^\infty \left( \sum_{\ell=-q}^p a_{\ell} \frac{\ell^j h^j}{j!} \right) f^{(j)}(x) =  \sum_{j=0}^\infty \left( \sum_{\ell=-q}^p a_{\ell} \frac{\ell^j h^{j-k}}{j!} \right) f^{(j)}(x) .
\end{align*} 
$$

And then you can match the coefficients to get the best approximation of the derivative. This leads to a linear systems in $a_{-p},\dots,a_q$.

[Solutions in Wikipedia](https://en.wikipedia.org/wiki/Finite_difference_coefficient)

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Exercises


* Consider the central difference stencil:
    $$
    \delta_{h}u(x) = \frac{-u(x+2h) + 8u(x+h) - 8u(x-h) + u(x-2h)}{12h}
    $$
    1. What is this divided difference approximating? (consistency)
    2. Determine the order of accuracy of this stencil. (Accuracy)

* Consider the stencil given by the coefficients:
  $$
       a_{-1}:= 1/6, \quad a_{0}:= -5/6, \quad a_{1}:= 3/2, \quad a_{2}:= -7/6, \quad a_{3}:= 1/3
  $$
  1. Which derivative is aiming to approximate?
  2. Determine the order of accuracy of this stencil.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Divided differences for two-point boundary problems

Let's start with a simple boundary value problem:
find $u:[a,b]\to \mathbb R$ such that $-u''(x)=f(x)$ for $x\in[a,b]$ and $u(a)=u(b)=0$, where $f:[a,b]\to \mathbb R$ is a given function. Suppose that we cannot find an analytical solution, how can we approximate it?

We try to approximate the solution in some equispaced points $x_i$ with $i=0,\dots,N$ with $x_{i+1}=x_i+h$, $x_0=a$ and $x_N=b$.

We have seen that we can approximate the second derivative with divided differences
$$
-u''(x_i) \approx \frac{u(x_{i+1}) - 2u(x_i) + u(x_{i-1})}{h^2} \qquad \forall i=0,\dots, N.
$$

So, we can look at an approximation of $u(x_i)\approx u_i$ for all $i=0,\dots,N$ that solves the following system
$$
-\frac{u_{i+1} - 2u_i + u_{i-1}}{h^2} = f(x_i) \qquad \forall i=1,\dots, N-1.
$$
Then, we can use the information from BC to set $u_0=u_N=0$.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Matrix form
$$
-\frac{u_{i+1} - 2u_i + u_{i-1}}{h^2} = f(x_i) \qquad \forall i=1,\dots, N-1.
$$

We can write this system in matrix form as
$$
\underbrace{-\frac{1}{h^2}\begin{bmatrix}
-2 & 1 & 0 & \dots & 0\\
1 & -2 & 1 & \dots & 0\\
0 & 1 & -2 & \dots & 0\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
0 & 0 & 0 & \dots & -2
\end{bmatrix}}_{=:A}
\underbrace{\begin{bmatrix}
u_1\\
u_2\\
u_3\\
\vdots\\
u_{N-1}
\end{bmatrix}}{=:U}
=
\underbrace{\begin{bmatrix}
f(x_1)\\
f(x_2)\\
f(x_3)\\
\vdots\\
f(x_{N-1})
\end{bmatrix}}_{=:F}
$$
We can use our favourite linear solver to find the solution $U$ from $AU=F$.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Inhomogeneous boundary conditions
Suppose now that the Dirichlet BC are now different from zero, i.e., $u(a)=u_0=\alpha$ and $u(b)=u_N=\beta$. How can we modify the system?
Clearly the first equation for $u_1$ becomes
$$
-\frac{u_0-2u_1+u_2}{h^2} = f(x_1) \Longrightarrow -\frac{\alpha-2u_1+u_2}{h^2} = f(x_1).
$$
But how can we incorporate this into the system without interfering with the other equations?
Add an artificial equation for $u_0$ and $u_N$: $u_0 = \alpha \qquad \text{and} \qquad u_N = \beta.$
Then, we can add the equations for $u_0$ and $u_N$ to the system and solve the system as before.
$$
\underbrace{-\frac{1}{h^2}\begin{bmatrix}
-h^2 & 0 & 0 &0 & \dots & 0& 0\\
1 & -2 & 1 & 0 & \dots & 0& 0\\
0 & 1 & -2 & 1 & \dots & 0& 0\\
0 & 0 & 1 & -2 & \dots & 0& 0\\
\vdots &\vdots & \vdots & \vdots & \ddots & \vdots & \vdots\\
0 & 0 & 0 & 0 & \dots & -2 & 1\\
0 & 0 & 0 & 0 & \dots & 0&-h^2
\end{bmatrix}}_{=:A}
\underbrace{\begin{bmatrix}
u_0\\
u_1\\
u_2\\
u_3\\
\vdots\\
u_{N-1}\\
u_N
\end{bmatrix}}{=:U}
=
\underbrace{\begin{bmatrix}
\alpha\\
f(x_1)\\
f(x_2)\\
f(x_3)\\
\vdots\\
f(x_{N-1})\\
\beta
\end{bmatrix}}_{=:F}
$$


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Neumann Boundary Conditions
Suppose now that the BC are of Neumann type on the left, i.e., $\partial_x u(a)=\alpha$ and $u(b)=\beta$. How can we modify the system?
We have to approximate at the border the derivative with a divided difference.
$$
\partial_x u(a) \approx \frac{u_1-u_0}{h} = \alpha. 
$$

Problem: this divided difference is only a first order approximation, while the second derivative is a second order approximation. This destroys the order of accuracy of the whole space.

Solution: use a higher order FD approximation of the derivative at the border.
$$
\partial_x u(a) \approx \frac{-3u_0+4u_1-u_2}{2h} = \alpha.
$$
Then, we can add this equation to the system and solve the system as before.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Exercise
Find the finite difference approximation of the homogeneous Dirichlet Poisson problem on a non uniform grid, i.e., $x_{i+1}-x_{i}\neq x_{i}-x_{i-1}$.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Errors!
We have seen that the **truncation error** of the finite difference approximation of the second derivative is of order $O(h^2)$, but how can we estimate the error of the solution?

**Truncation error**
$$
T(x) := f(x) - \frac{u(x+h) - 2u(x) + u(x-h)}{h^2} = \underbrace{f(x) +u''(x)}_{=0} -\frac{h^2}{24}\left( u^{(4)}(\xi)+u^{(4)}(\zeta)\right) .
$$
for some $\xi,\zeta \in [x-h,x+h]$.
Which is already good, we know that 
$$
\lvert T(x)\rvert \leq \frac{h^2}{12} \max_{a\leq \xi \leq b} \lvert u^{(4)}(\xi)\rvert.
$$

Can we pass this information to the error $|u(x_i)-u_i|$?

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Discrete maximum principle
Consider the finite difference discretization of the Poisson problem with homogeneous Dirichlet BCs. Let $A\in \mathbb R^{(N+1)\times (N+1)}$ be the LHS matrix and let $v\in \mathbb R^{N+1}$. If $(Av)_i \leq 0$ for all $i$ then
$$
\max_{i=1,\dots,N-1} v_i \leq \max\{v_0,v_{N}\}.
$$
### Proof
By contradiction, there exists a $v_n$ with $1\leq n \leq N-1$ such that $v_n>v_0$ and $v_n>v_{N}$ and it is the maximum $v_n = \max_{i=0,\dots,N} v_i$. Then, we have
$$
0\geq (Av)_n = -\frac{1}{h^2}\left(v_{n-1}-2v_n+v_{n+1}\right) \Longrightarrow v_n \leq \frac12 (v_{n-1} + v_{n+1}).
$$
Since, $v_n$ is the maximum, we have that $v_{n-1} \leq v_n$ and $v_{n+1}\leq v_n$, hence, $v_n \leq \frac12(v_{n+1}+v_{n-1})\leq v_n$, which means that $v_n=v_{n-1}=v_{n+1}=\max v_i$.
Analogusly we can show that $v_i= v_n$ for all $i=0,\dots,N$ which is a contradiction.



---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Theorem (a priori error estimation)
The finite difference method for the Poisson problem with Dirichlet BCs satisfies the error bound
$$
\lvert u(x_i) - u_i \rvert \leq \frac{h^2}{24} (b-a)^2 \max_{a\leq \xi \leq b} \lvert u^{(4)}(\xi)\rvert.
$$

### Proof (1/2)
Define with $M=\max_{\xi \in [a,b]}\lvert T(\xi)\rvert$ the maximum of the truncation error. Using the definition of the scheme we can write the truncation error as 
$$
\begin{align*}
&T(x_i) = f(x_i) + \frac{u(x_{i+1}) - 2u(x_i) + u(x_{i-1})}{h^2} = -\frac{u_{i+1} - 2u_i + u_{i-1}}{h^2} +\frac{u(x_{i+1}) - 2u(x_i) + u(x_{i-1})}{h^2} \\
&h^2 T(x_i) = e_{i+1}-2e_i+e_{i-1} \qquad \text{where } e_i = u(x_i) - u_i, \text{ for }i=1,\dots,N-1.
\end{align*}
$$
At the boundaries we are exact $e_0=e_N=0$.

Define the auxiliary function 
$$
\phi(x) = \frac{M}{2} \left(x-\frac{a+b}{2}\right)^2 
$$
and the auxiliary vector $v\in \mathbb R^{N+1}$ with $v_i := e_i+\phi(x_i)$ for $i=0,\dots,N$.


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

### Proof (2/2)

We check if $v$ satisfies the conditions of the discrete maximum principle. We have that
$$
\begin{align*}
(Av)_i &= -\frac{1}{h^2} \left( v_{i+1} - 2v_i + v_{i-1}\right) = -\frac{1}{h^2} \left( e_{i+1} - 2e_i + e_{i-1} + \phi(x_{i+1}) - 2\phi(x_i) + \phi(x_{i-1})\right)\\
&-T(x_i) - \frac{M}{2h^2} \left( \left(x_{i}+h-\frac{a+b}2\right)^2 - 2\left(x_i-\frac{a+b}2\right)^2 + \left(x_i-h-\frac{a+b}2\right)^2\right) \\
&= -T(x_i) - \frac{M}{2h^2} \left( h^2 - 0 + h^2\right) = -T(x_i) - M  \leq 0.
\end{align*}
$$
So we have that $\max v_i \leq \max\{v_0,v_N\}$.
$v_0 = e_0 + \phi(a) = \phi(a) = \frac{M}{2}\left(a-\frac{a}2-\frac{b}{2}\right)^2 = \frac{M}{8}(b-a)^2$ and $v_N = \frac{M}{8}(b-a)^2$, hence, 
$$v_i \leq \frac{M}{8}(b-a)^2\text{ for all }i .$$
This implies that
$$
e_i = u(x_i) - u_i = v_i - \underbrace{\phi(x_i)}_{\geq 0} \leq v_i \leq \frac{M}{8}(b-a)^2  \leq \frac{h^2}{24}(b-a)^2 \max_{\xi \in [a,b]} \lvert u^{(4)}(\xi)\rvert.
$$
Do the same with $v_i = -e_i + \phi(x_i)$ to get the other inequality.
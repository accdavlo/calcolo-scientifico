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

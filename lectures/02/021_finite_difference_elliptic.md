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
### With divided differences

### With Taylor and linear systems

### Wikipedia



---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Higher derivatives
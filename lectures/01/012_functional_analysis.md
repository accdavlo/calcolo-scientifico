---
marp: true
math: mathjax
---
<!--
title: Lecture 012 Functional Analysis
paginate: true
_class: titlepage
-->

# ~~Review of~~ Functional analysis concepts

---
<style scoped>section{font-size:23px;padding:50px;padding-top:50px}</style>

#### Disclaimer
These are concepts necessary to understand many aspects of the theory of PDEs as well of the numerical methods of the PDEs. 
They are a bit technical, I don't expect you to remember everything, but to understand why we need to introduce some concepts, in particular, when we will use them in the future lectures.


#### Source: Quarteroni



---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

# Divergence theorem [Wiki](https://en.wikipedia.org/wiki/Divergence_theorem)
Recall: **fundamental theorem of calculus** in 1D: if $f \in C^1([a,b])$, then
$$\int_a^b f'(x) \textrm{d} x = f(b) - f(a).$$

# Generalization to higher dimensions of fundamental theorem of calculus
Let $\Omega \subset \mathbb{R}^d$ be a compact subset with a piecewise smooth boundary $\partial \Omega$, and let $u : \Omega \to \mathbb{R}$ be a continuously differentiable function on an open neighborhood $O$ of $\bar{\Omega}\subset O$, i.e. $u\in C^1(O)$. Then, for each $i=1,\dots,d$,
$$
\int_{\Omega} \partial_{x_i} u(x) \textrm{d} x = \int_{\partial \Omega} u(x) n_i(x) \textrm{d} S,
$$
where $n(x) = (n_1(x), \dots, n_d(x))$ is the outward unit normal vector to $\partial \Omega$ at $x$, and $\textrm{d} S$ is the surface measure on $\partial \Omega$.


---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

# Proof of generalization to higher dimensions of fundamental theorem of calculus (for simple domain)

Let $\Omega:= \lbrace (x,y): x\in [a,b], \, g_1(x)\leq y \leq g_2(x) \rbrace$, case $x_i=y$.
$$
\int_{\Omega} \partial_{y} u(x,y)  \mathrm{d} x \mathrm{d} y = \int_{a}^b \int_{g_1(x)}^{g_2(x)}  \partial_{y} u(x,y) \mathrm{d} y \mathrm{d} x =  \int_{a}^b u(x,g_2(x)) - u(x,g_1(x)) \mathrm{d}x.
$$

$\partial \Omega  = \partial \Omega_1 \cup \partial \Omega_2$ where $\partial \Omega_i :=\lbrace (x,y): x\in[a,b], y=g_i(x) \rbrace$ for $i=1,2$.
Recall that since $n$ is normal to $S$, we have that $(n_x,n_y) dS = (\mathrm{d}y,-\mathrm{d}x)$, so
$$
\begin{align*}
&\int_{\partial \Omega_1} u(x,y) n_{y} dS = -\int_{a}^b u(x,g_1(x)) \mathrm{d} x, \\
&\int_{\partial \Omega_2} u(x,y) n_{y} dS = -\int_{b}^a u(x,g_2(x)) \mathrm{d} x =  \int_{a}^b u(x,g_2(x)) \mathrm{d} x.
\end{align*}
$$
Hence,
$$
\int_{\Omega} \partial_{y} u(x,y)  \mathrm{d} x \mathrm{d} y = \int_{\partial \Omega} u(x,y) n_{y} dS.
$$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

# Divergence theorem (special case of above)
Let $\Omega \subset \mathbb{R}^d$ be a compact subset with a piecewise smooth boundary $\partial \Omega$, and let $\mathbf{u} : \Omega \to \mathbb{R}^d$ be a continuously differentiable vector field function on an open neighborhood $O$ of $\bar{\Omega}\subset O$, i.e. $u_i\in C^1(O)$ for all $i=1,\dots,d$. Then, for each $i=1,\dots,d$,
$$
\int_{\Omega} \textrm{div}(\mathbf{u}) \textrm{d} x = \int_{\Omega} \sum_{i=1}^d \partial_{x_i} u_i(x) \textrm{d} x = \int_{\partial \Omega} \sum_{i=1}^d u_i(x) n_i(x) \textrm{d} S = \int_{\partial \Omega} \mathbf{u}(x) \cdot \mathbf{n}(x) \textrm{d} S,
$$
where $n(x) = (n_1(x), \dots, n_d(x))$ is the outward unit normal vector to $\partial \Omega$ at $x$, and $\textrm{d} S$ is the surface measure on $\partial \Omega$.

#### Integration by parts in high dimension
Let $f\in C^1(\Omega)$ and $\mathbf{u}\in (C^1(\Omega))^d$, then
$$
\int_{\partial \Omega } f \mathbf{u} \cdot \mathbf{n} \textrm{d} S = \int_{\Omega}\textrm{div}(f \mathbf{u}) =  \int_{\Omega} f \textrm{div}(\mathbf{u}) \textrm{d} x + \int_{\Omega} \nabla f \cdot \mathbf{u} \textrm{d} x.
$$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:50px}</style>

## Functional spaces
We are used to think about vector spaces as $\mathbb R^n$ or $\mathbb C^n$. However, we can also think about spaces of functions as vector spaces. For example, the space of continuous functions on an interval $[a,b]$ is a vector space, since the sum of two continuous functions is continuous and the scalar multiplication of a continuous function is also continuous.
We will call them **functional spaces** as their elements are functions. 

### Examples of (normed) functional spaces
* $C(\Omega)$: the space of continuous functions on $\Omega$, with the supremum norm $||f||_\infty = \sup_{x\in \Omega} |f(x)|$.
* $C^k(\Omega)$: the space of functions on $\Omega$ that are $k$-times continuously differentiable, with the norm $||f||_{C^k} = \sum_{p_1+\dots+p_d \leq k} ||\partial_{x_1^{p_1}\dots x_d^{p_d}}f||_\infty$.
* $C^\infty(\Omega)$: the space of functions on $\Omega$ that are infinitely differentiable.
* $L^2(\Omega):=\lbrace f:\Omega \to \mathbb R : \int_\Omega |f(x)|^2 dx <\infty\rbrace$: the space of square-integrable functions on $\Omega$, with the norm $||f||_{L^2} = \sqrt{\int_\Omega |f(x)|^2 dx}$.

**Keep these examples in mind, we will see them again and again!**

---
<style scoped>section{font-size:23px;padding:50px;padding-top:50px}</style>

## Exercise/Homework

Show that $||f||_{L^2} = \sqrt{\int_\Omega |f(x)|^2 dx}$ is a norm in $L^2(\Omega):=\lbrace f:\Omega \to \mathbb R : \int_\Omega |f(x)|^2 dx <\infty\rbrace$: the space of square-integrable functions on $\Omega$.

Recall: a norm is a function $||\cdot||: V \to \mathbb R$ that satisfies the following properties for all $u,v,w \in V$ and $\alpha \in \mathbb R$:
1. $||u|| \geq 0$ and $||u||=0$ if and only if $u=0$ (positive definiteness);
2. $||\alpha u|| = |\alpha| ||u||$ (homogeneity);
3. $||u+v|| \leq ||u|| + ||v||$ (triangle inequality).

Spoiler: there are infinitely many functions in $L^2$ that have $|| \cdot ||_{L^2} =0$. How to fix this?
We change the definition of $L^2$ as the space of equivalence classes of functions that are equal almost everywhere, i.e., 
$$L^2(\Omega):=\frac{\lbrace f:\Omega \to \mathbb R : \int_\Omega |f(x)|^2 dx <\infty\rbrace}{\sim}$$
where $f\sim g$ if $f(x)=g(x)$ for almost every $x\in \Omega$, i.e., if $\int_{\Omega} |f-g|^2 \mathrm{d}x=0$.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:50px}</style>

## Linear functionals



Given a functional space $V$, a **linear functional** is a map $L: V \to \mathbb{R}$ that satisfies linearity: $L(\alpha u + \beta v) = \alpha L(u) + \beta L(v)$ for all $u, v \in V$ and scalars $\alpha, \beta \in \mathbb{R}$.


### Examples
* The evaluation functional $L_{x_0}: C(\Omega) \to \mathbb{R}$ defined by $L_{x_0}(u) := u(x_0)$ for a fixed $x_0 \in \Omega$ is a linear functional;
* The integral functional $L: L^2(\Omega) \to \mathbb{R}$ defined by $L(u) := \int_\Omega u(x) dx$ is a linear functional;
* The bilinear form $B: L^2(\Omega) \times L^2(\Omega) \to \mathbb{R}$ defined by $B(u,v) := \int_\Omega u(x)v(x) dx$ is a bilinear functional.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:50px}</style>

## Linear functionals properties


### Boundedness and Continuity
A functional $L$ is bounded if there exists a constant $C$ such that $|L(u)| \leq C ||u||_V$ for all $u \in V$. If $V$ is a Banach space (normed and complete), then a linear bounded functional is also continuous.

#### Example of unbounded functional
The "evaluation in 0 of the derivative" functional $L: C^\infty([0,1]) \to \mathbb{R}$ defined by $L(u) := u'(0)$ is not bounded with respect to the supremum norm, since for any $C > 0$, we can find a function $u$ such that $||u||_\infty = 1$ but $|L(u)| = |u'(0)| \to \infty$, e.g. 
$$
u_n(x) = \sin(n\, x) \implies ||u_n||_\infty = 1, \quad L(u_n) = u_n'(0) = n \to \infty.
$$


---
<style scoped>section{font-size:23px;padding:50px;padding-top:50px}</style>


### Dual Space
The dual space $V^*=V'$ is the space of all bounded linear functionals on $V$.

$$V^*:=\lbrace F: V\to \mathbb R :\, F \text{ is linear and bounded}\rbrace.$$

### Norm
The norm of a functional $L \in V^*$ is defined as 
$||L||_{V^*} = \sup_{||u||_V \leq 1} |L(u)|=\sup_{||u||_V \neq 0} \frac{|L(u)|}{||u||_V}.$

### Homework
Show that the two formulae above are equivalent $\sup_{||u||_V \leq 1} |L(u)|=\sup_{||u||_V \neq 0} \frac{|L(u)|}{||u||_V}.$


---
<style scoped>section{font-size:23px;padding:50px;padding-top:20px}</style>

### Hilbert Space
A Hilbert space $H$ is a real or complex inner product space that is also a *complete* metric space with respect to the distance function induced by the inner product.

The inner product is a bilinear function $(\cdot,\cdot)_H: V\times V \to \mathbb R$ that is symmetric and positive definite. The induced norm  is $|| u||_H:= \sqrt{(u,u)_H}$.

#### Definition (Complete space)
A complete space is a space where every Cauchy sequence converges to a limit within the same space, i.e., for every $\lbrace u_n\rbrace_{n\in \mathbb N} \subset V$ such that 
$$\lim_{m,n \to \infty} ||u_m - u_n||_V = 0,$$
there exists $u \in V$ such that $\lim_{n \to \infty} ||u_n - u||_V = 0$.

#### Examples
* $L^2(\Omega)$ is a Hilbert space with the inner product defined as $(f,g)_{L^2} = \int_\Omega f(x)g(x) dx$.
* $C^0(\Omega)$ with the supremum norm is not a Hilbert space, since it is not complete with respect to the supremum norm. For example, the sequence of functions $f_n(x) = x^n$ converges pointwise to the function $f(x) = 0$ for $x \in [0,1)$ and $f(1) = 1$, which is not continuous, so it does not belong to $C^0(\Omega)$.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:50px}</style>

### Riesz Representative
The **Riesz representation theorem** states that for every bounded linear functional $L$ on a **Hilbert space** $H$, there exists a unique element $v_L \in H$ such that 
$$L(u) = ( u, v_L )_H$$
for all $u \in H$. Moreover, $||L||_{H^*} = ||v_L||_H$.
Conversely, for every element $u\in H$ there exists  a linear and bounded functional $L_u$ such that 
$$ 
L_u(v) = (u,v)_H \text{ for every }v\in H.
$$
Moreover, $||L_u||_{H^*} = ||u||_H$.

Hence, there is a bijection between $H$ and $H^*$.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:50px}</style>

## Bilinear form definitions
Given $V$ a normed functional space, a bilinear form $a$ is a function that maps every two elements of $V$ to a scalar
$$a:V\times V \to \mathbb R.$$

A form
* is **bilinear** if 
  * $a(\lambda u + \mu w, v)  = \lambda a( u ,v) + \mu a( w, v)$ for every $\lambda, \mu \in \mathbb R$ and every $v,w,u\in V$, and
  * $a( u, \lambda v + \mu w)  = \lambda a( u ,v) + \mu a( u,w)$ for every $\lambda, \mu \in \mathbb R$ and every $v,w,u\in V$;
* is **continuous** if  there exists an $M>0$ such that
  $$ a(u,v) \leq M \lVert u \rVert_V \lVert v \rVert_V \text{ for every } v,u\in V;$$
* is **symmetric** if $a(u,v)=a(v,u)$ for every $u,v\in V$;
* is **positive** if $a(v,v)>0$ for all $v\in V$ with $v\neq 0$;
* is **coercive** if there exists $\alpha>0$ such that $a(v,v)>\alpha \lVert v \rVert^2_V$ for all $v \in V$.



---
<style scoped>section{font-size:23px;padding:50px;padding-top:50px}</style>

### Homework
* $a(u,v):= \int_{\mathbb R} \sin(x)^2 \, u(x)v(x)\, \textrm{d} x$ is bilinear, continuous, symmetric, positive but not coercive on $L^2(\mathbb R)$
* $a(u,v):= \int_{\mathbb R} u(x)v(x) \,\textrm{d} x$ is bilinear, continuous, symmetric, positive and coercive on $L^2(\mathbb R)$
* $a(u,v):= \int_{\mathbb R} \sin(x)\, u(x)v(x) \, \textrm{d} x$ is bilinear, continuous, symmetric, not positive nor coercive on $L^2(\mathbb R)$
* $a(u,v):= \int_{\mathbb R} \sin(u(x)) \, v(x) \, \textrm{d} x$ is continuous, is not bilinear, not symmetric, not positive nor coercive on $L^2(\mathbb R)$.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:50px}</style>

## Distributions

Let $\Omega\subset \mathbb R^{d}$ be an open set and $f:\Omega \to \mathbb R$ a function.

### Support of a Function
The support of a function $f$, denoted by $\text{supp}(f)$, is the closure of the set where $f$ is non-zero.
$$\text{supp}(f):=\overline{\lbrace x\in\Omega : f(x) \neq 0\rbrace}.$$

### Compact Support
A function has compact support if its support is a compact set (compact = closed and bounded).

### $C^\infty$ Compact Support Functions
A function is in $\mathcal{D}(\Omega):=C^\infty_c(\Omega)$ if it is infinitely differentiable and has compact support in $\Omega$.


---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

### Convergence in $\mathcal{D}(\Omega)$
A sequence of functions $\{f_n\}$ in $\mathcal{D}(\Omega)$ converges to $f$ in $C^\infty_c(\Omega)$ if 
* exists a fixed compact set $K$ that contains all supports of $f_n$ 
* all derivatives of $f_n$ converge *uniformly* to the corresponding derivatives of $f$, i.e. $\partial_{x_1^{p_1}\dots x_d^{p_d}}f_n \to \partial_{x_1^{p_1}\dots x_d^{p_d}}f$ for all $p_1, \dots, p_d$.
 

---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

### Distributions
A **distribution** is a linear functional $T:\mathcal{D}(\Omega) \to \mathbb R$ that is continuous, i.e.,
$$\lim_{k\to \infty} T(\varphi_k) = T(\varphi),$$
for all $\varphi_k \to_{\mathcal{D}} \varphi \in \mathcal{D}$.
Hence, the distribution space $\mathcal{D}^*(\Omega)$ is the dual of $\mathcal{D}(\Omega)$.

Notation for distribution $T\in\mathcal{D}^*(\Omega)$ applied to a function $f\in\mathcal{D}(\Omega)$: $T(f)=\langle T,f\rangle$.

### Example Dirac Delta
The Dirac delta distribution $\delta_a$ with $a\in \Omega$ a point, is defined by $\delta_a(\phi) = \phi(a)$ for all $\phi \in \mathcal{D}(\Omega)$. It is a distribution that "picks out" the value of a function at a point.
The Dirac delta is not a functional on the $L^2(\mathbb R)$ space, since it is not bounded with respect to the $L^2$ norm. However, it is a distribution in $\mathcal{D}^*(\Omega)$.


### Convergence in $\mathcal{D}^*(\Omega)$
A sequence of distributions $T_n$ converges in $\mathcal{D}^*(\Omega)$ to $T\in \mathcal{D}^*(\Omega)$ if 
$$ \lim_{n\to \infty} T_n(\varphi) = T(\varphi), \qquad \forall \varphi \in \mathcal{D}(\Omega).$$


---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

## $L^2(\Omega)$ squared summable functions
$$L^2(\Omega):= \frac{\left\lbrace f:\Omega \to \mathbb R \text{ such that } \int_{\Omega} f(x)^2 \textrm{d} x < \infty \right\rbrace }{\sim},$$
$f\sim g$ if $f(x)=g(x)$ for almost every $x\in \Omega$.
1. $L^2(\Omega)$ is a Hilbert space with scalar product $(f,g):=\int_{\Omega} f(x)g(x)\textrm{d} x$.
2. The $L^2(\Omega)$ norm is define through the inner product as $\lVert f \rVert_{L^2(\Omega)} :=\sqrt{\int_{\Omega} f(x)^2\textrm{d} x}.$
3. To every function $f\in L^2(\Omega)$ is associated a distribution $T_f\in \mathcal{D}^*(\Omega)$ defined by 
   $$T_f(\varphi):= \int_{\Omega} f(x) \varphi(x)   \textrm{d} x,\qquad \forall \varphi \in \mathcal{D}(\Omega).$$
4. $\mathcal{D}(\Omega)$ is dense in $L^2(\Omega)$, i.e., for every $f\in L^2(\Omega)$ there exists a sequence of $\varphi_k\in \mathcal{D}(\Omega)$ such that 
$$\lVert \varphi_k - f \rVert_{L^2(\Omega)} \to 0.$$
5. $\mathcal{D}(\Omega)\subset L^2(\Omega) \Longrightarrow (L^2(\Omega))^*=L^2(\Omega)\subset \mathcal{D}^*(\Omega)$.
 
---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

## Example: convergence to Dirac Delta

Let $\chi_{[a,b]}$ be the characteristic function on the interval $[a,b]\subset \mathbb R$ defined as
$$
\chi_{[a,b]}(x)= \begin{cases}
0 & \text{if } x\notin [a,b]  ,    \\
1 & \text{if } x\in [a,b]  .    
\end{cases}
$$

Let us build the sequence of functions in $L^2(\mathbb R)$ $f_n(x) := \frac{n}2 \chi_{[-1/n,1/n]}(x).$ Clearly, we have that
1. $\int_{\mathbb R} f_n(x) \mathrm{d}x = 1$
2. $T_{f_n}(\varphi)= \int_{\mathbb R} f_n(x) \varphi(x) \mathrm{d}x = \frac{n}{2}\int_{-1/n}^{1/n} \varphi(x) \textrm{d}x = \frac{n}{2} (\Phi(1/n)-\Phi(-1/n))$ where $\frac{d}{dx}\Phi(x) = \varphi(x)$.
3. Let $h_n=1/n$, $T_{f_n}(\varphi)=\frac{\Phi(h_n)-\Phi(-h_n)}{2h_n}$
4. $\lim_{n\to \infty} T_{f_n}(\varphi)= \lim_{n\to \infty}\frac{\Phi(h_n)-\Phi(-h_n)}{2h_n} = \frac{d}{dx} \Phi(0) = \varphi(0)$.
5. $T_{f_n}(\varphi) \to \varphi(0) = \delta_0(\varphi)$.
6. $\delta_0$ is a distribution in $\mathcal{D}^*(\mathbb R)$ but not a function in $L^2(\mathbb R)$.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

## Definition: Derivation in distributional sense
Let $T\in\mathcal{D}^*(\Omega)$, with $\Omega\subset \mathbb R^d$ open. We can define the derivative of $T$ using the integration by parts.

$$
\partial_{x_i} T (\varphi) = \langle \partial_{x_i} T , \varphi \rangle:= -\langle T, \partial_{x_i}\varphi \rangle,\qquad \forall \varphi\in \mathcal{D}(\Omega)= C^{\infty}_c(\Omega).
$$

If $T$ is a $T_f$ with $f\in\mathcal{C}^1(\Omega)$, it is clearly the classical derivative. Let's see in 1D with $\Omega = [a,b]$.
$$
\partial_{x} T_f (\varphi) = \langle \partial_{x} T_f , \varphi \rangle = \int_a^b  \partial_{x} f(x) \varphi(x) \textrm{d}x = \underbrace{\left[  f(x) \varphi(x)\right]_a^b}_{=0} - \int_a^b   f(x) \partial_{x}\varphi(x) \textrm{d}x , \qquad \forall \varphi\in \mathcal{D}(\Omega).
$$
But the definition holds for every distribution, even for discontinuous functions, for the Dirac delta, etc. !!!

**Higher derivatives**
$$
\left\langle \frac{\partial^{p_1+\dots+p_d} T}{\partial x_1^{p_1} \dots \partial x_d^{p_d}}  , \varphi \right\rangle  := (-1)^{p_1+\dots+p_d}\left\langle T, \frac{\partial^{p_1+\dots+p_d}  \varphi}{\partial x_1^{p_1} \dots \partial x_d^{p_d}} \right\rangle,\qquad \forall \varphi\in \mathcal{D}(\Omega)= C^{\infty}_c(\Omega).
$$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

## Example: Derivative of Heaviside function
![bg right 75%](img/heaviside.png)

$$
R(x) = \begin{cases}
    1 &\text{ if }x>0,\\
    0 &\text{ if }x\leq 0,\\
\end{cases}
$$
* $R\in L^2((-1,1))$
* $R\notin C((-1,1))$
* $T_R\in \mathcal{D}^*((-1,1))$

$$\langle \partial_x T_R,\varphi \rangle = -\int_{-1}^1 R(x) \partial_x \varphi(x) \textrm{d} x$$
$$=-\int_{0}^1  \partial_x \varphi(x) \textrm{d} x = - \left[ \varphi\right]_0^1=\varphi(0)$$
$$
\Longrightarrow \partial_x R = \delta_0.
$$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

### Homework
* Compute the second derivative $\partial_{xx} T_R$ of the Heaviside function in the distributional sense
$R(x) = \begin{cases}
    1 &\text{ if }x>0,\\
    0 &\text{ if }x\leq 0,\\
\end{cases}$
* Compute the derivative of the function $f(x) = |x|$ in the distributional sense and checks that it coincides with the classical derivative where it is differentiable.
* Define the multiplication between a function $f\in \mathcal{C}^\infty$ and a distribution $T$ as $f\cdot T(\varphi) := T(f\cdot \varphi)$. Prove that for $f(x) = x$, we have that $f\cdot \delta'_0 = - \delta_0$ in distributional sense.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

## Sobolev Spaces

As we have seen $(L^2(\Omega))^*=L^2(\Omega)\subset \mathcal{D}^*(\Omega)$. This does not imply that their distributional derivatives are still in $L^2$. The Heaviside function is in $L^2$ but its derivative it's not.

We need to introduce other spaces to distinguish functions!

### Sobolev spaces
Let $\Omega\subset \mathbb R^d$ and $k \in \mathbb N_0$. We define the Sobolev space of order $k$ on $\Omega$ the space of the functions in $L^2(\Omega)$ with distributional derivatives up to order $k$ in $L^2(\Omega)$.
$$
H^k(\Omega):=\lbrace f\in L^2(\Omega): \partial_{x_1^{p_1}\dots x_d^{p_d}}f \in L^2(\Omega), \text{ for all }p_1,\dots,p_d: p_1+\dots+p_d \leq k \rbrace.
$$

* $H^{k+1}(\Omega)\subset H^k(\Omega)$
* $L^2(\Omega)=H^0(\Omega)$
* Heaviside $R\in H^0((-1,1))$, but $R\notin H^1((-1,1))$


---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

## Example
* Example of $H^1(\Omega)$ but not $H^2(\Omega)$ 
  $$
  f(x) = \begin{cases}
    x & \text { if }x > 0,\\
    0 & \text { if }x \leq 0.
  \end{cases} \qquad f'(x)= \begin{cases}
    1 & \text { if }x > 0,\\
    0 & \text { if }x \leq 0.
  \end{cases}
  $$


---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

## Norms and inner products of Sobolev spaces

* Sobolev spaces $H^k(\Omega)$ are Hilbert space with respect to the following scalar product
  $$(f,g)_k =(f,g)_{H^k(\Omega)}:= \sum_{p_1+\dots+p_d\leq k} \int_{\Omega} \partial_{x_1^{p_1}\dots x_d^{p_d}}f \cdot \partial_{x_1^{p_1}\dots x_d^{p_d}} g \, \textrm{d} x, $$
  with the norms
  $$\lVert f \rVert_k =\lVert f \rVert_{H^k(\Omega)}:= \sqrt{ \sum_{p_1+\dots+p_d\leq k} \int_{\Omega} (\partial_{x_1^{p_1}\dots x_d^{p_d}}f )^2 \, \textrm{d} x}, $$
* Seminorms
  $$\lvert f \rvert_k =\lvert f \rvert_{H^k(\Omega)}:= \sqrt{ \sum_{p_1+\dots+p_d = k} \int_{\Omega} (\partial_{x_1^{p_1}\dots x_d^{p_d}}f )^2 \, \textrm{d} x}, $$
* $\lVert f \rVert_k = \sqrt{\sum_{m=0}^k |f|_{m}^2}$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

## Examples for $k=1$

$$(f,g)_1=(f,g)_{H^1(\Omega)}= \int_{\Omega}f(x)\,g(x)\, \textrm{d}x+\int_{\Omega}f'(x)\,g'(x)\, \textrm{d}x$$

$$\lVert f \rVert_1= \sqrt{\int_{\Omega}f^2(x)\, \textrm{d}x+\int_{\Omega}(f'(x))^2\, \textrm{d}x} = \sqrt{ \lVert f \rVert_{L^2(\Omega)}^2 + \lVert f' \rVert_{L^2(\Omega)}^2 }$$

$$\lvert f \rvert_1= \sqrt{\int_{\Omega}(f'(x))^2\, \textrm{d}x} =  \lVert f' \rVert_{L^2(\Omega)} $$


---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

## Boundary for bounded domains
### Property 
If $\Omega\subset \mathbb R^d$ is open with a *smooth enough* boundary, then $H^k(\Omega)\subset C^m(\bar{\Omega})$ if $m<k-\frac{d}{2}$.

### Examples
$$
\begin{align*}
&d=1,\qquad m<k-\frac12,\qquad & & H^1((-1,1)) \subset C^0([-1,1]).\\
&d=2,\qquad m<k-1,\qquad & &H^1((-1,1)^2) \not\subset C^0([-1,1]^2), \qquad H^2((-1,1)^2)\subset C^0([-1,1]^2).\\
\end{align*}
$$


---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

## $H^1_0(\Omega)$
Let $\Omega$ be a bounded domain. We denote with $H^1_0(\Omega)$ the closure of $\mathcal{D}(\Omega)$ in $H^1(\Omega)$. (*morally zero on the boundary*)

## Theorem: Poincarè inequality
Let $\Omega \subset \mathbb{R}^d$ be a bounded domain with a Lipschitz boundary. There exists a constant $C = C(\Omega) > 0$ such that for all $u \in H^1_0(\Omega)$,
$$
\|u\|_{L^2(\Omega)} \leq C \|\nabla u\|_{L^2(\Omega)} = C|u|_1.
$$

### Proof
Since $\Omega\subset \mathbb R ^d$ is bounded there exists a ball $S_R=\lbrace x: |x-x_0|<R\rbrace$ that contains $\Omega$. Since, $\mathcal{D}(\Omega)$ is dense in $H^1_0(\Omega)$, we can prove the inequality for $u\in  \mathcal{D}(\Omega)$ and pass to the limit to get it for $H^1_0$. Notice that $\text{div}(x-x_0) = d$. So, using Cauchy-Schwarz,
$$
\begin{align*}
&\lVert u\rVert_{L^2(\Omega)}^2 = d^{-1} \int_{\Omega} d \, |u(x)|^2 \textrm{d}x = d^{-1} \int_{\Omega} \text{div}(x-x_0)|u(x)|^2 \textrm{d}x= -d^{-1} \int_{\Omega} (x-x_0) \nabla(|u(x)|^2) \textrm{d}x=\\
&-2d^{-1} \int_{\Omega} (x-x_0) u(x)\nabla(u(x)) \textrm{d}x\leq 2d^{-1} \lVert x-x_0 \rVert_{\infty} \lVert u \rVert_{L^2(\Omega)} \lVert \nabla u \rVert_{L^2(\Omega)} = 2d^{-1}R \lVert u \rVert_{L^2(\Omega)} \lvert  u \rvert_{1}.
\end{align*}
$$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:25px}</style>

### Proposition
On $H^1_0(\Omega)$ the seminorm $\lvert \cdot \rvert_1$ is actually a norm and it is equivalent to $\lVert \cdot \rVert_1$.
### Proof
$$ \lVert u \rVert_1^2 =\lvert u \rvert_1^2 + \lVert u \rVert_{L^2}^2 \leq (1+C^2)\lvert u \rvert_1^2.$$
On the other hand
$$\lvert u \rvert_1^2\leq \lvert u \rvert_1^2 + \lVert u \rVert_{L^2}^2 = \lVert u \rVert_1^2. $$


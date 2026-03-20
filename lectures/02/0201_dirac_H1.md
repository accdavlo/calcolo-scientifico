---
marp: true
math: mathjax
theme: default
paginate: true
---
<!--
title: Lecture 0201 Poisson problem with Dirac delta source in $H^1$
paginate: true
_class: titlepage
-->

# Poisson problem with Dirac delta source

---

<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

# Poisson problem with Dirac delta source
Consider the following problem on $\Omega = (-1,1)$:
$$\begin{cases}
-u'' = \delta_0, \\
u'(-1) = u'(1) = 0.
\end{cases}
$$

Using physical intuition, we expect $u$ to be a "tent" function with a peak at $x=0$ and linear decay towards the boundaries. However, we want to rigorously analyze this problem using functional analysis.

So, we are looking for a solution $u$ which is continuous and with derivatives in $L^2$. This suggests that we should work in the Sobolev space $H^1((-1,1))$.

Following the weak formulation of the problem, we have by the corollary of Lax-Milgram that
$$
\lVert u \rVert_{H^1} \leq C \lVert \delta_0 \rVert_{(H^{1})^*}.
$$

So, we expect $\delta_0$ to be a bounded linear functional on $H^1((-1,1))$. 


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

# Check boundness of $\delta_0$ on $H^1((-1,1))$ 1/n

Let's compute the norm of $\delta_0$ in the dual space $(H^1)^*$. First, recall that $H^1((-1,1))$ is continuously embedded in $C^0([-1,1])$, which means that every function in $H^1$ is continuous and can be evaluated at points.
$$
\begin{align*}
&\lVert \delta_0 \rVert_{(H^1)^*} = \sup_{u \in H^1, u \neq 0} \frac{|\delta_0(u)|}{\lVert u \rVert_{H^1}}= \sup_{u \in H^1, u \neq 0} \frac{|u(0)|}{\lVert u \rVert_{H^1}} .\\
\end{align*}
$$

Now, let's study $|u(0)|$ and let's try to bound it by the $\lVert u \rVert_{H^1}$.
By the fundamental theorem of calculus, we have for any $y \in (-1,1)$:
$$
u(0) = u(y) + \int_{y}^0 u'(x) \, dx.
$$
We can average over $y$ in $(-1,1)$ to get the following line, then using Cauchy-Schwartz we get the result
$$
\begin{align*}
&u(0) = \frac{1}{2} \int_{-1}^1 u(y) \, dy + \frac{1}{2} \int_{-1}^1 \int_{y}^0 u'(x) \, dx \, dy = \frac{1}{2} \int_{-1}^1 u(y) \, dy  +  \int_{y}^0 u'(x) \, dx.\\
&|u(0)| \leq \frac{1}{2} \sqrt{2} \lVert u \rVert_{L^2} + \sqrt{2} \lVert u' \rVert_{L^2} \leq C \lVert u \rVert_{H^1}.
\end{align*}
$$





---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

# Boundness of $\delta_0$ on $H^1((-1,1))$ and Riesz representation



So, $\delta_0$ is indeed a bounded linear functional on $H^1((-1,1))$. This means that we can apply the Riesz representation theorem to find a function $v_{\delta_0} \in H^1((-1,1))\subset C^0([-1,1])$ such that for all $u\in H^1((-1,1))$:
$$
\delta_0(u) =u(0)= \langle u, v_{\delta_0} \rangle_{H^1} = \int_{-1}^{1} u(x) v_{\delta_0}(x) \, dx + \int_{-1}^{1} u'(x) v_{\delta_0}'(x) \, dx.
$$

**Goal**: find $v_{\delta_0}\in C^1([-1,1])$ that verify the above equation.


---
<style scoped>section{font-size:21px;padding:50px;padding-top:10px}</style>

# Weak Formulation

Integrate by parts:
$$
\int u'v_{\delta_0}' = -\int u v_{\delta_0}'' + u(1)v_{\delta_0}'(1) - u(-1)v_{\delta_0}'(-1).
$$
Hence, we have that
$$
\int_{-1}^1 u(x) (v_{\delta_0}(x)-v''_{\delta_0}(x)) dx + u(1)v_{\delta_0}'(1) - u(-1)v_{\delta_0}'(-1) = u(0).
$$

Then, for any $u\in C^1_c(\Omega)$:
$$
u(0) = \int_{-1}^1 u (v_{\delta_0} - v_{\delta_0}'') dx.
$$

This means that we can construct a sequence of $u_\varepsilon \in C^1_c(\Omega)$ such that $u_\varepsilon \to \tilde{u}$ where $\tilde{u}(1)=1$ and $\tilde{u}(-1)=0$. Then, we have that
$$
\lim_{\varepsilon \to 0} \int_{-1}^1 u_\varepsilon (v_{\delta_0} - v_{\delta_0}'') dx  -\tilde{u}(0)  = \lim_{\varepsilon \to 0} \int_{-1}^1 u_\varepsilon (v_{\delta_0} - v_{\delta_0}'') dx -\tilde{u}(0) +v'_{\delta_0}(1).
$$
This means that $v'_{\delta_0}(1)=0$. Similarly, we can construct a sequence of $u_\varepsilon$ such that $\tilde{u}(1)=0$ and $\tilde{u}(-1)=1$ to get $v'_{\delta_0}(-1)=0$.


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>


So in distributional sense we want to solve:
$$
v_{\delta_0} - v_{\delta_0}'' = \delta_0.
$$

### Boundary Conditions

So we solve the boundary value problem:
$$
\begin{cases}
v_{\delta_0} - v_{\delta_0}'' = \delta_0, \\
v_{\delta_0}'(-1)=v_{\delta_0}'(1)=0.
\end{cases}
$$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

# Solve the ODE

For $x \neq 0$:
$$
v'' - v = 0
$$

General solution:
- $x>0$: $Ae^x + Be^{-x}$
- $x<0$: $Ce^x + De^{-x}$

Conditions:
- continuity at $0$
- jump: 
$$
\begin{align*}
&\lim_{\varepsilon \to 0} \int_{-\varepsilon}^\varepsilon v''-v\, \mathrm{d}x= -\int_{-\varepsilon}^\varepsilon \delta_0 = -1,\\
&\lim_{\varepsilon \to 0} v'(\varepsilon)-v(-\varepsilon) - 2\varepsilon v(0)  = v'(0^+)-v'(0^-)=  -1.
\end{align*}
$$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Solve the linear system

General solution:
- $x>0$: $Ae^x + Be^{-x}$
- $x<0$: $Ce^x + De^{-x}$

$$
\begin{cases}
Ae^1-Be^{-1} = 0 &\text{(Neumann BC at $x=1$)}\\
Ce^{-1}-De^1 = 0 &\text{(Neumann BC at $x=-1$)}\\
A+B = C+D &\text{(continuity at $x=0$)}\\
A-B - (C-D) = -1 &\text{(jump condition at $x=0$)}
\end{cases}
$$

Solution is 
$$
\begin{cases}
A = \frac{e^{-1}}{e^1-e^{-1}}\\
B = \frac{e}{e^1-e^{-1}}\\
C = \frac{e}{e^1-e^{-1}}\\
D = \frac{e^{-1}}{e^1-e^{-1}}
\end{cases}
$$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>


# Final Result

$$
v_{\delta_0}(x) = \frac{\cosh(1-|x|)}{2\sinh(1)}
$$

✔ $v_{\delta_0} \in H^1((-1,1))$  
✔ Represents the Dirac delta
✔ One can check that all the above conditions are statisfied


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

# Key Insight

In 1D:
$$
H^1 \subset C^0
$$

So:
- $\delta_0$ is bounded in $(H^1)^*$
- Riesz applies

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

# Higher Dimensions

In $ \mathbb{R}^2, \mathbb{R}^3, \dots$:

$$
H^1 \not\subset C^0
$$

So:
- $\delta_0$ is **not bounded** in $(H^1)^*$
- No Riesz representative in $H^1$


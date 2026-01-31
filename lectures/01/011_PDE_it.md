---
marp: true
math: mathjax
---
<!--
title: Lezione 011 PDE
paginate: true
_class: titlepage
-->

# Equazioni Differenziali Parziali

---

## PDE (partial differential equation, EDP in italiano) 

<style scoped>section{font-size:23px;padding:50px;padding-top:50px}</style>

Dato un dominio $\Omega \in \mathbb R ^{d}$ dove $d>1$, cerchiamo $u:\Omega \to \mathbb R^s$ dove $s\in \mathbb N_0$, soluzione di una **PDE stazionaria** di ordine $k$:
$$F(x,u, \nabla u \dots, \nabla^{(k-1)}u,\nabla^{(k)}u, g)=0$$
con $g:\Omega \to \mathbb R^s$ una funzione data. Oppure, più esplicitamente come
$$\mathcal{P}(u,g) \equiv F(x, u, \frac{\partial u}{\partial x_1},\dots, \frac{\partial u}{\partial x_d}, \frac{\partial^2 u}{\partial x_1 \partial x_1}, \dots, \frac{\partial^{p_1+\dots+p_d} u}{\partial^{p_1} x_1 \, \partial^{p_2} x_2 \dots \partial^{p_d} x_d }, g  )=0,$$ 
dove $p_1+ \dots + p_d\leq k$.

Una PDE **non stazionaria** di ordine $k$ si definisce come: trova $u:\Omega \times [0,T] \to \mathbb R^{s}$ tale che
$$\begin{equation}\mathcal{P}(u,g) \equiv F(x,t, u, \frac{\partial u}{\partial t}, \frac{\partial u}{\partial x_1},\dots, \frac{\partial u}{\partial x_d}, \frac{\partial^2 u}{\partial x_1 \partial x_1}, \dots, \frac{\partial^{p_0+p_1+\dots+p_d} u}{\partial^{p_0}t \,\partial^{p_1} x_1  \dots \partial^{p_d} x_d }, g  )=0,\end{equation}$$

dove $p_0+ \dots + p_d\leq k$.

Una soluzione classica di una PDE è una funzione $u\in \mathcal{C}^k(\Omega \times [0,T])$ che risolve l'equazione precedente.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

### Definizione
Se la PDE può essere scritta nella forma 
$$
\mathcal{P}(u,g) = a(x) u + b_0(x) \partial_t u + b_1(x) \partial_{x_1}u +\dots + b_d(x) \partial_{x_d}u + c_{\alpha(2,0,\dots,0)} \partial_{tt} u +\dots + \gamma_{\alpha(p_0,\dots ,p_d)} \frac{\partial^{p_0+\dots +p_d} u}{\partial^{p_0}t\,\partial^{p_1}x_1\dots \partial^{p_d}x_d}+\dots -g=0,
$$
cioè, se i coefficienti dell'incognito $u$ e delle sue derivate dipendono solo dalle variabili indipendenti $(t,x)$, allora la PDE è **lineare**. Altrimenti, è **non lineare**.

### Definizioni
Considera una PDE non lineare di ordine $k$
* se i coefficienti delle derivate di ordine $k$ dipendono solo dalle variabili indipendenti $(t,x)$, allora la PDE è **semilineare**;
* se i coefficienti delle derivate di ordine $k$ dipendono dalle variabili indipendenti  $(t,x)$ e dalle derivate parziali di $u$ di ordine al massimo $k-1$, allora la PDE è **quasi-lineare**;
* se non è quasi-lineare, è **completamente non lineare**.


--- 
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

### Esempi

* Equazione di reazione-avvezione-diffusione
    $$ \partial_t u = u_{xx } + c u_x + u^2,$$
    è semilineare.
* Equazione di Burgers inviscida
    $$
    \partial_t u + u u_x =0,
    $$
    è quasi-lineare ma non semilineare.
* L'equazione di Korteweg-de Vries (KdV)
    $$
    \partial_t u + u \partial_x u + \partial_{xxx} u =0,
    $$
    è semilineare.
* L'equazione di Monge-Ampère
    $$
    u_{xx}u_{yy} - (u_{xy})^2 =0
    $$
    è completamente non lineare.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Primo ordine lineare PDE, a.k.a. equazione di trasporto

$$ u_t + u_x=0 $$
Come si trova la soluzione generale?

Proviamo questo cambio di variabili 
$$(x,t) \to(\xi, \eta), \qquad \xi(x,t) = x+t,\, \eta(x,t)= x-t $$
con inversa
$$ x = \frac{\xi+\eta}{2}, t = \frac{\xi-\eta}{2}.$$
Sostituiamo le nuove variabili: $v(\xi,\eta):=u(x(\xi,\eta),t(\xi,\eta))$
$$\begin{align}u_x = v_\xi \xi_x + v_\eta \eta_x = v_\xi + v_\eta\\
u_t = v_\xi \xi_t + v_\eta \eta_t = v_\xi -v_\eta\end{align}$$
ottenendo una nuova PDE
$$0=u_t+u_x = 2 v_\xi \Longleftrightarrow v_\xi=0.$$
Implica che $v(\xi,\eta)=f(\eta)$ con $f\in\mathcal{C}^1(\mathbb R)$. Tornando alle variabili originali
$$u(x,t) = v(\xi(x,t),\eta(x,t)) = f(\xi(x,t))=f(x-t)$$

---
# Linee caratteristiche
<style scoped>section{padding-top:30px;align-content: start;}</style>

$$u_t+u_x=0, \qquad u(x,t) = v(\xi(x,t),\eta(x,t)) = f(\xi(x,t))=f(x-t).$$
$$X_{x_0}(t) = x_0+t$$

---

# Generalizzazione a coefficienti diversi
<style scoped>section{font-size:23px;padding-top:30px;align-content: start;}</style>

$$a(t,x)u_t+b(t,x)u_x+cu(t,x)=g(t,x), (t,x)\in\Omega\subset\mathbb R^2.$$
Ben definita (non singolare e $\mathcal{C}^1$) trasformazione $(t,x) \Leftrightarrow (\xi,\eta)$, cioè,
$$\left| \frac{\partial (\xi,\eta)}{\partial(t,x)}\right| := \left| \begin{pmatrix} \xi_t &\xi_x\\ \eta_t & \eta_x \end{pmatrix}\right| = \xi_t\eta_x - \xi_x \eta_t \neq 0.$$
Cambio di variabili: $u_t=v_\xi \xi_t + v_\eta\eta_t , \,u_x = v_\xi \xi_x + v_\eta \eta_x,$ dando
$$(a \xi_t + b \xi_x) v_\xi + (a\eta_t +b\eta_x)v_\eta +cv = g(t(\xi,\eta),x(\xi,\eta))$$
Obiettivo: semplificare l'equazione precedente, scegliamo $\eta$ tale che
$$a\eta_t + b \eta_x =0,$$
così che otteniamo un'ODE per ogni $\eta$
$$v_\xi + \frac{c}{a \xi_t + b \xi_x}v = \frac{g(t(\xi,\eta),x(\xi,\eta))}{a \xi_t + b \xi_x}.$$

---
# Generalizzazione a coefficienti diversi
<style scoped>section{font-size:23px;padding-top:30px;align-content: start;}</style>

Per ottenere $a\eta_t + b \eta_x =0$, bisogna notare che, w.l.o.g., stiamo cercando una curva $x(t)$ tale che $\eta(t,x(t)) = \eta_0$ costante per ogni $t$.
$$0= \frac{d \eta(t,x(t))}{dt} =\eta_t + \eta_x \frac{\partial x}{\partial t} \Longrightarrow \frac{\eta_t}{\eta_x} = -\partial_t x(t)$$ 
Quindi, abbiamo
$$\frac{\eta_t}{\eta_x} = -\frac{b}{a} \Longleftrightarrow \partial_t x(t) = \frac{b}{a}.$$

Integrando questa equazione, si ottiene la curva $x(t)$, portando alla definizione di $\eta(t,x)$ risolvendo per la costante $\eta_0$.


---
<style scoped>section{font-size:23px;padding-top:30px;align-content: start;}</style>

# Esempio
$$xu_t-tu_x=1$$

---
<style scoped>section{font-size:23px;padding-top:30px;align-content: start;}</style>

# Esempio
$$xu_t-tu_x=1$$
$$\begin{align}
&(x\xi_t -t\xi_x)v_\xi +(x\eta_t -t \eta_x)v_\eta =1\\
&(x\eta_t -t \eta_x)=0\\
&\frac{dx}{dt}=-\frac{t}{x}\\
&\int x\,dx=\int -t\,dt\\
&x=\sqrt{\eta_0^2-t^2}\\
&\eta(t,x):=\sqrt{t^2+x^2} & \eta_t = \frac{t}{\sqrt{t^2+x^2}}, \quad & \eta_x =  \frac{x}{\sqrt{t^2+x^2}},\\
&\xi(t,x)=\arctan (x/t) & \xi_t = \frac{t^2}{x^2+t^2}\frac{-x}{t^2} = -\frac{x}{x^2+t^2}, \quad & \xi_x = \frac{t}{x^2+t^2},\\
& t=\eta \cos(\xi),\,x = \eta \sin(\xi),\\
&\underbrace{(-\eta \sin(\xi) \frac{\eta \sin(\xi)}{\eta^2} -\eta\cos(\xi)\frac{\eta\cos(\xi)}{\eta^2})}_{=-1} v_\xi=1, &v=-\xi+f(\eta) \qquad u=-\arctan(x/t)&+f(x^2+t^2).
\end{align}
$$

---

## Esercizio

* Risolve $u_x-2u_y=0$
* Risolve $yu_x-xu_y+uy=xy$

---
<style scoped>section{font-size:23px;padding-top:30px;align-content: start;}</style>
# Second order linear PDE in 2D

Considera la PDE su $\Omega\subset \mathbb{R}^2$
$$\mathcal{P}(u,g) = A \partial_{xx}u+ B u_{xy} + C u_{yy} + Du_x + Eu_y +Fu-g=0\quad \forall (x,y) \in \Omega$$
dove $u\in \mathcal{C}^2(\Omega)$ e $A,B,C\in \mathcal C^2(\Omega)$ e non si annullano contemporaneamente. Classifichiamo la PDE in base al *discriminante* 
$$
\Delta := B^2-4AC.
$$
## Definizione
* Se $\Delta>0$ la PDE è detta **iperbolica** (in un punto $(x,y)$)
* Se $\Delta=0$ la PDE è detta **parabolica** (in un punto $(x,y)$)
* Se $\Delta<0$ la PDE è detta **ellittica** (in un punto $(x,y)$)


---
<style scoped>section{font-size:23px;padding-top:30px;align-content: start;}</style>

* ### Esempio iperbolico: equazione delle onde
    $$ \partial_{tt} u - c \partial_{xx} u =0 \text{ con }c>0$$
    Infatti, $\Delta = 4c>0.$

* ### Esempio parabolico: equazione del calore
    $$ \partial_{t} u - c \partial_{xx} u =0 \text{ con }c>0$$
    Infatti, $\Delta = 0.$

* ### Esempio ellittico: equazione di Poisson
    $$ - c \partial_{xx} u -c\partial_{yy}u =-c \Delta u =f \text{ con }c>0$$
    Infatti, $\Delta = -4c^2<0.$

* ### Cambio di segno: equazione di Tricomi
    $$y u_{xx}+ u_{yy}=0$$
    $\Delta = -4y.$

---
<style scoped>section{font-size:23px;padding-top:30px;align-content: start;}</style>

### Teorema
Il segno del discriminante $\Delta$ è invariante sotto trasformazioni di coordinate regolari e non singolari (cioè sotto un cambio di variabili).

#### Dimostrazione 1/2
Focalizziamo solo sui termini di ordine 2, poiché i termini di ordine 1 non contribuiscono al discriminante.
Supponiamo di eseguire un cambio di variabili $(x,y) \mapsto (\xi,\eta)$, dato da una diffeomorfismo.
Sotto questa trasformazione, i termini di ordine 2 si trasformano come segue:
$$\begin{equation}
    u_{xx} = \alpha^2 u_{\xi\xi} + 2\alpha\beta u_{\xi\eta} + \beta^2 u_{\eta\eta},
\end{equation}$$
$$\begin{equation}
    u_{xy} = \alpha\gamma u_{\xi\xi} + (\alpha\delta + \beta\gamma) u_{\xi\eta} + \beta\delta u_{\eta\eta},
\end{equation}$$
$$\begin{equation}
    u_{yy} = \gamma^2 u_{\xi\xi} + 2\gamma\delta u_{\xi\eta} + \delta^2 u_{\eta\eta},
\end{equation}$$
dove
$$\begin{equation}
    \alpha = \frac{\partial x}{\partial \xi}, \quad \beta = \frac{\partial x}{\partial \eta}, \quad \gamma = \frac{\partial y}{\partial \xi}, \quad \delta = \frac{\partial y}{\partial \eta}.
\end{equation}$$

---
<style scoped>section{font-size:23px;padding-top:30px;align-content: start;}</style>

#### Dimostrazione 2/2

Riscrivendo la PDE nelle nuove coordinate, i coefficienti trasformati $A', B', C'$ sono dati da
$$\begin{equation}
    A' = A\alpha^2 + B\alpha\gamma + C\gamma^2,
\end{equation}$$
$$\begin{equation}
    B' = 2A\alpha\beta + B(\alpha\delta + \beta\gamma) + 2C\gamma\delta,
\end{equation}$$
$$\begin{equation}
    C' = A\beta^2 + B\beta\delta + C\delta^2.
\end{equation}$$

Ora, calcolando il discriminante trasformato:
$$\begin{align}
    \Delta' &= B'^2 - 4A'C' \\
    &= (2A\alpha\beta + B(\alpha\delta + \beta\gamma) + 2C\gamma\delta)^2 \\
    &\quad - 4(A\alpha^2 + B\alpha\gamma + C\gamma^2)(A\beta^2 + B\beta\delta + C\delta^2).
\end{align}$$
Espandendo entrambi i termini e semplificando, troviamo che
$$\begin{equation}
    \Delta' = (B^2 - 4AC)(\alpha\delta - \beta\gamma)^2 = \Delta \det(J)^2,
\end{equation}$$
dove $J$ è la matrice Jacobiana della trasformazione. Poiché $\det(J)^2 \geq 0$, il segno di $\Delta$ rimane invariato. Questo prova l'invarianza del segno del discriminante sotto un cambio di variabili.


---
<style scoped>section{font-size:23px;padding-top:30px;align-content: start;}</style>

## Forma canonica iperbolica

Considera l'equazione delle onde
$$\partial_{tt} u- c \partial_{xx} u =0$$
con $c>0$. Possiamo trovare un cambio di variabili $(x,t) \mapsto (\xi,\eta)$ tale che la PDE si semplifichi a
$$\partial_{\xi\eta} v =0.$$
La mappa è definita da 
$$\eta=x+t,\quad \xi = x-t.$$
Questa è la forma canonica di una PDE iperbolica. La soluzione generale è data integrando in $\xi$ e poi in $\eta$, cioè,
$$v(\xi,\eta) = \int^{\xi} \int^{\eta} \partial_{wz} v(w,z)\, dz\, dw = \int^{\xi} f(w)  dw = F(\xi) + G(\eta) ,$$
dove $\partial_\xi F(\xi) = f(\xi)$.
Quindi, la soluzione generale dell'equazione delle onde è 
$$ u(x,t) = F(x-t) + G(x+t).$$

---
<style scoped>section{font-size:23px;padding-top:30px;align-content: start;}</style>

## Forma canonica iperbolica: possiamo sempre ottenere questa forma?
Considera solo i termini di ordine 2 della PDE iperbolica $\Delta = B^2-4AC>0$.
$$ A \partial_{xx}u+ B u_{xy} + C u_{yy} =0.$$
Cerciamo un cambio di variabili $(x,y) \mapsto (\xi,\eta)$ tale che la PDE si semplifichi a 
$$\partial_{\xi\eta} v =0.$$
La trasformazione può essere applicata notando che
$$
\begin{align}
&u_{xx} = v_{\xi\xi}(\xi_x)^2 + 2v_{\xi\eta}\xi_x\eta_x + v_{\eta\eta}(\eta_x)^2,\\
&u_{xy} = v_{\xi\xi}\xi_x\xi_y + v_{\xi\eta}(\xi_x\eta_y+\xi_y\eta_x) + v_{\eta\eta}\eta_x\eta_y,\\
&u_{yy} = v_{\xi\xi}(\xi_y)^2 + 2v_{\xi\eta}\xi_y\eta_y + v_{\eta\eta}(\eta_y)^2,
\end{align}
$$

La PDE trasformata legge
$$ (A\xi_x^2+B\xi_x\xi_y + C \xi_y^2)v_{\xi\xi} + (2A\xi_x\eta_y + B(\xi_x\eta_y+\xi_y\eta_x )+ 2C\xi_y\eta_x)v_{\xi\eta} + (A\eta_x^2+B\eta_x\eta_y+C\eta_y^2)v_{\eta\eta}=0.$$

---
<style scoped>section{font-size:23px;padding-top:30px;align-content: start;}</style>
Spazio di calcolo

---
<style scoped>section{font-size:20px;padding-top:30px;align-content: start;}</style>
$$ (A\xi_x^2+B\xi_x\xi_y + C \xi_y^2)v_{\xi\xi} + (2A\xi_x\eta_y + B(\xi_x\eta_y+\xi_y\eta_x )+ 2C\xi_y\eta_x)v_{\xi\eta} + (A\eta_x^2+B\eta_x\eta_y+C\eta_y^2)v_{\eta\eta}=0.$$
Vogliamo trovare il cambio di variabili tale che
$$
\begin{align}
\begin{cases}
A\xi_x^2+B\xi_x\xi_y + C \xi_y^2 = 0\\
A\eta_x^2+B\eta_x\eta_y+C\eta_y^2=0
\end{cases}
\end{align}
$$
Queste sono PDE di primo ordine, quindi stiamo cercando curve caratteristiche tali che $\xi(x,y)=\text{const}$, se troviamo una curva, per esempio $y(x)$ tale che $\xi(x,y(x))=\text{const}$, allora
$$\frac{d\xi}{dx} = \frac{\partial \xi}{\partial x} + \frac{\partial \xi}{\partial y}\frac{dy}{dx} =0 \Longrightarrow \frac{dy}{dx} = -\frac{\partial_x \xi}{\partial_y \xi}.$$
Dalla prima PDE, otteniamo
$$
A\left(\frac{dy}{dx}\right)^2 - B\frac{dy}{dx} + C =0,
$$
che è chiamata l'equazione caratteristica per la PDE originale. Questa è un'equazione quadratica in $\frac{dy}{dx}$ con $\Delta = B^2-4AC>0$. Le due soluzioni distinte sono
$$
\frac{dy}{dx} = \frac{+B\pm \sqrt{\Delta}}{2A}.
$$
Da questo possiamo ottenere la trasformazione $(x,y) \mapsto (\xi,\eta)$ come abbiamo fatto nel caso lineare.

---
<style scoped>section{font-size:23px;padding-top:30px;align-content: start;}</style>
Spazio di calcolo

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Esempio 
$$u_{tt}+u_{tx} =0$$

$$
\begin{align}
(\xi_t^2+\xi_t\xi_x)u_{\xi\xi} + (2\xi_t\eta_t +\xi_t\eta_x+\xi_x\eta_t)u_{\xi\eta} + (\eta_t^2+\eta_t\eta_x)u_{\eta\eta} =0\\
\end{align}
$$
Le equazioni per $\xi$ e $\eta$ sono le stesse.
Cerciamo una curva $y(x)$ tale che $\xi(x,y(x))=\text{const}$, cioè, $\xi(x,y(x)) = x+y(x)=\text{const}$ e che
$$
\begin{align}
&\xi_t^2+\xi_t\xi_x =0\\
&\frac{\xi_t^2}{\xi_x^2}+\frac{\xi_t}{\xi_x} =0\\
&\left(\frac{dx}{dt}\right)^2-\frac{dx}{dt} =0\\
&\frac{dx}{dt}=\begin{cases}
0\\
1
\end{cases}
 \Longrightarrow x(t) = \begin{cases}
\xi_0\\
\eta_0+t
\end{cases}\\
\Longrightarrow & \eta=x-t, \quad \xi=x.
\end{align}
$$

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

### Che cosa succede se proviamo a fare la stessa cosa con una PDE parabolica?

$$
\frac{dx}{dt} = -\frac{B\pm \sqrt{\Delta}}{2A}=-\frac{B}{2A}.
$$
C'è solo una curva caratteristica. Quindi, scegliendo $\xi = 2A x + B t$ e $\eta = x$ otteniamo la forma canonica
$$
A\frac{\partial^2 v}{\partial \xi^2} =0,
$$
con la soluzione generale $v(\xi,\eta) = F(\eta) + \xi G(\eta)$.

### Che cosa succede se proviamo a fare la stessa cosa con una PDE ellittica?
Non c'è una caratteristica che sia conservata. Ma, si può invece eliminare il coefficiente di $u_{\xi\eta}$ per ottenere la forma canonica per la PDE ellittica. Usando $\eta=t$ e $\xi=\frac{2Ax-Bt}{\sqrt{\Delta}}$, otteniamo
$$
A\left(\frac{\partial^2 v}{\partial \xi^2} + \frac{\partial^2 v}{\partial \eta^2}\right) =0.
$$


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

# Esistenza, unicità e ben posta
Per le PDE sopra abbiamo trovato classi di soluzioni. Come possiamo trovare soluzioni uniche a problemi specifici? Cosa dobbiamo specificare?
## Definizione (Problema di Cauchy)
Considera una PDE di ordine $k$ in $\Omega\subset \mathbb R^d$ e sia $S$ una superficie data su $\mathbb R^d$. Sia anche $n = n(x)$ il vettore unitario normale alla superficie $S$ in un punto $x = (x_1 , x_2 ,\dots, x_d )\in S$. Supponiamo che in ogni punto $x$ della superficie $S$ i valori della soluzione $u$ e di tutti i suoi derivati direzionali di ordine $k − 1$ nella direzione di $n$ siano dati, cioè, che abbiamo funzioni $f_0 , f_1 , \dots, f_{k−1}: S \to \mathbb R$ tali che
$$u(x) = f_0 (x),
\text{ e }
\frac{\partial u}{\partial n}(x) = f_1(x),
\text{ e }
\frac{\partial^2 u}{\partial n^2}(x) = f_2 (x), \dots,
\text{ e }
\frac{\partial^{k-1} u}{\partial n^{k-1}}(x) = f_{k−1} (x).
$$
Il **Problema di Cauchy** consiste nel trovare le funzioni $u$ sconosciute che soddisfino contemporaneamente la PDE e le condizioni sopra, che sono chiamate **condizioni iniziali** (ICs) e le funzioni $f_0 , f_1 , \dots , f_{k−1}$, saranno riferite come i dati iniziali.
Secondo il ruolo delle ICs possono essere chiamate anche **condizioni al bordo** (BCs).

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Esempi (Problema di Cauchy per l'equazione di trasporto)
$$
\begin{align}
\begin{cases}
    u_t+u_x = 0, \quad (x,t)\in\mathbb R^2,\\
    u(0,x) = \sin(x), \quad x\in\mathbb R.
\end{cases}
\end{align}
$$
Qui, $S=\lbrace (t,x)\in \mathbb R^2: t=0  \rbrace$.
La soluzione generale dell'equazione di trasporto è $u(x,t) = f(x-t)$, quindi la condizione iniziale legge $f(x) = \sin(x)$, cioè, $u(x,t) = \sin(x-t)$.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Esempi (Problema di Cauchy per l'equazione delle onde)

$$
\begin{align}
\begin{cases}
    u_{tt}-u_{xx} = 0, \quad (x,t)\in\mathbb R^2,\\
    u(t,0) = \sin(t), \quad t\in\mathbb R,\\
    u_x(t,0) = 0, \quad t\in\mathbb R.
\end{cases}
\end{align}
$$
In questo caso, $S=\lbrace (t,x)\in \mathbb R^2: x=0  \rbrace$ e $n=(n_t,n_x)=(0,-1)$. La soluzione generale dell'equazione delle onde è $u(t,x) = f(x-t) + g(x+t)$, quindi le condizioni iniziali (al bordo) leggono $f_0(t) = \sin(t)$ e $f_1(t) = 0$, quindi
$$
\begin{align}
    \begin{cases}
        f(-t)+g(t) = \sin(t),\\
        f'(-t)+g'(t) = 0,
    \end{cases} \Longrightarrow f(\xi) = \frac{1}{2}\sin(-\xi), \quad g(\eta) = \frac{1}{2}\sin(\eta),
\end{align}
$$
quindi, $u(t,x) = \frac12 \left( \sin(x+t) + \sin(-x+t) \right)$.




---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

# Teorema (Teorema di Cauchy-Kovalesvskaya)
Considera un problema di Cauchy per una PDE lineare, sia $x^0$ un punto della superficie iniziale $S$, che è assunta analitica (molto regolare). Supponiamo che $S$ non sia una superficie caratteristica nel punto $x^0$. Assumiamo che tutti i coefficienti della PDE lineare, il lato destro $g$, e tutti i dati iniziali $f_0 , f_1 ,\dots, f_{k−1}$ siano funzioni analitiche su un intorno del punto $x^0$. Allora, il problema di Cauchy ha una soluzione $u$, definita in un intorno di $x^0$. Inoltre, la soluzione $u$ è analitica in un intorno di $x^0$ e è unica nella classe di funzioni analitiche.

* Assunzioni: Regolarità
* Outcome: Esistenza
* Outcome: Unicità
* Outcome: Regolarità della soluzione

$\,$
* È sufficiente? No, la soluzione potrebbe comunque comportarsi male


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

# Ben posta


## Definizione
Un problema di PDE è ben posta se:
1. La PDE ha una soluzione
2. La soluzione è unica
3. La soluzione dipende continuamente dai coefficienti della PDE e dai dati del problema (IC/BC)

Se il problema di PDE non è ben posta, diciamo che è mal posta.







---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Esercizio
Mostra che la soluzione del problema di Cauchy per l'equazione delle onde 
$$
\begin{cases}
    \partial_{tt} u - \partial_{xx} u =0,\\
    u(t,0) = f(t),\\
    u_x(t,0) = g(t)
\end{cases}
$$
per alcuni BCs $f$ e $g$ è data dalla formula di d'Alembert
$$
u(t,x) = \frac12 (f(t-x)+f(t+x)) + \frac12 \int_{t-x}^{t+x}g(s) \textrm{d}s.
$$
Mostra che il problema di Cauchy è ben posta (saltando l'unicità). *


---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Esercizio * [Dubrovin's notes](https://people.sissa.it/~dubrovin/fm1_web.pdf)
1. Trova la soluzione dell'equazione di Laplace su $\Omega=[0,2\pi]$ per vari $k$
$$
\begin{cases}
    \partial_{tt} u + \partial_{xx} u =0,\\
    u(0,x) = 0,\\
    u_t(0,x) = \frac{\sin(kx)}{k},\\
    u(t,0)=u(t,2\pi).
\end{cases}
$$
Passi:
* $u_k = \frac{a_0(t)}{2} + \sum_{n=1}^{\infty} [a_n(t) \cos (nx) + b_n(t)\sin(nx)]$
* Sostituendo nell'equazione e trovando la soluzione generale usando il metodo della separazione delle variabili
* $\partial_{tt} a_n(t)=n^2 a_n(t)$ per tutti i $n$ con $a_n(0)=0, \partial_t a_n(0)=0$
* $\partial_{tt} b_n(t)=n^2 b_n(t)$ per tutti i $n$ con $b_n(0)=0, \partial_t b_n(0)=0$ per $n\neq k$, $\partial_t b_k(0)=1/k$.
* $u_k(t,x)= \frac{1}{k^2}\sin(kx) \sinh(kt)$ 

2. Anche se $\sup_x |u_k(0,x)| + |\partial_t u_k(0,x)|$ è piccolo, possiamo trovare un $k$ abbastanza grande in modo che per qualsiasi tempo $t_0>0$ $\sup_x |u_k(t_0,x)| + |\partial_t u_k(t_0,x)|$ sia grande.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

### Teorema *
Sia $u_k(t,x) =  \frac{1}{k^2}\sin(kx) \sinh(kt)$. Per qualsiasi positivo $\varepsilon, M, t_0$ esiste un intero $K$ tale che per qualsiasi $k>K$ i dati iniziali soddisfano $\sup_x |u_k(0,x)| + |\partial_t u_k(0,x)|<\varepsilon$ ma la soluzione al tempo $t_0$ soddisfa $\sup_x |u_k(t_0,x)| + |\partial_t u_k(t_0,x)|>M$.
**Dimostrazione:** Scegliamo un intero $K_1$ soddisfacente $K_1 > \frac{1}{\epsilon}$ avremo l'ineguaglianza della condizione iniziale per qualsiasi $k \geq K_1$. Per ottenere una stima inferiore della seconda forma al tempo $t_0$ osserviamo che
$$\sup_{x \in [0, 2\pi]} (|u_k (x, t)| + |\partial_t u_k (x, t)|) = \frac{1}{k^2}  \sinh(kt) + \frac{1}{k} \cosh(kt) > \frac{1}{k^2} e^{kt}$$
dove abbiamo usato un'ineguaglianza ovvia $\frac{1}{k} > \frac{1}{k^2} \text{ per } k > 1.$
La funzione $y = \frac{e^x}{x^2}$ è monotona crescente per $x > 2$ e $\lim_{x \to +\infty} \frac{e^x}{x^2} = +\infty.$
Quindi per qualsiasi $t_0 > 0$ esiste $x_0$ tale che $\frac{e^x}{x^2} > \frac{M}{t_0^2} \text{ per } x > x_0.$
Sia $K_2$ un intero positivo soddisfacente $K_2 > \frac{x_0}{t_0}.$
Allora per qualsiasi $k > K_2$ 
$$\frac{e^{kt_0}}{k^2} = t_0^2 \frac{e^{kt_0}}{k^2t_0^2} > t_0^2\frac{e^{x_0}}{x_0^2} > M.$$
Scegliamo $K = \max(K_1, K_2)$ e completiamo la dimostrazione del Teorema.

---
<style scoped>section{font-size:23px;padding:50px;padding-top:0px}</style>

## Take home message
Non tutti i dati al bordo sono adatti per avere un problema ben posta.
---
layout: post
title: 连分数与丢番图方程简介
date: 2015-1-13
categories: blog
tags: [Python,数学,Lisp,Project Euler]
description: 本文主要围绕两方面的内容进行简单介绍：1、连分数及其求解方法；2、佩尔方程及其求解方法。
---

* TOC
{:toc}

# 一、连分数简介

在数学中，[连分数](http://zh.wikipedia.org/zh-cn/%E8%BF%9E%E5%88%86%E6%95%B0) 即如下表达式：

$$x=a_0+\frac{1}{a_1+\frac{1}{a_2+\frac{1}{\ddots}}}=[a_0;a_1,a_2,\cdots]$$

其中 $a_i\in \mathbb{Z},i\in \mathbb{N}$ 。

连分数具有如下性质：

- 有理数的连分数表示只有有限的项，并且当没有尾随的 1 时，其表示方法唯一；
- 无理数的连分数表示是唯一的；
- 勒让德定理：二次无理数 $y$ 的连分数表示会产生循环，即 $y=[a_0;\overline{a_1,a_2,\cdots,a_2,a_1,2a_0}],a_0=[\,y\,]$；
- 数 $x$ 的截断连分数表示是在特定意义上最佳可能的有理数逼近。

###### 表 1：求 3.245 的连分数

| 取整 |   求差值  | 取倒数  |
| ---: |  ---:   |   ---: |
| 3 |  3.245 - 3 = 0.245   |   1 / 0.245 = 4.082 |
| 4 |  4.082 - 4 = 0.082   |   1 / 0.082 = 12.250|
| 12 | 12.250 - 12 = 0.250 |   1 / 0.250 = 4.000 |
| 4 |  4.000 - 4 = 0.000   |   结果为 [3;4,12,4]  |

这个算法适合于实数，但如果用浮点数实现的话，可能导致 [数值灾难](http://zh.wikipedia.org/zh-cn/%E6%B5%AE%E7%82%B9%E6%95%B0 "数值灾难")。为了得到精确的结果，需要用 [欧几里得 GCD 算法](http://zh.wikipedia.org/wiki/%E8%BC%BE%E8%BD%89%E7%9B%B8%E9%99%A4%E6%B3%95#.E4.B8.BE.E4.BE.8B) 的变体作为替代。

## 1、数值灾难

由于浮点数被用以在计算机中对实数进行**近似**表示，因此浮点运算与数学运算有所差异，导致无论是 Python、Matlab 还是经典的 C 语言，都无法通过上面的方法求出 3.245 的连分数，但有一个例外，那就是 Lisp。Lisp 不会自动求出 3245/1000 的结果，因此计算过程变成了分数的计算而非浮点运算，可以得到精确结果。

##### Lisp 的求法

```lisp
(defun frac (n)
	(write (floor n))(format t " ")
	(setq a (- n (floor n))) 
	(if (/= a 0) (frac (/ 1 a)))
)(frac (/ 3245 1000))
```
---

```
3 4 12 4
```

##### 欧几里得 GCD 算法（辗转相除法）

```python
def GCD(a,b,ans=[]): # 实数 a/b 的连分数
	if b:	return GCD(b, a%b, ans+[int(a/b)])
	else:	return ans
print(GCD(3245,1000))
```
---

```
[3, 4, 12, 4]
```

## 2、二次无理数的连分数

Lisp 或 GSD 算法对无理数的连分数都有些无能为力。下面着重讨论无理数 $\sqrt{n}$ 的连分数展开技巧[^frac]：

[^frac]: 杨中和. [二次无理数的连分数](http://wenku.baidu.com/link?url=whoEM9f9zCklDblBAxyboqjeIj_FGqPp3CZ89Y-y8GiwxQGCy8ze2W8NNAhbFotQvygkFJGbjukUTyr4pmzY_wh1jWmwzT8c47qw31v6ELe) [J]. 西安文理学院学报：自然科学版, 2008, 11(2): 24-58.

###### 表 2：求 $\sqrt{7}$ 的连分数($[\,\sqrt{7}\,]=2$)

| 取整 |  取倒数 |  分母有理化 | 分离整数与小数 |
| :---: |  :---:   |   :---: | :---: |
|  |  | | $2+\frac{\sqrt{7}-2}{1}$ |
| 2 |  $\frac{1}{\sqrt{7}-2}$ |  $\frac{\sqrt{7}+2}{3}$| $1+\frac{\sqrt{7}-1}{3}$ |
| 1 |  $\frac{3}{\sqrt{7}-1}$ |  $\frac{\sqrt{7}+1}{2}$| $1+\frac{\sqrt{7}-1}{2}$ |
| 1 |  $\frac{2}{\sqrt{7}-1}$ |  $\frac{\sqrt{7}+1}{3}$| $1+\frac{\sqrt{7}-2}{3}$ |
| 1 |  $\frac{3}{\sqrt{7}-2}$ |  $2+\sqrt{7}$| 结果为：$[2;\overline{1,1,1,4}]$ |

将上述算法一般化：设 $k=[\,\sqrt{n}\,]$，并令 $n_c=n-c^2$。

$$\sqrt{n}=\left[k;\frac{k+i_1}{n_k},\frac{i_1+i_2}{n_{i_1}/n_k},\cdots,\frac{i_{l-1}+i_l}{q},\frac{i_l+i_{l+1}}{n_l/q},\cdots\right]$$  


其中，若求得 $\frac{i_{l-1}+i_l}{q}$，则取满足 $i_{l+1}\leq k$ 的最大值，使 $i_l+i_{l+1}$ 能被 $n_l/q$ 整除。

如果考虑将 $\frac{i+j}{q}=a \Rightarrow i-\frac{a}{q}-j$ 的形式，有：

$$\sqrt{n}=0-\frac{k}{1}-k-\frac{a_1}{n_k}-i_1-\frac{a_2}{q_1}-i_2-\frac{a_3}{q_2}-i_3-\cdots$$  

其中，$\frac{n_{i_1}}{n_k}=q_1,\,\frac{n_{i_2}}{q_1}=q_2,\cdots$

## 3、渐近分数列

如下表所列，渐近分数常用于无理数的逼近。

###### 表 3：连分数与渐近分数列

| |  连分数 |  渐近分数列 | 
| :---: |  :---:   |   :---: |
| $\sqrt{2}$ |  $[1;\bar{2}]$ |  $\frac{1}{1},\frac{3}{2},\frac{7}{5},\frac{17}{12},\cdots$| 
| $\sqrt{7}$ |  $[2;\overline{1,1,1,4}]$ |  $\frac{2}{1},\frac{3}{1},\frac{5}{2},\frac{8}{3},\cdots$| 
| $\frac{\sqrt{5}-1}{2}$ | $[0;\bar{1}]$ |  $\frac{1}{1},\frac{1}{2},\frac{2}{3},\frac{3}{5},\frac{5}{8},\frac{8}{13},\cdots$| 
|  $\pi$ |  $[3;7,15,1,292,1,1,\cdots]$ |$\frac{3}{1},\frac{22}{7}\text{（约率）},\frac{333}{106},\frac{355}{113}\text{（密率）},\frac{103993}{33102},\cdots$ |
|  $\mathrm{e}$ |   $[2;1,2,1,\cdots,1,2k,1,\cdots]$| $\frac{2}{1},\frac{3}{1},\frac{8}{3},\frac{11}{4},\frac{19}{7},\frac{53}{23},\cdots$| 

数学上可以证明：由连分数得到的渐近分数，其值是在分子或分母小于下一个渐近分数的分数中，最接近精确值的近似值。

对渐进分数列 $\\{\frac{p_i}{q_i},\,i\in \mathbb{N}^+\\}$，有 $\frac{p_1}{q_1}=\frac{a_0}{1},\frac{p_1}{q_1}=\frac{a_1a_0+1}{a_1}$，其递推式为：

<p>
$$\begin{bmatrix}p_{i+1}\\q_{i+1}\end{bmatrix}=\begin{bmatrix}p_i&p_{i-1}\\q_i&q_{i-1}\end{bmatrix}\begin{bmatrix}a_{i}\\1\end{bmatrix}$$
</p>

显然，渐近分数列的奇数项小于原值，偶数项大于原值。

# 二、丢番图方程简介


[丢番图方程](http://zh.wikipedia.org/wiki/%E4%B8%9F%E7%95%AA%E5%9C%96%E6%96%B9%E7%A8%8B) 又名整系数多项式方程，其变量与系数均为整数。若一个丢番图方程具有以下的形式：

$$x^2 - ny^2= 1,\,\,\,x,y \in \mathbb{Z},\,n \in \mathbb{N}^+$$

则称此二元二次不定方程为佩尔方程。

## 1、佩尔方程的解

- 若 $n$ 是完全平方数，佩尔方程只有平凡解 $(\pm 1, 0)$。
- 对于其余情况，拉格朗日证明了佩尔方程总有非平凡解，而这些解可由 $\sqrt{n}$ 的连分数求出。

设 $\\{\frac{p_i}{q_i}\\}$ 是 $\sqrt{n}$ 的的渐近分数列，则存在 $i$ 使得 $(p_i,q_i)$ 为佩尔方程的解。取 $\min i$ 对应的 $(p_i,q_i)$ 作为佩尔方程的基本解（最小解），记作$(x_1,y_1)$，则全部的非平凡解解 $\\{x,y\\}$ 可表示为 $x_i + y_i\sqrt n = (x_1 + y_1\sqrt n)^i$，或由递推关系式求得：

<p>
$$\begin{bmatrix}x_{i+1}\\y_{i+1}\end{bmatrix}=\begin{bmatrix}x_1&ny_1\\y_1&x_1\end{bmatrix}\begin{bmatrix}x_{i}\\y_{i}\end{bmatrix}$$
</p>

规律：记 $\sqrt{n}$ 的连分数循环节长度为 $l$。当 $l$ 为偶数，$(p_l,q_l)$ 即是基本解；当 $l$ 为奇数，$(p_{2l},q_{2l})$ 即是基本解。

##### Example：求 $x^2 - 7y^2= 1$ 的解

由 $\sqrt{7}$ 的渐近分数列 $\\{\frac{p_i}{q_i}\\}=\frac{2}{1},\frac{3}{1},\frac{5}{2},\frac{8}{3},\cdots$，求得 $x^2 - 7y^2= 1$ 的基本解 $(8,3)$，其所有非平凡解 

$$\{(x,y)\}=\{(8,3),(127,48),(2024,765),(32257,12192),\cdots\}$$

## 2、Diophantine Equation[^ProjectEuler]

[^ProjectEuler]: [Project Euler：Diophantine Equation](https://projecteuler.net/problem=66)

题意：求最小的非完全平方数 $n\in(1,1000]$ 使佩尔方程 $x^2 - ny^2= 1$ 的基本解 $x_1$ 最大。

```python
from math import *
def iqj(i0,q0,j0,d):
	i = j0
	q = (d - j0*j0)//q0
	max_num = j0 + floor(sqrt(d))
	j = max([x for x in range(max_num,0,-1) if x % q == 0]) - j0
	a = (i + j)//q
	return i,q,j,a
def pell (d,h,k):
	if h*h - d*k*k == 1:	return True
	else:		        return False 
def frac(d):
	i0 = 0
	q0 = 1
	j0 = floor(sqrt(d))
	a0 = (i0 + j0)//q0
	h0 = a0
	k0 = 1
	if pell(d,h0,k0):	return h0
	else:
		i0,q0,j0,a1=iqj(i0,q0,j0,d)
		h1 = a1*a0 + 1
		k1 = a1
		while(not pell(d,h1,k1)):
			i0,q0,j0,a=iqj(i0,q0,j0,d)
			h = a*h1 + h0
			k = a*k1 + k0
			h0,k0 = h1,k1
			h1,k1 = h,k
		return h1
mh = 0
ans = 0
for d in [i+1 for i in range(1000) if sqrt(i+1)!=int(sqrt(i+1))]:
	h = frac(d)
	if h > mh:
		mh = h
		ans = d
print(ans)
```
---

```python
661
```

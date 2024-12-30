# Chapter 1: Brief History

Definition:
-----------

Calculus, originally called infinitesimal calculus, is a mathematical discipline focused on limits, continuity, derivatives, integrals, and infinite series. 

Before Calculus
---------------

Before Calculus even existed, people deal with infinite problems with **Method of Exhaustion** which is basically using the idea of **convergent infinite sequence**. The classic issue is finding the area of a circle by Archimedes. Archimedes used the Method of Exhaustion to approximate the area of a circle by inscribing and circumscribing polygons with an increasing number of sides within the circle. By calculating the area of these polygons, Archimedes was able to create upper and lower bounds for the area of the circle. As the number of sides of the polygons increased, these bounds converged to the exact area, ultimately leading him to deduce that the area of a circle is $\pi r^{2}$.

After the decline of ancient Greek civilization, Europe entered the Dark Ages. The spark of Greek civilization was preserved and studied by the Arabs. Alhazen (965 AD - 1039 AD) was an outstanding mathematician and physicist of the ancient Arab era. He delved into a vast array of ancient Greek mathematics, including infinite sequences and series, as well as the summation of powers of natural numbers. By combining geometry and algebra, he successfully derived and explained the summation formulas of powers of natural numbers in an intuitive geometric manner. 

Let's first consider the summation $\sum_{i=1}^{n}{i^k}$ where k is only for natural number. When the k=1, the summation is $1+2+3+4+...$, Alhazen invoke geometry area to imagine and calculate the algebraic summation like below: 

<p align="center">
  <img src="./images/calculusNotes_figure_1.svg"/>
</p>

Figure_1

As you can see That the total area is

```math
n(n+1) = \sum_{i=1}^{n}{i} + \sum_{i=1}^{n}{i} 
```

and so 

```math
\sum_{i=1}^{n}{i} = {n(n+1) \over 2} = {1 \over 2}n^2 + {1 \over 2}n
```

let's move on and take $k=2$, the image is like below

<p align="center">
  <img src="./images/calculusNotes_figure_2.svg"/>
</p>

Figure_2


The total area is

```math
\left( \sum_{i=1}^{n}{i} \right) \left( n+1 \right) = \sum_{i=1}^{n}{i^2} + \sum_{i=1}^{n}{ \left( \sum_{k=1}^{i}{k} \right) }
```

And we want to find $\sum_{i=1}^{n}{i^2}$, so we can do

```math
\left( {1 \over 2} n^2 + {1 \over 2} n \right) \left( n+1 \right) = \sum_{i=1}^{n}{i^2} + \sum_{i=1}^{n}{ \left( {1 \over 2} i^2 + {1 \over 2} i \right) }
```
```math
{1 \over 2} n^3 + n^2 + {1 \over 2} n = \sum_{i=1}^{n}{i^2} + {1 \over 2} \sum_{i=1}^{n}{i^2} + {1 \over 2} \left( {1 \over 2} n^2 + {1 \over 2} n \right)
```
```math
{1 \over 2} n^3 + {3 \over 4} n^2 + {1 \over 4} n = {3 \over 2} \sum_{i=1}^{n}{i^2}
```

and so

```math
\sum_{i=1}^{n}{i^2} = {1 \over 3} n^3 + {1 \over 2} n^2 + {1 \over 6} n

```

let's move on and take $k=3$, the image is like below

<p align="center">
  <img src="./images/calculusNotes_figure_1.svg"/>
</p>

Figure_3


At this point, we can find the pattern, and the total area is

```math
\left( \sum_{i=1}^{n}{i^2} \right) { \left( n+1 \right) } = \sum_{i=1}^{n} \left( \sum_{k=1}^{i}{k^2} \right)
```

We want to find $\sum_{i=1}^{n}{i^3}$, and so do

```math
\left( {1 \over 3} n^3 + {1 \over 2} n^2 + {1 \over 6} n \right) \left( n+1 \right) = \sum_{i=1}^{n}{i^3} + \sum_{i=1}^{n}{\left( {1 \over 3} i^3 + {1 \over 2} i^2 + {1 \over 6}i \right) }
```
```math
{1 \over 3}n^4+{5 \over 6}n^3+{4 \over 6}n^2+{1 \over 6}n = \sum_{i=1}^{n}{i^3} + {1 \over 3} \sum_{i=1}^{n}{i^3} + {1 \over 2} \left( {1 \over 3}n^3 + {1 \over 2}n^2 + {1 \over 6}n \right) + {1 \over 6} \left( {1 \over 2}n^2 + {1 \over 2}n \right)
```
```math
{1 \over 3}n^4 + {4 \over 6}n^3 + {4 \over 12}n^2 = {4 \over 3} \sum_{i=1}^{n}{i^3}
```

And so

```math
\sum_{i=1}^{n}{i^3} = {1 \over 4}n^4 + {1 \over 2}n^3 + {1 \over 4}n^2
```

The summation of $k=4, 5, 6...$ is using the same idea. It's easy to find the summation pattern:

```math
\sum_{i=1}^{n}{i} = {n(n+1) \over 2} = {1 \over 2}n^2 + {1 \over 2}n
```
```math
\sum_{i=1}^{n}{i^2} = {1 \over 3} n^3 + {1 \over 2} n^2 + {1 \over 6} n

```
```math
\sum_{i=1}^{n}{i^3} = {1 \over 4}n^4 + {1 \over 2}n^3 + {1 \over 4}n^2
```
```math
\sum_{i=1}^{n}{i^4} = {1 \over 5}n^5 + {1 \over 2}n^4 + {1 \over 3}n^3 - {1 \over 30}n
```

The pattern is the coefficient of first term(highest power term) of the summation is ${1 \over (k+1)}$


In 1656, John Wallis published his Arithemtica infinitorum, in which he displayed many ideas that were to lead to the integral calculus of Newton, including the famous **Wallis Product** which gives below (check 
[reference1: a paper talks about this](https://www.jstor.org/stable/25759727?seq=1) 
[reference2: Mathematitcal_Intention_Wallis, another paper talks about this](https://www.quadrivium.info/GGB/WallisTable.html) 
[reference3: a discussion talk about the prove of generalized binomial theorem](https://www.reddit.com/r/math/comments/8vv21s/how_do_you_prove_the_binomial_theorem_for_all/)

```math
{2 \over \pi} = {{1 \cdot 3} \over {2 \cdot 2}} \cdot {{3 \cdot 5} \over {4 \cdot 4}} \cdot {{5 \cdot 7} \over {6 \cdot 6}} \cdot...
```

Earlier in 1593, Vieta found another infinite product which gives $\pi$

```math
{2 \over \pi} = \sqrt{1 \over 2} \cdot \sqrt{{1 \over 2}+{1 \over 2} \cdot \sqrt{1 \over 2}} \cdot \sqrt{{1 \over 2}+{1 \over 2} \cdot {\sqrt{{1 \over 2}+{1 \over 2} \cdot \sqrt{1 \over 2}}}}... 
```

But, since Wallis doesn't mention it, we suppose that he was unaware of it.(Remarkably, these two seemingly different products are special cases of a more general formula (3).) The thoughts that lead Wallis to (1) are quite surprising and ingeious. It is the purpose of this paper to show to modern readers the brilliance of Wallis' thinking in his disocvery of (1)

How Calculus created?
---------------------

One thing to keep in mind is that Calculus is nothing more than an updated version of the Method of Exhuastion, but now it specifically deal with **Functions**. People have played algebra, geometry, and arithmetic for a long time. In 17th centuries, science was born and started to join the game. Many math problems were being researched again, like finding area of a shape, finding the length of curve or volume of some solid body. Most of them were written in algebraic expressions and equations. So a problem may like this in that time: How do we computer the area under a unit circle curve which is express as $\sqrt{1-x^2}$ under first quadrant of cartesian coordinates? We can use the Method of Exhaustion, take n number of small rectangles under the curve, and when n increases the more accurate the area we computer.   The term "Function" is created by Lebniz in 1694

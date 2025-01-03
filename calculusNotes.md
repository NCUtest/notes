# Chapter 1: Brief History

Definition:
-----------

Calculus, originally called infinitesimal calculus, is a mathematical discipline focused on limits, continuity, derivatives, integrals, and infinite series. 

Ancient Age
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
  <img src="./images/calculusNotes_figure_3.svg"/>
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

The summation of $k=4, 5, 6...$ is using the same idea. There's an obvious pattern if we list all the summations below

```math
\sum_{i=1}^{n}{i} = {1 \over 2}n^2 + {1 \over 2}n
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
```math
\text{...}
```

The empirical pattern reveals that the coefficient of first term(the highest power term) of those summations are always ${1 \over (k+1)}$. By the way, since we use "geometric" perspective to visualize the summation of integer power, there's another intuitive way to imagine the summation
  * For $k=1$, we are actually adding up the area of $1 \cdot n$ 2 dimensional rectangle.

<p align="center">
  <img src="./images/calculusNotes_figure_4.svg"/>
  <span style="background-color: grey; color: white; padding: 2px 5px;">Figure_4</span>
</p>

Figure_4


  * For $k=2$, we are actually adding up the volume of $1 \cdot n^2$ 3 dimensional volumes

<p align="center">
  <img src="./images/calculusNotes_figure_5.svg"/>
</p>

Figure_5


  * For $k=3$, we are actually adding up the $1 \cdot n^3$ 4 dimension hypervolume.(Not possible to draw)

Age of Renaissance
------------------ 

Time flies, and in the blink of an eye, 6 hundred years have passed. In 1656, during the late Renaissance, John Wallis, an important professor of mathematics and physics at the University of Oxford in England, referred to Alhazen's research and made many extensions.

First, he used Cartesian coordinates to reformulate the geometric description of the sum of natural numbers raised to k-th power. He transfomed $\sum_{i=1}^{n}{i^k}$ into $y=x^k$. When n becomes sufficiently large, the area under the curve $y=x^k$ should closely approximates the sum $\sum_{i=1}^{n}{i^k}$.

It should be stressed here that results about areas and volumes were not given as
formulas but always as ratios. This is true about nearly all such mathematical results
until the end of the seventeenth century. For example the area of a triangle is one half
of the area of the parallelogram that contains it. The volume of a pyramid is one third
of the box that contains it. The area of a piece of a parabola is two thirds of the
rectangle that contains it. The area of the circle is π/4 of the square that contains it.
These examples were all known by the second century BC. Alhazen and Wallis's works followed the same tradition, but within a new way.


<p align="center">
  <img src="./images/calculusNotes_figure_6.svg"/>
</p>

Figure_6

As Figure_6 shows, Wallis He selected a point on the curve $y=x^k$. The area of the rectangle which is defined as 1 formed by this point and the x- and y-axes, to the area under the curve and enclosed by the x- and y-axes.

If we cut the area under the curve into pieces of infinite small line segments, the summation of all the segments should follows the Alhazen's result too because there are infinite large terms. We've already known the result of Alhazen's summation $\sum_{i=1}^{n}{i^k}$. When $n$ is large enough, the summation should be lead by the first term which is ${1 \over (k+1)}$. So, obviously, when the area of rectangle is defined by 1, the ratio $\rho = {1 \over (1+k)}$ when n is large enough.

This is true for every **integer** point on the curve we choose, you can easily prove that. 

Wallis keeped move on, he tried to figure out if $\rho = {1 \over (1+k)}$ still keeps true when $k$ is not just integer but all real number.

First, He knew that when $k={1 \over 2}, {1 \over 3}, {1 \over 4}...$ then $\rho={1 \over (k+1)}$ keeps true. Because, for example $y = x^{1 \over 2}$ is just complementary to $y = x^2$. Actually if we rewrite $y=x^2$ as $y^{1 \over 2}=x$, then thing would be clear like the Figure_7 shows below. 

<p align="center">
  <img src="./images/calculusNotes_figure_7.svg"/>
</p>

Figure_7

The area cover by $y^{1 \over k}=x$ should be 
```math
1-{1 \over {k+1}} = {1 \over {{1 \over k}+1}}
```

Wallis doesn't prove that $\rho={1 \over {k+1}}$ remains true for any real number $k$. He only provide the reasoning for inverse integers $1 \over k$ like above and then doing some empirical tests for some real number $k$ to be more confident to believe that the pattern can be used in every real number $k$. (However, I think the idea of "continuity" may work to provide a proof.) 

One of the tests is finding the ratio of area under the curve of a circle curve which is $y=\sqrt{r^2-x^2}$ in first quadrant of cartesian coordinates. 

<p align="center">
  <img src="./images/calculusNotes_figure_8.svg"/>
</p>

Figure_8

Of course, Wallis knew that the ratio is $\pi \over 4$, he wanted to check if his theory(or in modern sense, a hypothesis) is correct in this case. However, $y=\sqrt{r^2-x^2}=(r^2-x^2)^{1 \over 2}$ is can't be directly expand because he knew nothing about any of **general binomial theorem** to expand fraction power like $(a+b)^{1 \over 2}$. So, he use his so called **interpolation** theorem to guess the answer.

First he defined the general form $y=\left( r^{1 \over q} + x^{1 \over q} \right)^p$. And find all the ration when p and q are integers number. You can expand the expression and use the theory $\rho={1 \over (k+1)}$ to do that. Eventually, you would get the table like Figure_9 below

<p align="center">
  <img src="./images/calculusNotes_figure_9.svg"/>
</p>

Figure_9


At this point Wallis temporarily abandoned both the geometric and algebraic representations and began to work solely in the table representation. The question then became, how does one interpolate the missing values in this table? His interpolate idea is based on that he trust the same pattern a row has should be follow by the missing value on that row. Figure_10 is the pattern he found:

<p align="center">
  <img src="./images/calculusNotes_figure_10.svg"/>
</p>

Figure_10


Expand the fraction numbers, we get the result of Figure_11

<p align="center">
  <img src="./images/calculusNotes_figure_11.svg"/>
</p>

Figure_11

Now if we denote the ratio when $p={1 \over 2}$ and $q={1 \over 2}$ as $\Omega$, a reasonable pattern should be as Figure_12 shows below:

<p align="center">
  <img src="./images/calculusNotes_figure_12.svg"/>
</p>

Figure_12


Wallis argued that when $p={1 \over 2}$, $q={q \over 2}$, the odd terms of that row should be $\frac{1 \cdot 3 \cdot 5 \cdot 7...n}{2 \cdot 4 \cdot 6 \cdot 8...\left( n-1 \right) }$. The ratio of n terms and n-2 terms in the row
```math
\frac{\frac{3 \cdot 5 \cdot 7 \cdot 9 \cdot ...n}{2 \cdot 4 \cdot 6 \cdot 8 \cdot \left( n-1 \right)}}{\frac{3 \cdot 5 \cdot 7 \cdot 9 \cdot ... \left( n-2 \right) }{2 \cdot 4 \cdot 6 \cdot 8 \cdots ... \left( n-3 \right)}} = \frac{n}{ \left( n-1 \right) } \approx 1
```
And we know that even terms is between odd terms, the value should be in between. This means the even terms would get closer to odd terms when n grows larger. So we can conclude that

```math
\Omega \cdot \frac{4 \cdot 6 \cdot 8 \cdot 10...}{3 \cdot 5 \cdot 7 \cdot 9...} \approx \frac{3 \cdot 5 \cdot 7 \cdot 9...}{2 \cdot 4 \cdot 6 \cdot 8...}
```

And then we can get

```math
\Omega \approx \frac{3 \cdot 3 \cdot 5 \cdot 5 \cdot 7 \cdot 7 \cdot 9 \cdot 9...}{2 \cdot 4 \cdot 4 \cdot 6 \cdot 6 \cdot 8 \cdot 8 \cdot 10...}
```

And we know that $\Omega={4 \over \pi}$, so we can express $\pi$ as
```math
\pi \approx 2 \cdot \frac{2 \cdot 2 \cdot 4 \cdot 4 \cdot 4 \cdot 6 \cdot 6 \cdot 8 \cdot 8...}{1 \cdot 3 \cdot 3 \cdot 5 \cdot 5 \cdot 7 \cdot 7 \cdot 9...}
```

This is the famous **Wallis Product**.

Earlier in 1593, Vieta found another infinite product which gives $\pi$

```math
{2 \over \pi} = \sqrt{1 \over 2} \cdot \sqrt{{1 \over 2}+{1 \over 2} \cdot \sqrt{1 \over 2}} \cdot \sqrt{{1 \over 2}+{1 \over 2} \cdot {\sqrt{{1 \over 2}+{1 \over 2} \cdot \sqrt{1 \over 2}}}}... 
```

But, since Wallis doesn't mention it, we suppose that he was unaware of it.(Remarkably, these two seemingly different products are special cases of a more general formula(not gonna talk in this moment).

Newton's general binomial theorem
---------------------
In 1676, Gottfried Wilhelm Leibniz inquired with Isaac Newton about the discovery process of the general binomial theorem. On June 13th, Newton responded through Henry Oldenburg, the Secretary of the Royal Society. In his letter, Newton wrote the following infinite series, referring to it as a theorem:

```math
(P+PQ){m/n}=P{m/n}+\frac{m}{n}AQ+\frac{m-n}{2n}BQ+\frac{m-2n}{3n}CQ+\frac{m-3n}{4n}DQ+\cdots
```
Newton explained that $P+PQ$ is the binomial considered, where P is the first term and $Q$ is the remaining term divided by $P$. The ratio $m \over n$ can be integer or a fraction, positive or negative. He provided an example for $\left( a^3+bbx \right)^{-2 \over 3}$, $P=a^3$, $Q={bbx \over a^3}$, $m=-2$ and $n=3$. On the right side of the equation, A represents the first term $P^{m \over n}$, B represents the second term ${m \over n} AQ$, and so on. In other words, $\left( P+PQ \right)^{m \over n} = A + B + C + D + ... $. From a modern perspective, Newton's formula might seem obscure and complex. Why does $P$ appear twice? Why not write $P+PQ$ as $P+Q$? Moreover, why not expand the terms on the right side of the equatoin and list the explicit expressions for $A$, $B$, $C$ and $D$? The reason is that Newton aimed to simplify the calculations, which will be explained later. Our first discussion is Leibniz's question: how did Newton arrive at this formula?

After receiving the letter, Leibniz expressed a desire for more detailed information. Consequently, on October 24th of the same year, Newton sent a second letter. In it, he explained how he was inspired by John Wallis's method of interpolation to derive the appropriate formula, even revealing that he had known about the method since he was a student at Cambridge University, 12 years prior. The precursor to Newton's discovery of the binomial theorem was the problem of calculating the value of $\pi$. Considering the area of the first quadrant of a unit circle $x^2+y^2=1$

, the calculation is as follows:

```math
\displaystyle \frac{\pi}{4}=\int_0^1\sqrt{1-x^2}dx
```

Newton's challenge was to represent $\left( 1-x^2 \right)^{1 \over 2}$ as an infinite series. Following in Wallis's footsteps, he examined the simpler expansion of $\left( 1+x \right)^r$. When $r$ is integer, the first few terms are:

```math
\left( 1+x \right)^0 = 1 + 0 \cdot x + 0 \cdot x^2 + 0 \cdot x^3 + 0 \cdot x^4 + 0 \cdot x^5 + ...
```
```math
\left( 1+x \right)^1 = 1 + 1 \cdot x + 0 \cdot x^2 + 0 \cdot x^3 + 0 \cdot x^4 + 0 \cdot x^5 + ...
```
```math
\left( 1+x \right)^2 = 1 + 2 \cdot x + 1 \cdot x^2 + 0 \cdot x^3 + 0 \cdot x^4 + 0 \cdot x^5 + ...
```
```math
\left( 1+x \right)^3 = 1 + 3 \cdot x + 3 \cdot x^2 + 1 \cdot x^3 + 0 \cdot x^4 + 0 \cdot x^5 + ...
```
```math
\left( 1+x \right)^4 = 1 + 4 \cdot x + 6 \cdot x^2 + 4 \cdot x^3 + 1 \cdot x^4 + 0 \cdot x^5 + ...
```
```math
\left( 1+x \right)^5 = 1 + 5 \cdot x + 10 \cdot x^2 + 10 \cdot x^3 + 5 \cdot x^4 + 1 \cdot x^5 + ...
```
```math
\vdots
```

Now implement the method of interpolation of Wallis. Newton write the table like Figure_13 below

<p align="center">
  <img src="./images/calculusNotes_figure_13.svg"/>
</p>

Figure_13


Of course, every row, you can see they are all $C^n_m$ which is combination problem. It's easy to prove that integer binomial theorem by induction. Newton put attention into the pattern of the column which should provide the value of non-integer $r$ power. The pattern of first colume is $1$. The pattern of second colume is $s$. The pattern of third column is the formula of arithmetic series $s {\left( s+1 \right) } \over 2$. So Newton got Figure_14 below:

<p align="center">
  <img src="./images/calculusNotes_figure_14.svg"/>
</p>

Figure_14


Like most mathematicians, Newton believed that the fundamental forms of mathematics are omnipresent. Since the constant term is 1, the coefficient of the $x$ term is $r$, and the coefficient of the $x^2$ term is ${r \left( r-1 \right)} \over 2$, the coefficient of the $x^3$ term should be $r {\left( r-1 \right) \left( r-2 \right)} \over c$. Substituting $r=3$, we get $3 \cdot 2 \cdot 1 \cdot {1 \over c} = 1$, thus c = 6. Similar reasoning can continue, giving the coefficient of $x^4$ term in $\left( 1+x \right)^r$ as ${r \left( r-1 \right) \left( r-2 \right) \left( r-3 \right)} \over {4!}$, and the coefficient of $x^5$ term as ${r \left( r-1 \right) \left( r-2 \right) \left( r-3 \right) \left( r-4 \right) } \over {5!}$. With all the formula, Newton' complete the table Figure_15 below:

<p align="center">
  <img src="./images/calculusNotes_figure_15.svg"/>
</p>

Figure_15

At this point, we can conclude

```math
\displaystyle  (1+x)^r=1+rx+\frac{r(r-1)}{2!}x^2+\frac{r(r-1)(r-2)}{3!}x^3+\cdots
```
if $r$ is real number, k is integer, define binomial coefficient:


```math
\displaystyle  \binom{r}{0}=1,~~\binom{r}{k}=\frac{r(r-1)\cdots(r-k+1)}{k!},~~k\ge 1
```

which can be express by binomial coefficients:

```math
\displaystyle  (1+x)^r=\binom{r}{0}+\binom{r}{1}x+\binom{r}{2}x^2+\binom{r}{3}x^3+\cdots
```
This is the general binomial theorem for $r\in R$.

However, Newton didn't provide any proof of this just like Wallis didn't provide any proof of his interpolation method. All the arguments above are empirical, which means not stricly valid in sense of Euclidean process. But Newton did provide a lot of example to gain the confidence that the theory works.

Most importantly, with general binomial theorem, we can use it to find any derivative of any function that can be expressed as $f(x) = x^r$, for $r\in R$. 

```math
f\left( x+dx \right)^r - f\left( x \right) \over dx = {\left( x + dx \right)^r - x^r} \over dx = \displaystyle  (x+dx)^r=\binom{r}{0}x^r dx^0+\binom{r}{1}x^{r-1} dx^1+\binom{r}{2}x^{r-2} dx^2+\binom{r}{3}x^{r-3} dx^3+\cdots
```





One thing to keep in mind is that Calculus is nothing more than an updated version of the Method of Exhuastion, but now it specifically deal with **Functions**. People have played algebra, geometry, and arithmetic for a long time. In 17th centuries, science was born and started to join the game. Many math problems were being researched again, like finding area of a shape, finding the length of curve or volume of some solid body. Most of them were written in algebraic expressions and equations. So a problem may like this in that time: How do we computer the area under a unit circle curve which is express as $\sqrt{1-x^2}$ under first quadrant of cartesian coordinates? We can use the Method of Exhaustion, take n number of small rectangles under the curve, and when n increases the more accurate the area we computer.   The term "Function" is created by Lebniz in 1694


Reference:
----------
[Wallis Table](https://www.quadrivium.info/GGB/WallisTable.html)
[Proof of Binomial theorem](https://www.quadrivium.info/GGB/WallisTable.html)


### A Pluto.jl notebook ###
# v0.11.10

using Markdown
using InteractiveUtils

# ╔═╡ 6ef30220-7474-11eb-3d80-e9149a026851
md"""
``\large y = mx + c``

The equation given is the equation for a straight line. 
- **m** -> slope
- **c** -> y-intercept
- **x** -> x-coordinate.

#### **Points to be noted**
1. Slope is same everywhere on a line
2. Two parellel lines have the same slope
3. Intersecting lines have different slopes

### General form of the equation of a straight line

`` \large ax + by + c = 0 ``

Rearranging to get it into the slope - intercept form gives:

`` \large y = \frac{-c-ax}{b} = \frac{-a}{b}x + \frac{-c}{b} ``

Here, m = `` \Large \frac{-a}{b} `` & `` c = \Large \frac{-c}{b} ``

If we generalize the equation to *n* dimensions

`` \large w_1x_1 + w_2x_2 + \dots + w_0 = 0 ``

`` \large x_1, x_2, \dots ``

`` \large w_1, w_2, \dots ``

# Equation of a plane 

`` \large \pi : ax + by + cz + d = 0 ``

`` \large L: ax + by + c = 0 ``

`` \large \pi `` is used to represent plane 

We can also write it as a more general notation:

`` \large \pi : w_1x_1 + w_2x_2 + w_3x_3 + w_0 = 0 ``


# Equation of a hyperplane

When the number of dimensions is greater than 2, then we call it **hyper-plane**
It is represented by: `` \large \pi_d ``

It's equation is:

`` \large \pi_d : w_1x_1 + w_2x_2 + \dots + w_dx_d + w_0= 0 ``

### Vectors in Linear Algebra

Below picture is what a vector is. It has a magnitude and a direction. 

The magnitude of the above vector is calculated by: 
$\large ||\vec u|| = \sqrt{a^2 + b^2}$. This is a **2-d** vector. 

For a **'d'** dimensional vector the formula is generalized to:
$\large ||\vec x|| = \sqrt{x_1^2 + x_2^2 + \dots + x_d^2}$

The equation of a hyperplane: 
$\large \pi_d : w_1x_1 + w_2x_2 + \dots + w_dx_d + w_0= 0$
 
can be rewritten in a matrix form using Linear algebra: 

``\large \begin{bmatrix} w_1   \dots  w_d \end{bmatrix}``
``\begin{bmatrix} x_1 \\ \vdots \\ x_d \\ \end{bmatrix} + w_0 = 0``

``\large W \in R^d``, which means **W** is a d-dimensional vector and all it's values are real numbers. ``\large w_0`` is a scalar. 

The Vector with all ``\large w`` 
s is a row vector & the vector with all ``\large x`` s is a column vector
In maths, when we say vector we mean a **column vector** by convention

We can write this in a more concise way: 
``\large W^Tx + w_0 = 0``
"""

# ╔═╡ 39ad87a0-75bb-11eb-0dc8-43e6c44eea06
begin
	import Images
	import ImageView
end

# ╔═╡ 0a0e2fb0-75be-11eb-0f35-879a7f474dd9
image = Images.load(raw"C:\Users\Abhishek Swain\Desktop\PGD_UOH\imgs\vector_mag.png")

# ╔═╡ 4c0a10e0-75c4-11eb-298c-634317c01b11
md"""
# Dataset
"""

# ╔═╡ 6927ade0-75c4-11eb-3ef8-ff7b2740b6ec


# ╔═╡ Cell order:
# ╟─6ef30220-7474-11eb-3d80-e9149a026851
# ╟─39ad87a0-75bb-11eb-0dc8-43e6c44eea06
# ╟─0a0e2fb0-75be-11eb-0f35-879a7f474dd9
# ╟─4c0a10e0-75c4-11eb-298c-634317c01b11
# ╠═6927ade0-75c4-11eb-3ef8-ff7b2740b6ec

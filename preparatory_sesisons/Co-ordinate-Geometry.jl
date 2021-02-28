### A Pluto.jl notebook ###
# v0.11.10

using Markdown
using InteractiveUtils

# ╔═╡ 7c389200-75d8-11eb-3a2f-f98cec9dc98e
begin
	import Images
	import ImageView
	using Plots
	using DataFrames
	using CSV
end

# ╔═╡ 110b84e0-75da-11eb-293f-637fab69d59e
md"""
# Equation of a straight line
"""

# ╔═╡ 617d9d20-75d8-11eb-04f4-094c7d702bfa
function plot_line()
	x = -5:5
	y = -5:5
	plot(x, y)
end;

# ╔═╡ e7fff870-75d8-11eb-0f1f-d325ea2f777a
plot_line()

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
``\large ||\vec u|| = \sqrt{a^2 + b^2}``. This is a **2-d** vector. 

For a **'d'** dimensional vector the formula is generalized to:
``\large ||\vec x|| = \sqrt{x_1^2 + x_2^2 + \dots + x_d^2}``

The equation of a hyperplane: 
``\large \pi_d : w_1x_1 + w_2x_2 + \dots + w_dx_d + w_0= 0``
 
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

# ╔═╡ 0a0e2fb0-75be-11eb-0f35-879a7f474dd9
Images.load(raw"C:\Users\Abhishek Swain\Desktop\PGD_UOH\imgs\vector_mag.png")

# ╔═╡ 4c0a10e0-75c4-11eb-298c-634317c01b11
md"""
# Dataset
"""

# ╔═╡ 12e05702-75fd-11eb-3add-d795a7c95701
begin
	file = raw"C:\Users\Abhishek Swain\Desktop\PGD_UOH\datasets\iris.csv"
	df = CSV.File(file) |> DataFrame
	df[1:5, 1:5]
end

# ╔═╡ ee8918f0-75fd-11eb-0fe8-65686cde5245
md"""
The above is the example of a dataset. This one is the famous Iris dataset.Iris dataset contains 4 features(*SepalLengthCm,	SepalWidthCm, PetalLengthCm, PetalWidthCm*) and a target(3 types of flowers) \
Each row has 4 columns representing the features and the last column is the target(the thing we want to predict)

We can have a concise mathematical representation of a dataset as:

``\large D = \{(x_i, y_i); x_i \in R^d, y_i \in {c_1, c_2}\}``

``\large x_i`` represents ``i^{th}`` feature vector \
``\large y_i`` represents ``i^{th}`` target vector

# Angle between Vectors
"""

# ╔═╡ 4fcdcdd0-75ff-11eb-0399-cb9584a88a31
Images.load(raw"C:\Users\Abhishek Swain\Desktop\PGD_UOH\imgs\Angle-Between-Two-Vectors.png")

# ╔═╡ a1c0a7c0-75ff-11eb-2737-ebd55bea7c9a
md"""
Here we need the notion of a dot product. This is taken from *Wikipedia*

> In mathematics, the dot product or scalar product is an algebraic operation that takes two equal-length sequences of numbers (usually coordinate vectors), and returns a single number. In Euclidean geometry, the dot product of the Cartesian coordinates of two vectors is widely used. It is often called "the" inner product (or rarely projection product) of Euclidean space, even though it is not the only inner product that can be defined on Euclidean space (see Inner product space for more). \
Algebraically, the dot product is the sum of the products of the corresponding entries of the two sequences of numbers. Geometrically, it is the product of the Euclidean magnitudes of the two vectors and the cosine of the angle between them.

From the last line of the definition, 

``\large \vec A \cdot \vec B = |\vec A||\vec B|\cos \theta = \vec A ^ T \vec B``

After rearranging, 

``\Large \theta = \cos ^ {-1} \left ( \frac{\vec A \cdot \vec B}{|\vec A||\vec B|} \right )``

If ``\large \theta`` is 0 then, vectors are perpendicular  

## Special cases of equation of a plane

One more concept we need is the concept of a unit vector. A unit vector is a vector whose magnitude is 1. Represented by ``\large \hat x `` called the **"hat"** symbol.

### 1. Passing through origin 

Equation recap: 
``\large \pi : w_1x_1 + w_2x_2 + w_3x_3 + w_0 = 0``

for the plane to pass through origin, ``\large x_1, x_2, x_3 = 0``. Plugging these values in the equation we have: ``w_0 = 0``. This is the equation of plane passing through origin 

### 2. Not passing through origin 

"""

# ╔═╡ 289c94c0-7600-11eb-3106-a5dc783e3e2d
Images.load(raw"C:\Users\Abhishek Swain\Desktop\PGD_UOH\imgs\plane-not-through-origin.jpg")

# ╔═╡ 46614730-7600-11eb-1d05-b1303c16f6ce
md"""
Equation of plane in vector form:

`` \large w^Tx + w_0 = 0 `` \
`` \large => ||w||||x||\cos\theta = 0 `` \
`` \large => ||x||\cos\theta + w_0 = 0 `` (as ``\large w`` is a unit vector)   
`` \large ||x||\cos\theta = a `` (from the figure)  

So, finally ``\large a = -w_0``  

As you can see, ``\large a`` is the distance of the plane from the origin. So, what we see is the distance of a plane not passing through origin is ``\large |w_0|`` provided ``\large w`` is a unit vector.  

if ``\large w`` is not a unit vector then ``\large a = \frac{|w_0|}{||w||}`` 

We can prove it like this: \
``\large w \cdot x + w_0 = 0`` \
``\large => ||w||||x||\cos\theta + w_0 = 0 `` \
``\large => ||w|| a + w_0 = 0 ``, as ``\large ||x||\cos\theta = a`` (from the figure) \
``\large =>  a = \frac{-w_0}{||w||} ``

but ofcourse we can do away with the -ve sign as distance can't be negative. So,
``\large a = \frac{|w_0|}{||w||} ``
"""

# ╔═╡ Cell order:
# ╟─7c389200-75d8-11eb-3a2f-f98cec9dc98e
# ╟─110b84e0-75da-11eb-293f-637fab69d59e
# ╟─617d9d20-75d8-11eb-04f4-094c7d702bfa
# ╟─e7fff870-75d8-11eb-0f1f-d325ea2f777a
# ╟─6ef30220-7474-11eb-3d80-e9149a026851
# ╟─0a0e2fb0-75be-11eb-0f35-879a7f474dd9
# ╟─4c0a10e0-75c4-11eb-298c-634317c01b11
# ╟─12e05702-75fd-11eb-3add-d795a7c95701
# ╠═ee8918f0-75fd-11eb-0fe8-65686cde5245
# ╟─4fcdcdd0-75ff-11eb-0399-cb9584a88a31
# ╟─a1c0a7c0-75ff-11eb-2737-ebd55bea7c9a
# ╟─289c94c0-7600-11eb-3106-a5dc783e3e2d
# ╟─46614730-7600-11eb-1d05-b1303c16f6ce

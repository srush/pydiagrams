<p align="center"><img src="https://raw.githubusercontent.com/danoneata/chalk/master/examples/output/logo-sm.png" width=300></p>

Chalk is a declarative drawing library built on top of [PyCairo](https://pycairo.readthedocs.io).
The API draws heavy inspiration from
Haskell's [diagrams](https://diagrams.github.io/),
Scala's [doodle](https://github.com/creativescala/doodle/) and
Jeremy Gibbons's lecture notes on [Functional Programming for Domain−Specific Languages](http://www.cs.ox.ac.uk/publications/publication7583-abstract.html).

⚠️ The library is still very much work in progress and subject to change.

## Installation

The library is available on PyPI as `chalk-diagrams` and can be installed with `pip`:

```bash
pip install chalk-diagrams
```

On Debian (or Colab) you will need to install Cairo

```bash
sudo apt-get install libcairo2-dev
```

If you want to use the LaTeX extension, run:

```bash
pip install chalk-diagrams[latex]
```

For the LaTeX extension you might need to install `pdf2svg` and `texlive`;
on Debian these dependencies can be installed as follows:

```bash
sudo apt-get install pdf2svg texlive texlive-science texlive-latex-recommended texlive-latex-extra
```

**Installation with Conda**

You can install the library with **conda** from `conda-forge` channel.

```powershell
conda install -c conda-forge chalk-diagrams
```

## Overview

Below we provide a brief introduction of the main functionality of the library.
These examples are available in the `examples/intro.py` file.

We start by importing the [`colour`](https://github.com/vaab/colour) module and the `diagrams` functions:

```python
from colour import Color
from chalk import *
```

We also define some colors that will be shortly used:

```python
papaya = Color("#ff9700")
blue = Color("#005FDB")
```

We can easily create basic shapes (the functions `circle`, `square`, `triangle`) and style them with various attributes (the methods`fill_color`, `line_color`, `line_width`).
For example:

```python
d = circle(1).fill_color(papaya)
```

![circle](https://raw.githubusercontent.com/danoneata/chalk/master/examples/output/intro-01.png)

The diagram can be saved to an image using the `render` method:

```python
d.render("examples/output/intro-01.png", height=64)
```

We can glue together two diagrams using the combinators `atop` (or `+`), `beside` (or `|`), `above` (or `/`).
For example:

```python
circle(0.5).fill_color(papaya) | square(1).fill_color(blue)
```

which is equivalent to

```python
circle(0.5).fill_color(papaya).beside(square(1).fill_color(blue))
```

This code produces the following image:

![atop](https://raw.githubusercontent.com/danoneata/chalk/master/examples/output/intro-02.png)

We also provide combinators for a list of diagrams:
`hcat` for horizontal composition, `vcat` for vertical composition.
For example:

```python
hcat(circle(0.1 * i) for i in range(1, 6)).fill_color(blue)
```
![hcat](https://raw.githubusercontent.com/danoneata/chalk/master/examples/output/intro-03.png)

We can use Python functions to build more intricate diagrams:

```python
def sierpinski(n: int, size: int) -> Diagram:
    if n <= 1:
        return triangle(size)
    else:
        smaller = sierpinski(n - 1, size / 2)
        return smaller.above(smaller.beside(smaller).center_xy())

d = sierpinski(5, 4).fill_color(papaya)
```

![sierpinski](https://raw.githubusercontent.com/danoneata/chalk/master/examples/output/intro-04.png)

### Gallery of examples

For more examples, please check the `examples` folder;
their output is illustrated below:

<table>
<tr>
<td align="center"><img src="doc/imgs/squares.png"><br><code><a href="https://github.com/danoneata/chalk/tree/master/examples/squares.py">squares.py</a></code></td>
<td align="center"><img src="doc/imgs/logo.png"><br><code><a href="https://github.com/danoneata/chalk/tree/master/examples/logo.py">logo.py</a></code></td>
<td align="center"><img src="doc/imgs/escher-square-limit.png"><br><code><a href="https://github.com/danoneata/chalk/tree/master/examples/escher_square.py">escher_square.py</a></code></td>
</tr>
<tr>
<td align="center"><img src="doc/imgs/hilbert.png"><br><code><a href="https://github.com/danoneata/chalk/tree/master/examples/hilbert.py">hilbert.py</a></code></td>
<td align="center"><img src="doc/imgs/koch.png"><br><code><a href="https://github.com/danoneata/chalk/tree/master/examples/koch.py">koch.py</a></code></td>
<td align="center"><img src="doc/imgs/hex-variation.png"><br><code><a href="https://github.com/danoneata/chalk/tree/master/examples/hex_variation.py">hex-variation.py</a></code></td>
</tr>
<tr>
<td align="center"><img src="doc/imgs/lenet.png"><br><code><a href="https://github.com/danoneata/chalk/tree/master/examples/lenet.py">lenet.py</a></code></td>
<td align="center"><img src="doc/imgs/tensor.png"><br><code><a href="https://github.com/danoneata/chalk/tree/master/examples/tensor.py">tensor.py</a></code></td>
<td align="center"><img src="doc/imgs/hanoi.png"><br><code><a href="https://github.com/danoneata/chalk/tree/master/examples/hanoi.py">hanoi.py</a></code></td>
</tr>
<!--<tr>
<td align="center"><img src="doc/imgs/latex.svg"><br><code><a href="https://github.com/danoneata/chalk/tree/master/examples/latex.py">latex.py</a></code></td>
</tr>
-->
</table>

These scripts can be run as follows:

```bash
python examples/squares.py
```

## Authors

- [Dan Oneață](http://doneata.bitbucket.io/)
- [Alexander Rush](http://rush-nlp.com/)

Special thanks to [Ionuț G. Stan](http://igstan.ro/) for providing many useful insights and comments!

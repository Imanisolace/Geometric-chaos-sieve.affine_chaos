# geometric-chaos-sieve.affine_chaos

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Imanisolace/Geometric-chaos-sieve.affine_chaos/blob/main/test_sieve.ipynb)

O(1) geometric filter for 3-body stability. True 3D with varying z.

## Why True 3D?
Most filters use flat 2D. This uses full `np.linalg.norm` in 3D, so z varies per point.

## Method
`q = r / R` where r=inradius, R=circumradius.
- ~0.5 = equilateral (stable)
- 0.0 = collinear/deenerate (reject)

## Usage
```python
from sieve import GeometricSieve
import numpy as np

sieve = GeometricSieve()

# True 3D with varying z per point
pos_3d = np.array([[1,0,0.2],[-0.5,0.866,1.4],[-0.5,-0.866,-0.7]])
print(sieve.shape_parameter(pos_3d))  # 0.4410 stable

pos_line = np.array([[0,0,0],[1,0,1],[2,0,2]])
print(sieve.shape_parameter(pos_line))  # 0.0 reject
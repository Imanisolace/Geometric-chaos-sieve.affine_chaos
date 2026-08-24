# geometric-sieve

O(1) geometric filter for 3-body stability. True 3D with varying z.

## Method
Uses `q = r / R` (inradius / circumradius). ~0.5 equilateral, 0 degenerate.
Uses full 3D norms, so varying z per point is handled.

## Usage
```python
from sieve import GeometricSieve
import numpy as np

sieve = GeometricSieve()

# True 3D with varying z per point
pos_3d = np.array([[1,0,0.2],[-0.5,0.866,1.4],[-0.5,-0.866,-0.7]])
print(sieve.shape_parameter(pos_3d)) # 0.4410 stable

pos_line = np.array([[0,0,0],[1,0,1],[2,0,2]])
print(sieve.shape_parameter(pos_line)) # 0.0 reject
# geometric-sieve

O(1) filter for 3-body stability. Handles varying z (True 3D).

Uses `q = r / R` (inradius / circumradius) with true 3D norms.

### Usage
```python
from sieve import GeometricSieve
import numpy as np

sieve = GeometricSieve()

# varying z per point - proves True 3D
pos_3d = np.array([[1,0,0.2],[-0.5,0.866,1.4],[-0.5,-0.866,-0.7]])
pos_line = np.array([[0,0,0],[1,0,1],[2,0,2]])

print(sieve.shape_parameter(pos_3d)) # ~0.38 stable
print(sieve.shape_parameter(pos_line)) # 0 reject
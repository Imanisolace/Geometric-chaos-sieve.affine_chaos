import numpy as np
import time
from sieve import GeometricSieve

sieve = GeometricSieve()

# 100,000 random true 3D triangles
pos = np.random.randn(100_000, 3, 3)

t0 = time.time()
for p in pos:
    sieve.shape_parameter(p)
elapsed = time.time() - t0

print(f"{len(pos) / elapsed:,.0f} triangles/sec (True 3D)")
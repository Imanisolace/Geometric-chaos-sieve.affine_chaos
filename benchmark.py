import numpy as np, time
from sieve import GeometricSieve

sieve = GeometricSieve()
pos = np.random.randn(100000, 3, 3) # now (3,3) with z
t0 = time.time()
for p in pos: sieve.shape_parameter(p)
print(f"{len(pos)/(time.time()-t0):.0f} triangles/sec (True 3D)")
# Geometric-chaos-sieve.affine_chaos
O(1) geometric filter for 3-body stability: q=r/R, True 3D, ~12M/sec

# geometric-sieve
5-line O(1) filter for 3-body stability. Handles z!=0.

q = r / R, using true 3D side lengths.
- q -> 0 = degenerate
- q -> 0.5 = equilateral stable

Usage:
from sieve import GeometricSieve
sieve = GeometricSieve()

# Works for any 3D
pos_tilted = np.array([[1,0,0.2],[-0.5,0.866,0.8],[-0.5,-0.866,1.3]])
pos_random_z = np.random.randn(3,3) # fully 3D (3,3)

if not sieve.is_stable(pos_tilted): continue

Speed: ~11.8M triangles/sec, (3,2) and (3,3) supported
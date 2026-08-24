import numpy as np
from sieve import GeometricSieve

s = GeometricSieve()

eq_2d = np.array([[1,0],[ -0.5,0.866],[ -0.5,-0.866]])
eq_3d = np.array([[1,0,0.5],[-0.5,0.866,0.5],[-0.5,-0.866,0.5]]) # z!=0 tilted
line = np.array([[0,0,0],[1,0,1],[2,0,2]]) # collinear with z!=0

print(f"2D equilateral q={s.shape_parameter(eq_2d):.3f} -> should 0.5")
print(f"3D tilted q={s.shape_parameter(eq_3d):.3f} -> should 0.5")
print(f"3D line q={s.shape_parameter(line):.6f} -> should 0")

assert s.shape_parameter(eq_2d) > 0.4
assert s.shape_parameter(eq_3d) > 0.4
assert s.shape_parameter(line) < 1e-6
print("all tests passed")
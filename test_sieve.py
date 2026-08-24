import numpy as np
from sieve import GeometricSieve

s = GeometricSieve()

# 2D equilateral
eq_2d = np.array([
    [1.0, 0.0],
    [-0.5, 0.86602540378],
    [-0.5, -0.86602540378]
])

# True 3D with VARYING z per point (proves True 3D)
eq_3d_varying = np.array([
    [1.0, 0.0, 0.2],
    [-0.5, 0.86602540378, 1.4],
    [-0.5, -0.86602540378, -0.7]
])

# Collinear with VARYING z (diagonal line in 3D)
line_3d_varying = np.array([
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 1.0],
    [2.0, 0.0, 2.0]
])

print(f"2D equilateral q = {s.shape_parameter(eq_2d):.4f} (should ≈ 0.5)")
print(f"3D varying z q = {s.shape_parameter(eq_3d_varying):.4f} (should >0.2 stable)")
print(f"3D line var z q = {s.shape_parameter(line_3d_varying):.6f} (should ≈ 0)")

assert s.shape_parameter(eq_2d) > 0.4
assert s.shape_parameter(eq_3d_varying) > 0.2
assert s.shape_parameter(line_3d_varying) < 1e-6

print("\nAll True 3D varying-z tests passed.")
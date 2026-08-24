import numpy as np

class GeometricSieve:
    def shape_parameter(self, pos: np.ndarray) -> float:
        """q = r/R, works for (3,2) and (3,3) even if z!=0"""
        a = np.linalg.norm(pos[1] - pos[0])
        b = np.linalg.norm(pos[2] - pos[1])
        c = np.linalg.norm(pos[0] - pos[2])
        s = (a + b + c) / 2.0
        area_sq = max(s * (s - a) * (s - b) * (s - c), 0.0)
        if area_sq < 1e-18:
            return 0.0
        area = np.sqrt(area_sq)
        r = area / (s + 1e-18)
        R = (a * b * c) / (4 * area + 1e-18)
        return r / (R + 1e-18)

    def is_stable(self, pos: np.ndarray, threshold: float = 5e-4) -> bool:
        return self.shape_parameter(pos) > threshold

    def batch_filter(self, positions: np.ndarray, threshold: float = 5e-4):
        return np.array([self.is_stable(p, threshold) for p in positions])
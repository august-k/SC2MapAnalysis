import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import center_of_mass
from Region import Region


class Polygon:

    def __init__(self, region: Region):
        self.region = region
        self.array = region.array
        self.indices = np.where(self.array == 1)

    def plot(self):
        plt.imshow(self.array.T)
        plt.show()

    @property
    def center(self):
        cm = center_of_mass(self.array)
        return np.int(cm[0]), np.int(cm[1])

    def is_inside(self, point):
        return point[0] in self.indices[1] and point[1] in self.indices[0]

    @property
    def perimeter(self):
        isolated_region = self.region.array
        xx, yy = np.gradient(isolated_region)
        edge_indices = np.argwhere(xx ** 2 + yy ** 2 > 0.1)
        return edge_indices


    @property
    def area(self):
        """
        Number of points contained within Polygon.
        :return:
        """
        return len(self.indices[0])

    @property
    def get_holes(self, coords):
        # fly zones inside the Polygon
        pass
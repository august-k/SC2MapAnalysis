from typing import List

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from sc2.game_info import GameInfo
from sc2.position import Point2
from scipy.ndimage import binary_fill_holes, generate_binary_structure, label

from Region import Region


class MapData:
    def __init__(self, map_name: str, game_info: GameInfo, base_locations: List[Point2]):

        self.map_name = map_name
        self.placement_arr = game_info.placement_grid.data_numpy
        self.path_arr = game_info.pathing_grid.data_numpy
        self.base_locations = base_locations
        self.region_grid = None
        self.regions = {}
        self.compile_map()

    def compile_map(self):
        grid = binary_fill_holes(self.placement_arr).astype(int)
        # chokes = np.where
        # compiled_grid = grid * (np.abs(scipy.ndimage.laplace(grid)) > 0)
        compiled_grid = grid

        s = generate_binary_structure(2, 2)
        labeled_array, num_features = label(compiled_grid, structure=s)

        rows, cols = labeled_array.shape
        region_grid = np.append(labeled_array, np.zeros((abs(cols - rows), cols)), axis=0).T
        regions_labels = np.unique(labeled_array)

        for i in range(len(regions_labels)):
            region = Region(array=np.where(region_grid == i, 1, 0), label=i, map_expansions=self.base_locations)
            self.regions[i] = region
        self.region_grid = region_grid

    def plot_regions_by_label(self, fontdict=None):
        if not fontdict:
            fontdict = {'family': 'normal',
                        'weight': 'bold',
                        'size': 25}

        values = list(self.regions.keys())

        plt.figure(figsize=(20, 20))
        im = plt.imshow(self.region_grid.T, interpolation='none')
        colors = [im.cmap(im.norm(value)) for value in values]

        # create a patch (proxy artist) for every color
        patches = [mpatches.Patch(color=colors[i], label="Region {l}".format(
            l=str(values[i]) + " Size: " + str(self.regions[i].get_area))) for i in range(len(values))]

        # put those patched as legend-handles into the legend
        plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        for key, value in self.regions.items():
            plt.text(value.polygon.center[0],
                     value.polygon.center[1],
                     value.label,
                     bbox=dict(fill=False, edgecolor='red', linewidth=2),
                     fontdict=fontdict)
        plt.show()

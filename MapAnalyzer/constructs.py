from functools import lru_cache
from typing import TYPE_CHECKING

import numpy as np
from sc2.game_info import Ramp as sc2Ramp
from sc2.position import Point2

from MapAnalyzer.Polygon import Polygon

if TYPE_CHECKING:  # pragma: no cover
    from .MapData import MapData


class ChokeArea(Polygon):
    """
    ChokeArea DocString
    """

    def __init__(
            self, array: np.ndarray, map_data: "MapData", main_line: tuple = None
    ) -> None:
        self.main_line = main_line
        super().__init__(map_data=map_data, array=array)

    @lru_cache(100)
    def get_width(self) -> float:
        import math

        if self.main_line is not None:
            x1, y1 = self.main_line[0][0], self.main_line[0][1]
            x2, y2 = self.main_line[1][0], self.main_line[1][1]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def __repr__(self):  # pragma: no cover
        return f"<ChokeArea[size={self.area}]> of {[r for r in self.areas]}"


class MDRamp(ChokeArea):
    """
    MDRamp DocString
    """

    def __init__(self, map_data: "MapData", array: np.ndarray, ramp: sc2Ramp) -> None:
        self.ramp = ramp
        self.regions = []
        super().__init__(map_data=map_data, array=array)

    @property
    def top_center(self) -> Point2:
        return self.ramp.top_center

    @property
    def bottom_center(self) -> Point2:
        return self.ramp.bottom_center

    def __repr__(self):  # pragma: no cover
        return f"<MDRamp[size={self.area}]: [{[a for a in self.areas]}]"


class VisionBlockerArea(ChokeArea):
    """
    VisionBlockerArea DocString
    """

    def __init__(self, map_data: "MapData", array: np.ndarray) -> None:
        super().__init__(map_data=map_data, array=array)

    def __repr__(self):  # pragma: no cover
        return f"<VisionBlockerArea[size={self.area}]: [{[a for a in self.areas]}]"

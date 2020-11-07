from ..campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger

MAP = CampaignMap('B1')
MAP.shape = 'J5'
MAP.camera_data = ['D2', 'D3', 'G2', 'G3']
MAP.camera_data_spawn_point = ['D3', 'D2']
MAP.map_data = """
    -- -- ME -- ME ME ME ME ME --
    SP -- ++ -- ME -- ME ++ -- MB
    ++ ++ ++ ++ ++ ++ -- ++ ME ++
    SP -- -- ++ ME -- ME ++ -- MB
    -- -- -- ME -- ME ME ME ME --
"""
MAP.weight_data = """
    50 50 10 50 30 20 10 10 10 50
    50 50 50 50 30 50 20 50 50 10
    50 50 50 50 50 50 50 50 30 50
    50 50 50 50 50 50 20 50 50 10
    50 50 50 10 30 20 10 10 10 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 4},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 1},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 1},
    {'battle': 5},
    {'battle': 6, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, J1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, J2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, J3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, J4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, J5, \
    = MAP.flatten()


class Config:
    # ===== Start of generated config =====
    MAP_HAS_MAP_STORY = True
    MAP_HAS_FLEET_STEP = False
    MAP_HAS_AMBUSH = True
    # ===== End of generated config =====


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        return self.battle_default()

    def battle_6(self):
        return self.fleet_boss.clear_boss()

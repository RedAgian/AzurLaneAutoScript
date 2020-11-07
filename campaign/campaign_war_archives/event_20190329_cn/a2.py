from ..campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger
from .a1 import Config as ConfigBase

MAP = CampaignMap('A2')
MAP.shape = 'H6'
MAP.camera_data = ['D2', 'D4', 'E2', 'E4']
MAP.camera_data_spawn_point = ['D4']
MAP.map_data = """
    -- -- ++ ++ ++ ++ -- MM
    ME -- ME -- ME -- ME --
    -- ++ -- ++ ++ ME ++ ME
    -- -- ME ++ ++ ME ++ --
    -- -- ++ MB ME ME -- --
    SP SP ++ MB ME ME ME --
"""
MAP.weight_data = """
    50 50 50 50 50 50 50 50
    20 50 10 10 10 10 50 50
    50 50 50 50 50 10 50 50
    50 50 20 50 50 10 50 50
    50 50 50 10 10 10 50 50
    50 50 50 10 20 20 50 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 4},
    {'battle': 1, 'enemy': 1, 'mystery': 1},
    {'battle': 2, 'enemy': 1},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 1},
    {'battle': 5, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, \
A2, B2, C2, D2, E2, F2, G2, H2, \
A3, B3, C3, D3, E3, F3, G3, H3, \
A4, B4, C4, D4, E4, F4, G4, H4, \
A5, B5, C5, D5, E5, F5, G5, H5, \
A6, B6, C6, D6, E6, F6, G6, H6, \
    = MAP.flatten()


class Config(ConfigBase):
    # ===== Start of generated config =====
    MAP_HAS_MAP_STORY = True
    MAP_HAS_FLEET_STEP = False
    MAP_HAS_AMBUSH = True
    # ===== End of generated config =====


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        if self.fleet_2_push_forward():
            return True

        return self.battle_default()

    def battle_5(self):
        return self.fleet_boss.clear_boss()

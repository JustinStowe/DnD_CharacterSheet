"""
GUI Tabs Package
Contains modular tab implementations for the character sheet
"""

# Export all modular tabs
from .base_tab import BaseTab
from .main_tab import MainTab
from .skills_tab import SkillsTab
from .inventory_tab import InventoryTab
from .spells_tab import SpellsTab
from .feats_tab import FeatsTab
from .magic_items_tab import MagicItemsTab

__all__ = [
    'BaseTab',
    'MainTab',
    'SkillsTab',
    'InventoryTab',
    'SpellsTab',
    'FeatsTab',
    'MagicItemsTab'
]

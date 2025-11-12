"""
Prestige Classes Package
Contains all prestige class definitions from various D&D 3e sourcebooks
"""

from .prestige_classes import (
    PRESTIGE_CLASS_DEFINITIONS,
    check_prestige_class_requirements,
    get_prestige_class_info,
    get_all_prestige_classes,
    is_prestige_class
)

__all__ = [
    'PRESTIGE_CLASS_DEFINITIONS',
    'check_prestige_class_requirements',
    'get_prestige_class_info',
    'get_all_prestige_classes',
    'is_prestige_class'
]

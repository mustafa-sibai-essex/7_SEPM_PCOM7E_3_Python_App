"""
It holds a data class to be instantiated to be used throughout the application.

Imports:
    from dataclasses: dataclass
"""

from dataclasses import dataclass

@dataclass
class AppData:
    """A class to keep track of global variables used throughout the __test__"""

    keys: list
    entries_hw: list
    entries_sw: list
    total_hw: float
    total_sw: float
    total_widgets: dict

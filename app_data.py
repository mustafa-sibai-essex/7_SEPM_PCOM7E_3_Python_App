from dataclasses import dataclass

@dataclass
class app_data:
    """A class to keep track of global variables used throughout the app"""

    keys: list
    entries_hw: list
    entries_sw: list
    total_hw: float
    total_sw: float
    total_widgets: dict
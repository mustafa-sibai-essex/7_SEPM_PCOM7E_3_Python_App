"""
It holds the keys and starts the GUI Handler.

Imports:
    from app_data: AppData
    from GUIHandler: GUIHandler
    from JSONHandler: JSONHandler
"""


from app_data import AppData
from gui_handler import GUIHandler
from json_handler import JSONHandler

keys = [
    "type",
    "description",
    "count",
    "price",
    "man_cost",
    "des_cost",
    "cod_cost",
    "tes_cost",
    "total",
]

global_data = AppData(keys, [], [], 0.0, 0.0, {})

json_handler = JSONHandler(global_data)
gui_handler = GUIHandler(global_data, json_handler)
json_handler.set_gui_handler(gui_handler)

gui_handler.start()

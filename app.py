from app_data import app_data
from GUIHandler import GUIHandler
from JSONHandler import JSONHandler

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

global_data = app_data(keys, [], [], 0.0, 0.0, {})

json_handler = JSONHandler(global_data)
gui_handler = GUIHandler(global_data, json_handler)
json_handler.set_gui_handler(gui_handler)

gui_handler.start()

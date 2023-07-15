from app_data import app_data
from GUIHandler import GUIHandler
from JSONHandler import JSONHandler

global_data = app_data([], [], [], 0, 0, {})

json_handler = JSONHandler(global_data)
gui_handler = GUIHandler(global_data, json_handler)
json_handler.set_gui_handler(gui_handler)

gui_handler.start()
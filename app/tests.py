"""
Includes unit tests for the basic functionality of the application.

Imports:
    app

Functions:
    test_calculate()
    test_hw_data()
    test_sw_data()
    test_label()
    test_clear_frame()

Fixtures used in the tests can be found in conftest.py
"""

import sys

sys.path.insert(0, "..")
import os
from gui_handler import GUIHandler
from json_handler import JSONHandler
from app_data import AppData

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


def test_calculate(test_data_1):
    """A test case to check if the calculation is correct"""
    value = gui_handler.calculate(test_data_1)
    assert value == 180.18


def test_hw_data(test_data_2):
    """Tests if the hardware data is parsed correctly"""
    total = 180.18  # Total of the test data, not used in the test - only to pass it as argument
    test_entries = gui_handler.push_data_hw(test_data_2, total)
    assert len(test_data_2) == len(test_entries)


def test_sw_data(test_data_3):
    """Tests if the software data is parsed correctly"""
    total = 56.69  # Total of the test data, not used in the test - only to pass it as argument
    test_entries = gui_handler.push_data_hw(test_data_3, total)
    assert len(test_data_3) == len(test_entries)


def test_label():
    """Tests if the push_desc function has the correct text in the label object"""
    text = "Test test test"
    test_label = gui_handler.push_desc(text)
    test_text = test_label.cget("text")
    assert text == test_text


def test_export_json(mocker):
    mocker.patch(
        "json_handler.filedialog.asksaveasfilename",
        return_value="project_test_data.json",
    )
    json_handler.export_json(global_data)
    os.remove("project_test_data.json")


def test_import_json(mocker):
    mocker.patch(
        "json_handler.filedialog.asksaveasfilename",
        return_value="project_test_data.json",
    )
    json_handler.export_json(global_data)
    mocker.patch(
        "json_handler.filedialog.askopenfilename", return_value="project_test_data.json"
    )
    raw_data = json_handler.load_json()
    assert raw_data != None


def test_import_json_not_found(mocker):
    mocker.patch(
        "json_handler.filedialog.asksaveasfilename",
        return_value="project_test_data.json",
    )
    json_handler.export_json(global_data)
    os.remove("project_test_data.json")
    mocker.patch(
        "json_handler.filedialog.askopenfilename", return_value="project_test_data.json"
    )
    raw_data = json_handler.load_json()
    data = raw_data["data"]
    assert data == None

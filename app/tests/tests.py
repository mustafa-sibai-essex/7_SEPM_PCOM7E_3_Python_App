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


from app import app

def test_calculate(test_data_1):
    """A test case to check if the calculation is correct"""
    value = app.calculate(test_data_1)
    assert value == 180.18


def test_hw_data(test_data_2):
    """Tests if the hardware data is parsed correctly"""
    total = 180.18  # Total of the test data, not used in the test - only to pass it as argument
    test_entries = app.push_data_hw(test_data_2, total)
    assert len(test_data_2) == len(test_entries)


def test_sw_data(test_data_3):
    """Tests if the software data is parsed correctly"""
    total = 56.69  # Total of the test data, not used in the test - only to pass it as argument
    test_entries = app.push_data_hw(test_data_3, total)
    assert len(test_data_3) == len(test_entries)


def test_label():
    """Tests if the push_desc function has the correct text in the label object"""
    text = "Test test test"
    test_label = app.push_desc(text)
    test_text = test_label.cget("text")
    assert text == test_text


def test_clear_frame(test_frame):
    """Tests if clear_frame() function destroys all children of a frame"""
    app.clear_frame(test_frame)
    assert len(test_frame.winfo_children()) == 0

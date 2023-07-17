"""
Pytest configuration file with fixtures used in the tests.

Imports:
    pytest
    tkinter

Functions:
    test_data_1()
    test_data_2()
    test_data_3()
    test_frame()

"""
import pytest
import tkinter as tk


@pytest.fixture
def test_data_1():
    """Test data that will be used in the tests"""
    test_data_1 = [
        {'type': 'Board', 'description': 'A83-S', 'count': 1, 'price': 25, 'man_cost': 14, 'des_cost': 8, 'cod_cost': 0,
         'tes_cost': 1.38},
        {'type': 'CPU', 'description': '68k0', 'count': 1, 'price': 8, 'man_cost': 0, 'des_cost': 0, 'cod_cost': 0,
         'tes_cost': 0},
        {'type': 'Glue Chip', 'description': 'G1', 'count': 1, 'price': 5, 'man_cost': 0, 'des_cost': 16, 'cod_cost': 0,
         'tes_cost': 2.76},
        {'type': 'Glue Chip', 'description': 'G2', 'count': 1, 'price': 5, 'man_cost': 0, 'des_cost': 16, 'cod_cost': 0,
         'tes_cost': 2.76},
        {'type': 'Glue Chip', 'description': 'G3', 'count': 1, 'price': 5, 'man_cost': 0, 'des_cost': 16, 'cod_cost': 0,
         'tes_cost': 2.76},
        {'type': 'Glue Chip', 'description': 'G4', 'count': 1, 'price': 5, 'man_cost': 0, 'des_cost': 16, 'cod_cost': 0,
         'tes_cost': 2.76},
        {'type': 'RAM', 'description': '256KB', 'count': 2, 'price': 5, 'man_cost': 0, 'des_cost': 16, 'cod_cost': 0,
         'tes_cost': 2.76}]
    return test_data_1


@pytest.fixture
def test_data_2():
    """Test data that will be used in the tests"""
    test_data_2 = [
        {'type': 'Board', 'description': 'A83-S', 'count': 1, 'price': 25, 'man_cost': 14, 'des_cost': 8, 'cod_cost': 0,
         'tes_cost': 1.38, 'total': 48.38},
        {'type': 'CPU', 'description': '68k0', 'count': 1, 'price': 8, 'man_cost': 0, 'des_cost': 0, 'cod_cost': 0,
         'tes_cost': 0, 'total': 8},
        {'type': 'Glue Chip', 'description': 'G1', 'count': 1, 'price': 5, 'man_cost': 0, 'des_cost': 16, 'cod_cost': 0,
         'tes_cost': 2.76, 'total': 23.76},
        {'type': 'Glue Chip', 'description': 'G2', 'count': 1, 'price': 5, 'man_cost': 0, 'des_cost': 16, 'cod_cost': 0,
         'tes_cost': 2.76, 'total': 23.76},
        {'type': 'Glue Chip', 'description': 'G3', 'count': 1, 'price': 5, 'man_cost': 0, 'des_cost': 16, 'cod_cost': 0,
         'tes_cost': 2.76, 'total': 23.76},
        {'type': 'Glue Chip', 'description': 'G4', 'count': 1, 'price': 5, 'man_cost': 0, 'des_cost': 16, 'cod_cost': 0,
         'tes_cost': 2.76, 'total': 23.76},
        {'type': 'RAM', 'description': '256KB', 'count': 2, 'price': 5, 'man_cost': 0, 'des_cost': 16, 'cod_cost': 0,
         'tes_cost': 2.76, 'total': 28.76}]
    return test_data_2


@pytest.fixture
def test_data_3():
    """Test data that will be used in the tests"""
    test_data_3 = [{'type': 'OS', 'description': 'HB/OS in ROM', 'count': 1, 'price': 0, 'man_cost': 0, 'des_cost': 9,
                    'cod_cost': 8.85, 'tes_cost': 1.38, 'total': 19.23},
                   {'type': 'OS', 'description': 'MccOS', 'count': 1, 'price': 0, 'man_cost': 0, 'des_cost': 2.25,
                    'cod_cost': 2.95, 'tes_cost': 0.15, 'total': 5.35},
                   {'type': 'OS', 'description': 'Libraries and drivers', 'count': 1, 'price': 0.025, 'man_cost': 0,
                    'des_cost': 12.38, 'cod_cost': 19.18, 'tes_cost': 0.52, 'total': 32.11}]
    return test_data_3

@pytest.fixture
def test_frame():
    """Creates a test frame with two children"""
    root = tk.Tk()
    test_frame = tk.Frame(root)
    child1 = tk.Frame(test_frame)
    child2 = tk.Frame(test_frame)
    return test_frame
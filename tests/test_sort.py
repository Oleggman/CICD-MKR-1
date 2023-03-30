import pytest
from main import *


def test_read_info():
    assert read_info("test_file.txt") == [['Ukraine', '600000', '45000000']]


def test_sort_data():
    assert get_sort([['First element', '220', '430'],
                     ['Second element', '105', '540'],
                     ['Third element', '365', '445']], 1) == [['Second element', '105', '540'],
                                                              ['First element', '220', '430'],
                                                              ['Third element', '365', '445']]


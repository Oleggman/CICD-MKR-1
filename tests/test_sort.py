import pytest
from main import *
from pytest import mark


def test_read_info():
    assert read_info("test_file.txt") == [['Ukraine', '600000', '45000000']]


def test_get_sort_1():
    assert get_sort([['First element', '220', '430'],
                     ['Second element', '105', '540'],
                     ['Third element', '365', '445']], 1) == [['Second element', '105', '540'],
                                                              ['First element', '220', '430'],
                                                              ['Third element', '365', '445']]


def test_sort_by_population():
    assert sort_by_population([['First element', '200', '300'],
                                  ['Second element', '100', '500'],
                                  ['Third element', '300', '400']]) == [['First element', '200', '300'],
                                                                        ['Third element', '300', '400'],
                                                                        ['Second element', '100', '500']]


def test_sort_by_area():
    assert sort_by_area([['First element', '200', '300'],
                                  ['Second element', '100', '500'],
                                  ['Third element', '300', '400']]) == [['Second element', '100', '500'],
                                                                        ['First element', '200', '300'],
                                                                        ['Third element', '300', '400']]

@mark.fixture_example
def test_first():
    print('Second element', '100', '500')

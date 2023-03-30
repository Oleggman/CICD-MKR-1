import pytest
from main import *


def test_read_info():
    assert read_info("test_file.txt") == [['Ukraine', '600000', '45000000']]



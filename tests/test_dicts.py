import pytest
from solutions.dicts import *

# Tests for get_information
def test_get_information():
    assert get_information({'a': {'b': 1, 'c': 2}}, 'a', 'b') == 1
    assert get_information({'a': {'b': 1, 'c': 2}}, 'a', 'd') == None
    assert get_information({'a': {'b': 1, 'c': 2}}, 'x', 'b') == None

# Tests for add_information
def test_add_information():
    # Adding a value to an innermost dictionary when middle dictionary exists
    assert add_information({'a': {'b': {}}}, 'a', 'b', 'c', 1) == {'a': {'b': {'c': 1}}}

    # Modifying a value in an innermost dictionary
    assert add_information({'a': {'b': {'c': 1}}}, 'a', 'b', 'c', 2) == {'a': {'b': {'c': 2}}}

    # Adding a new middle and innermost dictionary and value
    assert add_information({'a': {'b': {'c': 1}}}, 'x', 'y', 'z', 3) == {'a': {'b': {'c': 1}}, 'x': {'y': {'z': 3}}}

    # Adding a new innermost dictionary and value when outer and middle dictionaries exist
    assert add_information({'a': {'b': {}}}, 'a', 'b', 'd', 4) == {'a': {'b': {'d': 4}}}



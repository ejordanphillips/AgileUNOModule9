"""
Jordan Phillips
Module 9 Assignment 
"""

import pytest

from my_module import greeting

def test_greeting_pass():
    assert "Hello, Jordan" == greeting("Jordan"), "test failed"

def test_greeting_fail():
    assert "Hello, Jordan" != greeting("Jordan"), "test failed"

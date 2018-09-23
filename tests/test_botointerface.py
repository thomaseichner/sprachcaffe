#!/usr/bin/env python

"""test_botointerface.py: docstring"""

__author__ = 'thomas'
__creation_date__ = '23.09.18'

import pytest

import botointerface


def test_service_setup():
    bi = botointerface.BotoInterface(config_file='test_basic_config.yml', loglevel='DEBUG')
    with pytest.raises(NameError):
        assert bi.setup_service()
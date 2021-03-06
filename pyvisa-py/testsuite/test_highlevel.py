# -*- coding: utf-8 -*-
"""Test creating a resource manager using PyVISA-Py as a backend.


:copyright: 2014-2020 by PyVISA-py Authors, see AUTHORS for more details.
:license: MIT, see LICENSE for more details.

"""
import importlib
from pyvisa.testsuite import BaseTestCase

highlevel = importlib.import_module("pyvisa-py.highlevel")


class TestPyVisaLibrary(BaseTestCase):
    """Test generic property of PyVisaLibrary."""

    def test_debug_info(self):
        """Test generating debug infos for PyVISA-py."""
        infos = highlevel.PyVisaLibrary.get_debug_info()
        for key in ("Version",):
            self.assertIn(key, infos)

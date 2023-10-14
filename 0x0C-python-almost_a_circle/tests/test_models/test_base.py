#!/usr/bin/python3
"""Create Tests case using unitest for base.py:

    Test Cases:
    setUp: Set Up the nbobjects to Zero
    Test_id_assign_with_value: key-value pair test
    test_id_assing_with_value_2: empty class call
    test_id_assing_with_value_3: previse number id without the key id
    test_id_assin_with_nvalue: test with a negative value
    test_id_assig_with_none_value: Pass None as argument
    test_multi_id: Test with multiple ID & calculate
    """

import unittest
from models.base import Base


class Test_instan(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_assign_with_value(self):
        obj = Base(id=1)
        self.assertEqual(obj.id, 1)

    def test_id_assing_with_value_2(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id + obj2.id, 3)

    def test_id_assing_with_value_3(self):
        obj = Base(90)
        self.assertEqual(obj.id, 90)

    def test_id_assin_with_nvalue(self):
        obj = Base(-5)
        self.assertEqual(obj.id, -5)

    def test_id_assig_with_none_value(self):
        obj = Base(None)
        self.assertEqual(obj.id, 1)

    def test_multi_id(self):
        obj = Base()
        obj1 = Base(96)
        obj2 = Base()
        self.assertEqual(obj.id + obj1.id + obj2.id, 99)

    def test_inequality(self):
        obj = Base(1)
        obj2 = Base(2)
        self.assertNotEqual(obj.id, obj2.id)

    def test_str_as_id(self):
        obj = Base("1")
        obj1 = Base("unit")
        self.assertEqual(obj.id, "1")
        self.assertEqual(obj1.id, "unit")

    def test_more_args(self):
        with self.assertRaises(TypeError):
            obj = Base(1, 1)

    def test_try_access_to_private_attrs(self):
        obj = Base()
        with self.assertRaises(AttributeError):
            obj.__nb_objects

#!/usr/bin/python3
import unittest
from models.city import City
"""
Unittest Module for City class
"""


class TestUser(unittest.TestCase):
    ''' Unittest for City class '''

    def test_object_Instantiation(self):
        ''' instantiates class '''
        self.city = City()

    def testattr(self):
        ''' test Class: City attributes '''
        self.city = City()
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertFalse(hasattr(self.city, "random_attr"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
        self.city.name = "WonderLand"
        self.city.state_id = "Won67L0nd"
        self.assertEqual(self.city.name, "WonderLand")
        self.assertEqual(self.city.state_id, "Won67L0nd")
        self.assertEqual(self.city.__class__.__name__, "City")

    def testsave(self):
        ''' testing method: save '''
        self.city = City()
        self.city.save()
        self.assertTrue(hasattr(self.city, "updated_at"))

    def teststr(self):
        ''' testing __str__ return format of BaseModel '''
        self.city = City()
        s = "[{}] ({}) {}".format(self.city.__class__.__name__,
                                  str(self.city.id), self.city.__dict__)
        self.assertEqual(print(s), print(self.city))

if __name__ == '__main__':
    unittest.main()

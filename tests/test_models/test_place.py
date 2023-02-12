#!/usr/bin/python3
import unittest
from models.place import Place
"""
Unittest Module for Place class
"""


class TestUser(unittest.TestCase):
    ''' Unittest for Place class '''

    def test_object_Instantiation(self):
        ''' instantiates class '''
        self.place = Place()

    def testattr(self):
        ''' test Class: Place attributes '''
        self.place = Place()
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertFalse(hasattr(self.place, "random_attr"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "id"))
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longtude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def testsave(self):
        ''' testing method: save '''
        self.place = Place()
        self.place.save()
        self.assertTrue(hasattr(self.place, "updated_at"))

    def teststr(self):
        ''' testing __str__ return format of BaseModel '''
        self.place = Place()
        s = "[{}] ({}) {}".format(self.place.__class__.__name__,
                                  str(self.place.id), self.place.__dict__)
        self.assertEqual(print(s), print(self.place))

if __name__ == '__main__':
    unittest.main()

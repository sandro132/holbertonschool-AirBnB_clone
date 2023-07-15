#!/usr/bin/python3
"""
Unittest for State
"""

import unittest
from datetime import datetime
from models.review import Review
from time import sleep


class testState(unittest.TestCase):
    """
    Test for State
    """
    def test_str_place_id(self):
        """
        Check if place_id is a string
        """
        self.assertEqual(str, type(Review.place_id))

    def test_str_user_id(self):
        """
        Check if user_id is a string
        """
        self.assertEqual(str, type(Review.user_id))

    def test_str_text(self):
        """
        Check if text is a string
        """
        self.assertEqual(str, type(Review.text))

    def test_unique_id(self):
        """
        Check if the review id in unique
        """
        instance1 = Review()
        instance2 = Review()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_instance_createdat(self):
        """
        Check if created_at is a intance of Review
        """
        self.assertTrue(hasattr(Review(), "created_at"), True)

    def test_instance(self):
        """
        Check if updated_at is a intance of Review
        """
        self.assertTrue(hasattr(Review(), "updated_at"), True)

    def test_public_datetime(self):
        """
        Test for a make public datetime
        """
        self.assertEqual(datetime, type(Review().created_at))

    def test_public_datetime_updated(self):
        """
        Test for a make public datetime
        """
        self.assertEqual(datetime, type(Review().updated_at))

    def test_less_time_createdat(self):
        """
        Check less time in created_at
        """
        instance1 = Review()
        sleep(0.2)
        instance2 = Review()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_less_time_updatedat(self):
        """
        Check less time in updated_at
        """
        instance1 = Review()
        sleep(0.2)
        instance2 = Review()
        self.assertLess(instance1.updated_at, instance2.updated_at)


if __name__ == '__main__':
    unittest.main()

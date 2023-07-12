import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setup(self):
        self.base = BaseModel()

    def test_method_save(self):
        self.base = BaseModel()
        testsave = self.base.update_at()
        self.base.save()
        self.assertNotEqual(testsave, self.created_at)

    def test_method_to_dict(self):
        test_to_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(test_to_dict['created_at'], str)
        self.assertIsInstance(test_to_dict['updated_at'], str)

#    def test_method_attributes(self):
#        self.assertTrue(hasattr(BaseModel, "__init__"))
#        self.assertTrue(hasattr(BaseModel, "save"))
#        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        self.base = BaseModel()
        self.assertTrue(isinstance(self.base, BaseModel))

if __name__ == '__main__':
    unittest.main()
import unittest
from task2 import *
import sys
from unittest import skipIf


class TestMaterial(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("тесты к заданию 4 урока 18")


    def setUp(self) -> None:
        self.material_ = Material("steel", 7850.3)
        self.subject_ = Subject("wire", "steel", 7800.3)

    @skipIf(sys.version_info < (3, 10), reason="Вам нужна версия программы 3.10 или выше")
    def test_get_material(self):
        self.assertIsInstance(self.material_.get_material(), str)
        self.assertEqual(self.material_.get_material(), "steel;7850.3")





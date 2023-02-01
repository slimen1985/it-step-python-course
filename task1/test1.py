import unittest
import pytest
from task1 import *


class TestBirds(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("тесты к заданию 3 урока 16")

    def setUp(self) -> None:
        self.bird = Bird("Утка")
        self.fly_bird = FlyingBird("Орел")
        self.non_fly = NonFlyingBird("Страус")
        self.super_bird = SuperBird("Гусь", "зерно")

    def test_bird(self):
        self.assertIsInstance(self.fly_bird, Bird)
        self.assertIsInstance(self.super_bird, Bird)
        self.assertIsInstance(self.non_fly, Bird)


    def test_super_bird(self):
        self.assertEqual(self.super_bird.fly(), f"Птица {self.super_bird.name} умеет летать")
        self.assertEqual(self.super_bird.walk(), f"Птица {self.super_bird.name} умеет ходить")
        self.assertEqual(self.super_bird.swim(), f"Птица {self.super_bird.name} умеет плавать")
        self.assertEqual(self.super_bird.eat(), f"Птица {self.super_bird.name} ест {self.super_bird.ration}")

    @pytest.mark.xfail
    def test_non_fly_bird(self):
        self.assertEqual(self.non_fly.walk(), f"Птица {self.non_fly.name} не летает")














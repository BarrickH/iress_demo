import unittest
from app.main import Robot
from app.command import Command


class CommandTest(unittest.TestCase):
    def setUp(self):
        self.Robot_mock = Robot()
        pass

    def tearDown(self):
        del self.Robot_mock

    def test_rotate_robot(self):
        self.Command = Command(cmd='RIGHT')
        self.assertEqual(self.Command.rotate_robot(),None)
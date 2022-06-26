import unittest
from app.command import Command


class CommandTest(unittest.TestCase):
    def setUp(self):
        self.command = Command('')
        pass

    def tearDown(self):
        del self.command

    def test_rotate_robot(self):
        self.assertEqual(self.command.execute_command('RIGHT'),None)
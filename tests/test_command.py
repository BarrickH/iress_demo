import unittest
from app.command import Command
from app.exceoptions import IncorrectPlaceException, IncorrectCommandException


class CommandTest(unittest.TestCase):
    def setUp(self):
        self.command = Command('')

    def test_command_rotate_right(self):
        self.assertRaises(IncorrectPlaceException,self.command.execute_command,'RIGHT')

    def test_command_rotate_left(self):
        self.assertRaises(IncorrectPlaceException,self.command.execute_command,'LEFT')

    def test_command_move(self):
        self.assertRaises(IncorrectPlaceException,self.command.execute_command,'MOVE')

    def test_command_report(self):
        self.assertRaises(IncorrectPlaceException,self.command.execute_command,'REPORT')

    def test_command_invalid(self):
        self.assertRaises(IncorrectCommandException,self.command.execute_command,'INVALID')

    def test_command_place(self):
        self.assertEqual(self.command.execute_command('PLACE 1,1,NORTH'), None)
        test_result = {
            'placed':self.command.placed,
            'x':self.command.C._x,
            'y':self.command.C._y,
            'face':self.command.C.current_face_direction
        }
        expect_result = {
            'placed': True,
            'x': 1,
            'y': 1,
            'face': 'NORTH'
        }
        self.assertDictEqual(test_result,expect_result)

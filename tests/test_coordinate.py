import unittest
from app.command import Command
from app.exceoptions import IncorrectPlaceException


class CoordinateTest(unittest.TestCase):
    def setUp(self):
        self.command = Command('')

    def test_coordinate_value(self):
        self.command.execute_command('PLACE 1,1,NORTH')
        self.assertEqual(str(self.command.C),'1,1,NORTH')

    def test_place_out_coordinate(self):
        self.assertRaises(IncorrectPlaceException, self.command.execute_command, "PLACE 5,0,NORTH")
        self.assertRaises(IncorrectPlaceException, self.command.execute_command, "PLACE 0,5,NORTH")

    def test_move_out_coordinate(self):
        self.command.execute_command('PLACE 4,4,NORTH')
        self.assertRaises(IncorrectPlaceException, self.command.execute_command, "MOVE")
        self.command.execute_command('PLACE 4,4,EAST')
        self.assertRaises(IncorrectPlaceException, self.command.execute_command, "MOVE")

    def test_robot_move_inside_coordinate(self):
        self.command.execute_command('PLACE 2,2,SOUTH')
        self.command.execute_command("MOVE")
        self.assertEqual(self.command.C.__str__(),'2,1,SOUTH')

    def test_coordinate_face_direction(self):
        self.command.execute_command('PLACE 2,2,WEST')
        self.command.execute_command("RIGHT")
        self.assertEqual(self.command.C.current_face_direction, 'NORTH')
        self.command.execute_command("RIGHT")
        self.assertEqual(self.command.C.current_face_direction, 'EAST')
        self.command.execute_command("LEFT")
        self.assertEqual(self.command.C.current_face_direction, 'NORTH')
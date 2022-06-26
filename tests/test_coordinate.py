import unittest
from app.coordinate import Coordinate
from app.command import Command
from app.exceoptions import IncorrectPlaceException


class CoordinateTest(unittest.TestCase):
    def setUp(self):
        self.coordinate = Coordinate()

    def test_coordinate_value(self):
        self.coordinate.place_to_coordinate(x=1,y=1,face='NORTH')
        self.assertEqual(str(self.coordinate),'1,1,NORTH')

    def test_place_out_coordinate(self):
        self.assertRaises(IncorrectPlaceException, self.coordinate.place_to_coordinate, x=5,y=0,face='NORTH')
        self.assertRaises(IncorrectPlaceException, self.coordinate.place_to_coordinate, x=0,y=5,face='NORTH')

    def test_move_out_coordinate(self):
        self.coordinate.place_to_coordinate(x=4,y=4,face='NORTH')
        self.assertRaises(IncorrectPlaceException, self.coordinate.move_in_coordinate, x=0,y=1)
        self.coordinate.place_to_coordinate(x=4,y=4,face='EAST')
        self.assertRaises(IncorrectPlaceException, self.coordinate.move_in_coordinate, x=1,y=0)

    def test_robot_move_inside_coordinate(self):
        self.coordinate.place_to_coordinate(x=2,y=2,face='SOUTH')
        self.coordinate.move_in_coordinate(x=0,y=-1)
        self.assertEqual(self.coordinate.__str__(),'2,1,SOUTH')

    def test_coordinate_face_direction_integration(self):
        command = Command(cmd='')
        command.execute_command('PLACE 2,2,WEST')
        command.execute_command("RIGHT")
        self.assertEqual(command.C.current_face_direction, 'NORTH')
        command.execute_command("RIGHT")
        self.assertEqual(command.C.current_face_direction, 'EAST')
        command.execute_command("LEFT")
        self.assertEqual(command.C.current_face_direction, 'NORTH')
import unittest
from app.validations import CoordinateValidations
from app.exceoptions import IncorrectPlaceException


class CommandTest(unittest.TestCase):
    def test_valid_place_command_validator(self):
        self.assertEqual(CoordinateValidations.place_cmd_validation('PLACE 0,0,NORTH'),'PLACE 0,0,NORTH')
        self.assertEqual(CoordinateValidations.place_cmd_validation('PLACE 0,0,SOUTH'),'PLACE 0,0,SOUTH')
        self.assertEqual(CoordinateValidations.place_cmd_validation('PLACE 0,0,EAST'),'PLACE 0,0,EAST')
        self.assertEqual(CoordinateValidations.place_cmd_validation('PLACE 0,0,WEST'),'PLACE 0,0,WEST')
        self.assertEqual(CoordinateValidations.place_cmd_validation('PLACE 4,3,WEST'),'PLACE 4,3,WEST')
        self.assertEqual(CoordinateValidations.place_cmd_validation('PLACE 2,2,EAST'),'PLACE 2,2,EAST')

    def test_invalid_place_command_validator(self):
        self.assertRaises(IncorrectPlaceException,CoordinateValidations.place_cmd_validation,"PLACE 0,0,INVALID")
        self.assertRaises(IncorrectPlaceException,CoordinateValidations.place_cmd_validation,"PLACE -1,0,NORTH")
        self.assertRaises(IncorrectPlaceException,CoordinateValidations.place_cmd_validation,"PLACE 0,-1,NORTH")
        self.assertRaises(IncorrectPlaceException,CoordinateValidations.place_cmd_validation,"PLACE 0,0,1,NORTH")
        self.assertRaises(IncorrectPlaceException,CoordinateValidations.place_cmd_validation,"PLACE 5,0,NORTH")
        self.assertRaises(IncorrectPlaceException,CoordinateValidations.place_cmd_validation,"PLACE 0,5,NORTH")
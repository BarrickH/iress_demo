from app.coordinate import Coordinate
from app.validations import CoordinateValidations as cv
from app.validations import place_validator_decorator
from app.exceoptions import IncorrectPlaceException


class Command:
    _directions = ['west', 'north', 'east', 'south', 'west', 'north']
    _move_mapping = {
        'NORTH':{'y':1},
        'EAST':{'x':1},
        'SOUTH':{'y':-1},
        'WEST':{'x':-1},
    }

    def __init__(self, cmd: str,):
        self.placed = False
        self.cmd = cmd
        self.cmd_parts = None
        self.C = Coordinate()

    def go(self, cmd: str) -> None:
        try:
            self.execute_command(cmd)
        except IncorrectPlaceException:
            return
        else:
            return
        finally:
            return

    def execute_command(self,cmd:str) -> None:
        self.cmd = cmd.strip()
        self.cmd_parts = cmd.strip().split(' ')[0]
        move_result_mapping = {
            "PLACE": self.place_robot,
            "RIGHT": self.rotate_robot,
            "LEFT": self.rotate_robot,
            "MOVE": self.move_robot,
            "REPORT": self.robot_report
        }
        if self.cmd_parts not in move_result_mapping.keys():
            raise Exception(str('Unaccepted command'))
        else:
            return move_result_mapping.get(self.cmd_parts)()

    def place_robot(self):
        place_cmd = cv.place_cmd_validation(self.cmd)
        x,y,face = self.C.get_coordinate(place_cmd=place_cmd)
        self.C.place_to_coordinate(x=x,y=y,face=face)
        self.placed = True

    @place_validator_decorator
    def rotate_robot(self, turning:str):
        index_step = 1 if turning == 'right' else -1
        direction_index = self._directions[1:5].index(self.C.current_face_direction) + index_step
        self.C.current_face_direction = self._directions[direction_index]

    @place_validator_decorator
    def move_robot(self):
        move_effect = self._move_mapping[self.C.current_face_direction]
        x = move_effect.get('x', 0)
        y = move_effect.get('y', 0)
        self.C.move_in_coordinate(x=x,y=y)

    @place_validator_decorator
    def robot_report(self):
        print(self.C)
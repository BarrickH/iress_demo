from app.coordinate import Coordinate
from app.decorator_validators import place_validator, move_validator
from app.validations import CoordinateValidations as cv


class Command:
    _directions = ['west', 'north', 'east', 'south', 'west', 'north']
    _move_mapping = {
        'NORTH':{'y':1},
        'EAST':{'x':1},
        'SOUTH':{'y':-1},
        'WEST':{'x':-1},
    }

    def __init__(self, cmd: str):
        self.placed = False
        self.cmd = cmd
        self.C = Coordinate()

    @place_validator
    @move_validator
    def execute_command(self) -> None:
        move_result = {
            "RIGHT": self.face_to('right'),
            "LEFT": self.face_to('left'),
            "MOVE": self.next_move(),
            "REPORT": self.report()
        }
        if self.cmd not in move_result.keys():
            raise Exception(str('command error'))
        else:
            return move_result.get(self.cmd)

    def place_robot(self, cmd):
        place_cmd = cv.place_cmd_validation(cmd)
        x,y,face = self.C.get_coordinate(place_cmd)
        self.C.place_to_coordinate(x,y,face)

    def face_to(self, turning):
        index_step = 1 if turning == 'right' else -1
        direction_index = self._directions[1:5].index(self.C.current_face_direction) + index_step
        self.C.current_face_direction = self._directions[direction_index]

    def next_move(self):
        move_effect = self._move_mapping[self.C.current_face_direction]
        x = move_effect.get('x', 0)
        y = move_effect.get('y', 0)
        self.C.move_in_coordinate(x=x,y=y)

    def report(self):
        print(self.C)
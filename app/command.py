from app.validators import place_validator, move_validator


class Command:
    _directions = ['west', 'north', 'east', 'south', 'west', 'north']

    def __init__(self, cmd: str):
        self.placed = False
        self.cmd = cmd

        self.current_position = []
        self.next_position = []
        self.face_direction = ''
        self.face_direction_last = 'north'
        pass

    @place_validator
    @move_validator
    def execute_command(self) -> None:
        move_result = {
            "right": self.face_to('right'),
            "left": self.face_to('left'),
            "move": self.next_move(),
            "report": self.report()
        }
        if self.cmd not in move_result.keys():
            raise Exception(str('command error'))
        else:
            return move_result[self.cmd]

    def face_to(self, turning):
        index_step = 1 if turning == 'right' else -1
        direction_index = self._directions[1:5].index(self.face_direction_last) + index_step
        self.face_direction = self._directions[direction_index]

    def next_move(self):
        self.current_position

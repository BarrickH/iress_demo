import unittest
from app.command import Command
from unittest.mock import patch
from io import StringIO


def get_file_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return [line.replace('\n', '') for line in lines]


class RunTest(unittest.TestCase):
    def setUp(self):
        self.command = Command('')
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_run_1(self, mock_stdout):
        commands = get_file_lines('e2e_test_1.txt')
        for cmd in commands:
            self.command.go(cmd)
        assert mock_stdout.getvalue() == '0,0,NORTH\n0,1,NORTH\n1,1,EAST\n1,2,NORTH\n'

    @patch('sys.stdout', new_callable=StringIO)
    def test_run_2(self, mock_stdout):
        cmd_list = ["PLACE 10,10,NORTH", "REPORT", "PLACE 4,4,NORTH", "MOVE", "REPORT", "RIGHT", "RIGHT", "MOVE",
                    "REPORT", ]
        e2e_test_file = open("e2e_test_2.txt", "w")
        for c in cmd_list:
            e2e_test_file.write(c + "\n")
        e2e_test_file.close()
        commands = get_file_lines('e2e_test_2.txt')
        for cmd in commands:
            self.command.go(cmd)
        assert mock_stdout.getvalue() == '4,4,NORTH\n4,3,SOUTH\n'

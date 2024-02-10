#!/usr/bin/python3
"""console.py TESTS"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """TESTING console.py file"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        """TESTING quit command"""
        console = HBNBCommand()
        self.assertTrue(console.onecmd('quit'))
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command(self, mock_stdout):
        """TESTING help command"""
        console = HBNBCommand()
        console.onecmd('help')
        self.assertIn("Documented commands", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        """TESTING create command"""
        console = HBNBCommand()
        console.onecmd('create BaseModel')
        self.assertNotEqual(mock_stdout.getvalue(), '')


    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_command(self, mock_stdout):
        """TESTING invalid command"""
        console = HBNBCommand()
        console.onecmd('invalid_command')
        self.assertIn("No such command", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()

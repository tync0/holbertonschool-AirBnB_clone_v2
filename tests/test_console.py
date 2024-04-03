from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import sys
from models import type_of_storage


class TestConsole(TestCase):
    """
    Unittests for command line interpreter of project.
    """

    def setUp(self):
        """Setup of interpreter"""
        self.interpreter = HBNBCommand()

    def test_emptyline(self):
        """If input is emptyline"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.interpreter.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_exists(self):
        """checking for docstrings i think"""
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    @classmethod
    def get_S(cls):
        """get stringio value and close"""
        temp_out = StringIO()
        sys.stdout = temp_out
        return temp_out.getvalue()

    def test_create_error(self):
        """test if create works right"""
        temp_out = StringIO()
        sys.stdout = temp_out

        self.interpreter.onecmd("create")
        self.assertEqual(temp_out.getvalue(), '** class name missing **\n')
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        HBNBCommand().do_create("base")
        self.assertEqual(temp_out.getvalue(), '** class doesn\'t exist **\n')
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        if type_of_storage != "db":
            HBNBCommand().do_create("BaseModel")
            self.assertTrue(temp_out.getvalue() != "")
        temp_out.close()
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()

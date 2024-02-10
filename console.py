#!/usr/bin/python3
import cmd
import json
import shlex
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
"""hbnb command"""


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        print("")  # Print a new line before exiting
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = shlex.split(arg)
        class_name = arg_list[0]

        try:
            obj = eval(class_name)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        arg_list = shlex.split(arg)
        class_name = arg_list[0]

        try:
            obj_id = arg_list[1]
            obj = BaseModel.load_from_file().get(class_name + "." + obj_id)
            if obj:
                print(obj)
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = shlex.split(arg)
        class_name = arg_list[0]

        if class_name in ["BaseModel", "User", "State", "Review"]:
            if len(arg_list) < 2:
                print("** instance id missing **")
                return

            obj_id = arg_list[1]
            objs = BaseModel.load_from_file()
            objs.update(User.load_from_file())
            objs.update(State.load_from_file())
            objs.update(Review.load_from_file())

            try:
                del objs[class_name + "." + obj_id]
                BaseModel.save_to_file(objs)
            except KeyError:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        arg_list = shlex.split(arg)
        class_name = arg_list[0]

        if class_name in ["BaseModel", "User", "State", "Review"]:
            if len(arg_list) < 2:
                print("** instance id missing **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()

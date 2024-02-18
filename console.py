#!/usr/bin/python3
"""hbnb command definition"""
import cmd
import json
import shlex
import sys
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models import storage


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

        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return

        class_name = arg_list[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(arg_list) == 1:
            print("** instance id missing **")
            return

        obj_id = arg_list[1]
        objs = BaseModel.load_from_file()
        key = class_name + "." + obj_id
        obj = objs.get(key)

        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return

        class_name = arg_list[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(arg_list) == 1:
            print("** instance id missing **")
            return

        obj_id = arg_list[1]
        objs = BaseModel.load_from_file()
        key = class_name + "." + obj_id

        if key in objs:
            del objs[key]
            BaseModel.save_to_file(objs)
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        objs = BaseModel.load_from_file()
        key = class_name + "." + obj_id

        if key not in objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]
        obj = objs[key]

        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass

        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(obj) for obj in storage.all().values()])
            return

        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name in ["BaseModel", "User", "State", "Review"]:
            print([str(obj) for key, obj in storage.all().items()
                   if key.split('.')[0] == class_name])
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

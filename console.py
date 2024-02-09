#!/usr/bin/python3
import cmd
import json
import shlex
import sys
from models.base_model import BaseModel
"""hbnb command"""

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")  # Print a new line before exiting
        return True

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

         if len(arg_list) < 2:
            print("** instance id missing **")
            return

         try:
            obj_id = arg_list[1]
            obj = BaseModel.load_from_file().get(class_name + "." + obj_id)
            if obj:
                del BaseModel.load_from_file()[class_name + "." + obj_id]
                BaseModel.save_to_file()
            else:
                print("** no instance found **")
         except NameError:
                print("** class doesn't exist **")





if __name__ == '__main__':
    HBNBCommand().cmdloop()

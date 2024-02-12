#!/usr/bin/python3
"""hbnb command definition"""
import cmd
import shlex
import json
import sys
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
        arg_list = shlex.split(arg)
        class_name = arg_list[0]

        try:
            obj = eval(class_name)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def load_all_instances(self):
        """Load all instances from storage"""
        objs = BaseModel.load_from_file()
        objs.update(User.load_from_file())
        objs.update(State.load_from_file())
        objs.update(Review.load_from_file())
        return objs

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        arg_list = shlex.split(arg)
        class_name = arg_list[0]

        if len(arg_list) < 2:
            print("** instance id missing  **")
            return

        if class_name not in ["BaseModel", "User", "State", "Review"]:
            print("** class doesn't exist **")
            return

        obj_id = arg_list[1]
        objs = storage.all()

        key = class_name + "." + obj_id
        obj = objs.get(key)

        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg_list = shlex.split(arg)

        if len(arg_list) == 0:
            print("** class name missing **")
            return

        class_name = arg_list[0]

        if class_name not in ["BaseModel", "User", "State", "Review"]:
            print("** class doesn't exist **")
            return

        if len(arg_list) == 1:
            print("** instance id missing **")
            return

        obj_id = arg_list[1]
        objs = storage.all()
        key = "{}.{}".format(class_name, obj_id)

        if key not in objs:
            print("** no instance found **")
            return

        try:
            del objs[key]
            storage.save()
        except Exception as e:
            print("Error deleting instance:", e)

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

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        count = sum(1 for obj in storage.all().values() if isinstance(
            obj, eval(class_name)))
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

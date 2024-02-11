#!/usr/bin/python3
"""hbnb command definition"""
import cmd
import models
import json
import shlex
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
        try:
            class_name = arg.split()[0]
            obj = eval(class_name)()
            storage.new(obj)
            storage.save()
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

        if class_name not in ["BaseModel", "User", "State", "Review"]:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        obj_id = arg_list[1]
        objs = BaseModel.load_from_file()
        objs.update(User.load_from_file())
        objs.update(State.load_from_file())
        objs.update(Review.load_from_file())

        obj = objs.get(class_name + "." + obj_id)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        obj = storage.get(class_name, instance_id)
        if obj:
            obj.delete()
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        obj = storage.get(class_name, instance_id)
        if not obj:
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
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        arg_list = arg.split('.')
        if len(arg_list) != 2:
            print("*** Unknown syntax:", arg)
            return
        class_name = arg_list[0]
        method = arg_list[1]
        if method != "all()":
            print("*** Unknown syntax:", arg)
            return
        try:
            class_obj = getattr(models, class_name)
            instances = class_obj.all()
            print(instances)
        except AttributeError:
            print("** class doesn't have 'all()' method **")

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split('.')
        if len(arg_list) != 2:
            print("*** Unknown syntax:", arg)
            return

        class_name = arg.split()[0]
        method = arg_list[1]
        if method != "count()":
            print("*** Unknown syntax:", arg)
            return

        try:
            class_obj = getattr(models, class_name)
            count = class_obj.count()
            print(count)
        except AttributeError:
            print("** class doesn't have 'count()' method **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""hbnb command definition"""
import cmd
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
        arg_list = shlex.split(arg)
        class_name = arg_list[0]

        try:
            obj = eval(class_name)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def load_instances(self, class_name):
        """Load instances of the specified class from storage"""
        if class_name == "BaseModel":
            return BaseModel.load_from_file()
        elif class_name == "User":
            return User.load_from_file()
        elif class_name == "State":
            return State.load_from_file()
        elif class_name == "Review":
            return Review.load_from_file()
        else:
            return {}

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        arg_list = shlex.split(arg)
        if len(arg_list) != 2:
            print("** invalid syntax: show <class name> <instance id> **")
            return

        class_name, obj_id = arg_list

        if class_name not in ["BaseModel", "User", "State", "Review"]:
            print("** class doesn't exist **")
            return

        if not obj_id:
            print("** instance id missing **")
            return

        objs = load_instances(class_name)
        obj = objs.get(obj_id)

        if obj:
            print(obj)
        else:
            print("** no instance found **")

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
        i = 0
        for obj in storage.all().values():
            if class_name == obj.__class__.__name__:
                i += 1

        print(i)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

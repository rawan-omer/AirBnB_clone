#!/usr/bin/python3
"""hbnb command definition"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the program."""
        return True

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D) to exit the program."""
        print("")  # Print a new line before exiting
        return True

    def emptyline(self):
        """Override default behavior for empty input."""
        pass

    def do_create(self, arg):
        """Create a new instance of the specified class."""
        args = shlex.split(arg)
        if len(args) == 0:
            print(" class name missing ")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print(" class doesn't exist ")
            return
        new_instance = storage.classes()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Display the string representation of an instance."""
        args = shlex.split(arg)
        if len(args) < 2:
            print(" class name missing ")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print(" class doesn't exist ")
            return
        if len(args) < 2:
            print(" instance id missing ")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print(" no instance found ")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and ID."""
        args = shlex.split(arg)
        if len(args) < 2:
            print(" class name missing ")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print(" class doesn't exist ")
            return
        if len(args) < 2:
            print(" instance id missing ")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print(" no instance found ")
            return
        del storage.all()[key]
        storage.save()

    def do_update(self, arg):
        """Update an instance based on the class name and ID."""
        args = shlex.split(arg)
        if len(args) < 4:
            print(" class name missing ")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print(" class doesn't exist ")
            return
        if len(args) < 2:
            print(" instance id missing ")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print(" no instance found ")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        obj = storage.all()[key]
        if hasattr(obj, attribute_name):
            try:
                attribute_value = eval(attribute_value)
            except (NameError, SyntaxError):
                pass
            setattr(obj, attribute_name, attribute_value)
            storage.save()
        else:
            print(" no instance found ")

    def do_all(self, arg):
        """Display string representations of all instances."""
        args = shlex.split(arg)
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print(" class doesn't exist ")
            return
        print([str(obj) for key, obj in storage.all().items()
               if key.split('.')[0] == class_name])


if name == 'main':
    HBNBCommand().cmdloop()

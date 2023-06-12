#!/usr/bin/python3
"""
HBNB CLONE
"""

from datetime import datetime
from pickle import FALSE
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import cmd
import sys
import models


class HBNBCommand(cmd.Cmd):
    """
    class hbnb Command
    """
    intro = ''
    prompt = '(hbnb) '
    file = None
    classes = ["BaseModel",
               "User",
               "State",
               "City",
               "Amenity",
               "Place",
               "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        self.close()
        quit()
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        self.close()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """
        create  a new instnce of base model
        """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval("{}()".format(args[0]))
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        show a new instnce of base model
        """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        else:
            all_obj = storage.all()
            id_obj = "{}.{}".format(args[0], args[1])
            item_print = False
            for k, v in all_obj.items():
                if id_obj == k:
                    obj = v
                    print(obj)
                    item_print = True
                    return
            if item_print is False:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instancee of Class Name
        """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            obj = "{}.{}".format(args[0], args[1])
            all_obj = storage.all()
            delete_item = False
            for k in all_obj.keys():
                if obj == k:
                    delete_item = True
            if delete_item:
                del all_obj[obj]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print all string represntation of all instance based
        or not in the class name
        """
        args = arg.split()
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            str_list = []
            verfy_all = False
            for v in storage.all().values():
                if len(args) > 0 and args[0] == v.__class__.__name__:
                    str_list.append(v.__str__())
                    verfy_all = True
                elif len(arg) == 0:
                    str_list.append(v.__str__())
                    verfy_all = True
            if verfy_all:
                print(str_list)
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """
        Update an instnce of Class Name
        """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if len(args) > 4:
            return
        else:
            obj = "{}.{}".format(args[0], args[1])
            all_obj = storage.all()
            update_item = False
            for k, v in all_obj.items():
                if obj == k:
                    update_item = True
                    setattr(all_obj[obj], args[2], args[3])
            if update_item:
                storage.save()
            else:
                print("** no instance found **")

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    HBNBCommand().cmdloop()

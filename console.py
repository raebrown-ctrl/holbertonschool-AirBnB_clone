#!/usr/bin/python3
'''Creating cmd console'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
class_dict = {'BaseModel': BaseModel,
              'User': User,
              'State': State,
              'City': City,
              'Amenity': Amenity,
              'Place': Place,
              'Review': Review}
all_data = storage.all()


class HBNBCommand(cmd.Cmd):
    '''cmd console class'''
    prompt = '(hbnb) '

    def do_quit(self, *args):
        '''write quit to exit'''
        return True

    def do_EOF(self, line):
        '''write EOF to exit'''
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn't execute anything"""
        if self.lastcmd:
            pass

    def do_create(self, line):
        '''Creates a new instance of BaseModel'''
        if not line:
            print('** class name missing **')
            return
        if line not in class_dict.keys():
            print("** class doesn't exist **")
            return
        inst_to_create = class_dict.get(line, None)()
        inst_to_create.save()
        print(inst_to_create.id)

    def do_show(self, line):
        '''Prints the string representation of
         an instance based on the class name and id'''
        if not line:
            print('** class name missing **')
            return

        args = line.split()

        if args[0] not in class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return

        obj = args[0] + '.' + args[1]

        for k, v in all_data.items():
            if k == obj:
                print(v)
                return
        print('** no instance found **')

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        if not line:
            print('** class name missing **')
            return

        args = line.split()

        if args[0] not in class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return

        obj = f'{args[0]}.{args[1]}'

        try:
            all_data.pop(obj)
        except KeyError:
            print('** no instance found **')
            return
        storage.save()

    def do_all(self, line):
        '''Prints all string representation of
         all instances based or not on the class name'''
        new_list = []
        check = False

        if not line:
            for k, v in all_data.items():
                new_list.append(str(v))

            print(new_list)
            return
        else:
            args = line.split()
            for k, v in all_data.items():
                obj_type = k.split('.')
                if obj_type[0] == args[0]:
                    new_list.append(str(v))
                    check = True
            if check:
                print(new_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        '''Updates an instance based on the class name
         and id by adding or updating attribute'''
        if not line:
            print('** class name missing **')
            return

        args = line.split()

        if args[0] not in class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return

        obj = f'{args[0]}.{args[1]}'
        inst_found = False

        for k, v in all_data.items():
            if k == obj:
                inst_found = v

        if not inst_found:
            print('** no instance found **')
            return

        if len(args) < 3:
            print('** attribute name missing **')
            return
        if len(args) < 4:
            print('** value missing **')
            return

        setattr(inst_found, args[2], args[3])

        inst_found.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

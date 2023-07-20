#!/usr/bin/python3
"""imports"""


import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from datetime import datetime
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


"""the entry point of the command interpreter"""
class_name = {'BaseModel': BaseModel, 'User': User,
              'State': State, 'City': City, 'Amenity': Amenity,
              'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """class creation"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Finish the execution of the program"""
        return True

    def emptyline(self):
        """empty line that execute anything"""
        pass

    def do_create(self, line):
        """Create a new instance in BaseModel"""
        # take out the arguments from line and
        # assign in a variable
        argv = line.split()
        # take out the number from arguments
        argc = len(argv)
        if argc == 0:
            print("** class name missing **")
        else:
            if argv[0] in class_name:
                new_inst = class_name[argv[0]]()
                storage.new(new_inst)
                new_inst.save()
                print(new_inst.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation"""
        argv = line.split()
        argc = len(argv)
        if argc == 0:
            print("** class name missing **")
        else:
            if argv[0] in class_name:
                if argc == 2:
                    # copy dictionary
                    inst = storage.all()
                    key_ref = argv[0] + "." + argv[1]
                    if key_ref in inst:
                        print(inst[key_ref])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """ Deletes an istances based on the class name id """
        argv = line.split()
        argc = len(argv)
        if argc == 0:
            print("** class name missing **")
        else:
            if argv[0] in class_name:
                if argc == 2:
                    inst = storage.all()
                    key_ref = argv[0] + "." + argv[1]
                    if key_ref in inst:
                        del inst[key_ref]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation"""
        argv = line.split()
        argc = len(argv)
        inst = storage.all()
        if argc == 0:
            all_list = []
            for k, v in inst.items():
                all_list.append(str(v))
            print(all_list)
        else:
            if argv[0] in class_name:
                new_list = []
                for k, v in inst.items():
                    if argv[0] == type(v).__name__:
                        new_list.append(str(v))
                print(new_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """ update - update a object and add attributes
        use - 'update [NAME_OBJECT] [ID] [ATTRIBUTE_NAME] "[ATTRIBUTE_VALUE]"'
        """
        # Create argc and argv
        argv = line.split()
        argc = len(argv)
        # List to attributes to not edit
        # Verify if the input are empty
        if argc == 0:
            print("** class name missing **")

        # If not empty but no find in base the
        # argv[0] = BaseModel
        if argv[0] not in class_name:
            print("** class doesn't exist **")

        # Verify if only the [NAME_OBJECT] fits
        if argc == 1:
            print("** instance id missing **")

        # If argv[2] (ATTRIBUTE_NAME) no are in
        # to_not_edit execute
        # Load all obects
        inst = storage.all()
        # Construct the key according to
        # parameters
        key_ref = argv[0] + "." + argv[1]
        # Verify if the key_ref exists in instances
        if key_ref in inst.keys():
            obj_in = inst[key_ref]
            if argc == 2:
                print("** attribute name missing **")
            elif argc == 3:
                print("** value missing **")
            else:
                obj_in.__dict__[argv[2]] = argv[3][1:-1]
                obj_in.updated_at = datetime.now()
                storage.save()
        else:
            print("** no instance found **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()

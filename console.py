#!/usr/bin/python3
"""imports"""


import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from datetime import datetime


"""the entry point of the command interpreter"""
class_name = {'BaseModel': BaseModel}

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
        #take out the arguments from line and 
        #assign in a variable
        argv = line.split()
        #take out the number from arguments
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

    def do_all(self, line):
        """ select all objects and return all attributes of NAME_OBJECT
        use 'all [NAME_OBJECT]' - NAME_OBJECT is any name of de object
        """
        # Get the argc and argv
        argv = line.split()
        argc = len(argv)
        # Load all the obects in instances
        instances = storage.all()
        # Verify if len of argc is equal to 0
        if argc == 0:
            # Create a empty list for all instances
            list_for_all = []
            for key, obj in instances.items():
                list_for_all.append(str(obj))
            print(list_for_all)
            return
        # Verify if class not exist in class_name
        if argv[0] not in class_name:
            print("** class doesn't exist **")
            return
        # If not - exist
        else:
            # Create new list
            new_list = []
            # Iterate in key and obj
            for key, obj in instances.items():
                # Example if BaseModel is the type of
                # type(obj).__name__ this is equal a
                # BaseModel
                if argv[0] == type(obj).__name__:
                    # Append the string of object
                    new_list.append(str(obj))
            # Print the new list
            print(new_list)

    def do_destroy(self, line):
        """Delete an instance based on the class name and id
        use - 'destroy [NAME_OBJECT] [ID]'
        """
        # Splits line by the spaces
        argv = line.split()
        argc = len(argv)
        # if no arguments happen
        if argc == 0:
            print("** class name missing **")
            return
        if argv[0] not in class_name:
            print("** class doesn't exist **")
            return
        if argc == 1:
            print("** instance id missing **")
            return
        # Get all instances
        instances = storage.all()
        key_ref = argv[0] + "." + argv[1]
        if key_ref in instances.keys():
            del instances[key_ref]
            storage.save()
            return
            # if it does not exist
        else:
            print("** no instance found **")

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
            return
        # If not empty but no find in class_name the
        # argv[0] = BaseModel
        if argv[0] not in class_name:
            print("** class doesn't exist **")
            return
        # Verify if only the [NAME_OBJECT] fits
        if argc == 1:
            print("** instance id missing **")
            return
        # If argv[2] (ATTRIBUTE_NAME) no are in
        # to_not_edit execute
        # Load all obects
        instances = storage.all()
        # Construct the key according to
        # parameters
        key_ref = argv[0] + "." + argv[1]
        # Verify if the key_ref exists in instances
        if key_ref in instances.keys():
            obj_in = instances[key_ref]
            if argc == 2:
                print("** attribute name missing **")
                return
            elif argc == 3:
                print("** value missing **")
                return
            else:
                obj_in.__dict__[argv[2]] = argv[3][1:-1]
                obj_in.updated_at = datetime.now()
                storage.save()
        else:
            print("** no instance found **")
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
#!/usr/bin/python3
"""imports"""


import cmd


"""the entry point of the command interpreter"""
class HBNBCommand(cmd.Cmd):
    """class creation"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exit the interprete terminal"""
        return True

    def do_EOF(self, line):
        """Finish the execution of the program"""
        return True

    def empty_line(self, line):
        """empty line that execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
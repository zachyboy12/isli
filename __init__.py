from sys import argv as __argv
__pairs = None
args = __argv[1:]
options_help = '''Options:
'''
description = ''
usage = ''


def command(typename='STR'):
    def inner(func):
        global __pairs, options_help
        options_help += f'   {func.__name__.replace("_", "-")}: {typename} - {func.__doc__}\n'
        if __pairs is None:
            __pairs = {func.__name__.replace('_', '-'): func}
        else:
            __pairs[func.__name__.replace('_', '-')] = func
    return inner


def start():
    global __pairs, options_help, usage, args, description
    current_arg = -1
    if __argv[1:] == []:
        if usage == '':
            print('\n' + description + f'\n\nUsage: {__argv[0]} [OPTIONS]\n\n\n' + options_help + '   -help, -h - Show this message and exit.\n')
        else:
            print('\n' + description + f'\n\nUsage: {usage}\n\n\n' + options_help + '   -help, -h - Show this message and exit.\n')
    else:
        for arg in args:
            current_arg += 1
            if arg in __pairs:
                try:
                    __pairs[arg](args[current_arg + 2])
                except (IndexError, ValueError):
                    __pairs[arg](args[current_arg + 1])
                except TypeError:
                    __pairs[arg]()
            else:
                if arg == '-help' or arg == '-h':
                    if usage == '':
                        print('\n' + description + f'\n\nUsage: {__argv[0]} [OPTIONS]\n\n\n' + options_help + '   -help, -h - Show this message and exit.\n')
                    else:
                        print('\n' + description + f'\n\nUsage: {usage}\n\n\n' + options_help + '   -help, -h - Show this message and exit.\n')
                else:
                    pass
            
            
def search_arg(arg_name: str):
    global args
    return args[args.index(arg_name)]

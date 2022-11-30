from random import randint
from typing import Callable


def log(pattern: str = None) -> Callable:
    """
    Takes parameters for decorating the fuction
    :param pattern: string, into which random time values are substituted
    :return: Callable, decorated function
    """
    def outer_wrapper(func: Callable) -> Callable:
        """
        Decorates the function
        :param func: Callable, original function
        :return: Callable, decorated function
        """
        def inner_wrapper(*args, **kwargs):
            """
            Changes the behavior of the working of the function
            :param args: params of original function
            :param kwargs: params of original function
            """
            time = randint(1, 30)
            if pattern is None:
                print(f'{func.__name__} - {time} min!')
            else:
                parts = pattern.split('{')
                for i in range(1, len(parts)):
                    if parts[i][0] != '}':
                        pos = int(parts[i][0])
                        parts[i] = f'{args[pos]}{parts[i].split("}")[1]}'
                    else:
                        parts[i] = f'{time}{parts[i].split("}")[1]}'
                print(''.join(parts))
        return inner_wrapper
    return outer_wrapper

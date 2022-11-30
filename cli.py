import click
from random import randint
from main import Margherita, Pepperoni, Hawaiian
from log import log

PIZZAS = {'margherita': Margherita,
          'pepperoni': Pepperoni,
          'hawaiian': Hawaiian}


@log()
def bake(order_id: int, pizza: str):
    """
    Bakes the pizza from the order with number order_id
    Prints the message with this information
    :param order_id: int, the number of the order
    :param pizza: string, the name of the pizza that was ordered
    """
    print(f'Bake your order #{order_id} (pizza {pizza})')


@log('\U0001F69A Deliver your order #{0} to {1} in {} minutes!')
def deliv(order_id: int, address: str):
    """
    Delivers the order with number order_id to address specified by the user
    Prints the message with this information
    :param order_id: int, the number of the order
    :param address: string, the address which user specified in the order,
    where the pizza should be delivered
    """
    print(f'Delivery your order #{order_id} by the address {address}')


@log('\U0001F3E0 Please pick your order #{0} within {} minutes!')
def pickup(order_id: int):
    """
    Prints the message with information that the order with number order_id
    is ready and needed to pick up from Pizzeria
    :param order_id: int, the number of the order
    """
    print(f'Please pick your order #{order_id}!')


@click.group()
def cli():
    pass


@cli.command()
@click.option('--size', required=True,
              help='Specify the pizza size')
@click.option('--delivery', default=None,
              help='If you want to arrange delivery, '
                   'enter --delivery and address as argument in ""')
@click.argument('pizza', nargs=1)
def order(pizza: str, size: str, delivery: str):
    """
    Places an order made by the user, assigns a number to it, submits it for
    baking, and after it's ready, arranges either pickup or delivery
    to the address specified by the user
    :param pizza: string, the name of the pizza which user ordered
    :param size: string, the size of the pizza which user ordered
    :param delivery: string, address typed by user
    where pizza should be delivered
    """

    if pizza.lower() not in PIZZAS:
        raise ValueError('We have not this pizza, sorry')

    order_id = randint(0, 10**4)
    pizza_order = PIZZAS[pizza.lower()](size.upper())

    print(f'Order #{order_id} (pizza {pizza_order.name}) accepted. Wait...')
    bake(order_id, pizza)
    if delivery is None:
        pickup(order_id)
    else:
        deliv(order_id, delivery)


@cli.command()
@click.option('--values', default=None,
              help='If you want to check the values of ingredients, '
                   'enter --values and specify pizza size')
def menu(values: str = None):
    """
    Prints the menu of Pizzeria in two forms:
    - short with name of pizza, its icon, list of ingredients
    and available sizes
    - extended with name of pizza, its icon and full list of ingredients
    (by grams)
    :param values: specify pizza size if user wants to check
    the values of ingredients
    """

    if values is None:
        print(f'{repr(Margherita())}\n{repr(Pepperoni())}\n{repr(Hawaiian())}')
    else:
        size = values.upper()
        print(f'{Margherita(size)}\n\n{Pepperoni(size)}\n\n{Hawaiian(size)}')


if __name__ == '__main__':
    cli()

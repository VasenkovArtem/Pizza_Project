import pytest
from main import Pizza, Margherita, Pepperoni, Hawaiian
from click.testing import CliRunner
from cli import menu, order


def test_set_attributes_size_error():
    """
    Testing the setting attributes of the pizza with wrong size
    """
    with pytest.raises(ValueError) as e:
        Margherita(size='ml')
    assert 'No such size! Available sizes: L, XL' in str(e)


def test_set_attributes_properly():
    """
    Testing the setting attributes of the pizza (all attributes are correct)
    """
    pizza = Pepperoni(size='XL')
    assert hasattr(pizza, '_size')
    assert pizza._size == 'XL'
    assert hasattr(pizza, 'tomato_sauce')
    assert pizza.tomato_sauce == 400
    assert hasattr(pizza, 'mozzarella')
    assert pizza.mozzarella == 600
    assert hasattr(pizza, 'pepperoni')
    assert pizza.pepperoni == 1000


@pytest.mark.parametrize(
    'pizza, message',
    [
        (Margherita(size='L'), 'tomato sauce: 250,\nmozzarella: 500,\n'
                               'tomatoes: 300'),
        (Margherita(size='XL'), 'tomato sauce: 400,\nmozzarella: 800,\n'
                                'tomatoes: 500'),
        (Pepperoni(size='L'), 'tomato sauce: 250,\nmozzarella: 400,\n'
                              'pepperoni: 700'),
        (Pepperoni(size='XL'), 'tomato sauce: 400,\nmozzarella: 600,\n'
                               'pepperoni: 1000'),
        (Hawaiian(size='L'), 'tomato sauce: 250,\nmozzarella: 300,\n'
                             'chicken: 400,\npineapples: 200'),
        (Hawaiian(size='XL'), 'tomato sauce: 400,\nmozzarella: 500,\n'
                              'chicken: 700,\npineapples: 500'),
    ],
)
def test_dict_simple(pizza: Pizza, message: str):
    """
    Testing the output of pizza ingredients in the form of simple dictionary
    :param pizza: Pizza, instance of some type of pizza
    :param message: string, right output
    """
    assert pizza.dict() == message


@pytest.mark.parametrize(
    'pizza, message',
    [
        (Margherita(size='L'), 'You need 250 grams of tomato sauce,\n'
                               'You need 500 grams of mozzarella,\n'
                               'You need 300 grams of tomatoes'),
        (Margherita(size='XL'), 'You need 400 grams of tomato sauce,\n'
                                'You need 800 grams of mozzarella,\n'
                                'You need 500 grams of tomatoes'),
        (Pepperoni(size='L'), 'You need 250 grams of tomato sauce,\n'
                              'You need 400 grams of mozzarella,\n'
                              'You need 700 grams of pepperoni'),
        (Pepperoni(size='XL'), 'You need 400 grams of tomato sauce,\n'
                               'You need 600 grams of mozzarella,\n'
                               'You need 1000 grams of pepperoni'),
        (Hawaiian(size='L'), 'You need 250 grams of tomato sauce,\n'
                             'You need 300 grams of mozzarella,\n'
                             'You need 400 grams of chicken,\n'
                             'You need 200 grams of pineapples'),
        (Hawaiian(size='XL'), 'You need 400 grams of tomato sauce,\n'
                              'You need 500 grams of mozzarella,\n'
                              'You need 700 grams of chicken,\n'
                              'You need 500 grams of pineapples'),
    ],
)
def test_dict(pizza: Pizza, message: str):
    """
    Testing the output of pizza ingredients with beautiful decoration
    :param pizza: Pizza, instance of some type of pizza
    :param message: string, right output
    """
    assert pizza.dict(simple=False) == message


@pytest.mark.parametrize(
    'pizza, message',
    [
        (Margherita(size='L'), '- Margherita 🧀:\ntomato sauce: 250,\n'
                               'mozzarella: 500,\ntomatoes: 300'),
        (Margherita(size='XL'), '- Margherita 🧀:\ntomato sauce: 400,\n'
                                'mozzarella: 800,\ntomatoes: 500'),
        (Pepperoni(size='L'), '- Pepperoni 🍕:\ntomato sauce: 250,\n'
                              'mozzarella: 400,\npepperoni: 700'),
        (Pepperoni(size='XL'), '- Pepperoni 🍕:\ntomato sauce: 400,\n'
                               'mozzarella: 600,\npepperoni: 1000'),
        (Hawaiian(size='L'), '- Hawaiian 🍍:\ntomato sauce: 250,\n'
                             'mozzarella: 300,\nchicken: 400,\n'
                             'pineapples: 200'),
        (Hawaiian(size='XL'), '- Hawaiian 🍍:\ntomato sauce: 400,\n'
                              'mozzarella: 500,\nchicken: 700,'
                              '\npineapples: 500'),
    ],
)
def test_icon_mixin_str(pizza: Pizza, message: str):
    """
    Testing the string representation of pizza with icons from IconMixin
    :param pizza: Pizza, instance of some type of pizza
    :param message: string, right output
    """
    assert str(pizza) == message


@pytest.mark.parametrize(
    'pizza, message',
    [
        (Margherita(), '- Margherita 🧀: tomato sauce, mozzarella, tomatoes. '
                       'Available sizes: L, XL'),
        (Pepperoni(), '- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni. '
                      'Available sizes: L, XL'),
        (Hawaiian(), '- Hawaiian 🍍: tomato sauce, mozzarella, chicken, '
                     'pineapples. Available sizes: L, XL'),
    ],
)
def test_icon_mixin_repr(pizza: Pizza, message: str):
    """
    Testing the representation of pizza with icons from IconMixin
    :param pizza: Pizza, instance of some type of pizza
    :param message: string, right output
    """
    assert repr(pizza) == message


def test_equal():
    """
    Testing two identical pizzas for equality between each other
    """
    hawaiian_1 = Hawaiian(size='L')
    hawaiian_2 = Hawaiian()
    assert not id(hawaiian_1) == id(hawaiian_2)
    assert hawaiian_1 == hawaiian_2


def test_not_equal():
    """
    Testing two different types of pizza and two different sizes of one type
    of pizza for non-equality between each other
    """
    margherita_l = Margherita(size='L')
    margherita_xl = Margherita(size='XL')
    pepperoni_l = Pepperoni()
    assert not margherita_l == margherita_xl
    assert not margherita_l == pepperoni_l


def test_equal_error():
    """
    Testing of raising error when trying to compare pizza to non-pizza
    """
    pizza = Pepperoni(size='XL')
    with pytest.raises(TypeError) as e:
        pizza == 'pizza'
    assert 'Alas, the object on the right is not a pizza!' in str(e)


@pytest.mark.parametrize(
    'pizza, message',
    [
        (Margherita(), 'Margherita'),
        (Pepperoni('XL'), 'Pepperoni'),
        (Hawaiian(size='L'), 'Hawaiian'),
    ],
)
def test_name(pizza: Pizza, message: str):
    """
    Testing that displaying name of the pizza is right
    :param pizza: Pizza, instance of some type of pizza
    :param message: string, right output
    """
    assert pizza.name == message


def test_cli_menu():
    """
    Testing the working of displaying short menu in the command line
    using click
    """
    message = ('- Margherita 🧀: tomato sauce, mozzarella, tomatoes. '
               'Available sizes: L, XL\n- Pepperoni 🍕: tomato sauce, '
               'mozzarella, pepperoni. Available sizes: L, XL\n- Hawaiian 🍍: '
               'tomato sauce, mozzarella, chicken, pineapples. '
               'Available sizes: L, XL\n')
    runner = CliRunner()
    result = runner.invoke(menu)
    assert result.output == message


@pytest.mark.parametrize(
    'size, message',
    [
        ('l', '- Margherita 🧀:\ntomato sauce: 250,\nmozzarella: 500,\n'
              'tomatoes: 300\n\n- Pepperoni 🍕:\ntomato sauce: 250,\n'
              'mozzarella: 400,\npepperoni: 700\n\n- Hawaiian 🍍:\n'
              'tomato sauce: 250,\nmozzarella: 300,\nchicken: 400,\n'
              'pineapples: 200\n'),
        ('xl', '- Margherita 🧀:\ntomato sauce: 400,\nmozzarella: 800,\n'
               'tomatoes: 500\n\n- Pepperoni 🍕:\ntomato sauce: 400,\n'
               'mozzarella: 600,\npepperoni: 1000\n\n- Hawaiian 🍍:\n'
               'tomato sauce: 400,\nmozzarella: 500,\nchicken: 700,\n'
               'pineapples: 500\n'),
    ],
)
def test_cli_menu_values(size: str, message: str):
    """
    Testing the working of displaying extended menu
    (with values of the ingredients)
    in the command line using click
    :param size: string, the size of pizzas
    :param message: string, right output
    """
    runner = CliRunner()
    result = runner.invoke(menu, ['--values', size])
    assert result.output == message


def test_cli_order_error_argument():
    """
    Testing the working of creating order
    without specifying the size of the pizza
    """
    runner = CliRunner()
    result = runner.invoke(order, ['Pepperoni'])
    assert result.exit_code == 2
    assert "Error: Missing option '--size'." in result.output


def test_cli_order_error_pizza():
    """
    Testing the working of creating order
    with non-available type of the pizza
    """
    runner = CliRunner()
    result = runner.invoke(order, ['Meatballs', '--size', 'ml'])
    assert result.exit_code == 1
    assert "ValueError('We have not this pizza, sorry')" in str(result)


@pytest.mark.parametrize(
    'pizza, size, address, message',
    [
        ('pepperoni', 'l', None, 'Order # (pizza Pepperoni) accepted. '
                                 'Wait...\nbake - min!\n🏠 Please pick '
                                 'your order # within minutes!\n'),
        ('Margherita', 'xl', None, 'Order # (pizza Margherita) accepted. '
                                   'Wait...\nbake - min!\n🏠 Please pick '
                                   'your order # within minutes!\n'),
        ('hawaiian', 'xl', 'Moscow', 'Order # (pizza Hawaiian) accepted. '
                                     'Wait...\nbake - min!\n🚚 Deliver '
                                     'your order # to Moscow in minutes!\n'),
        ('pepperoni', 'xl', 'Russia Moscow Avito',
         'Order # (pizza Pepperoni) accepted. Wait...\nbake - min!\n'
         '🚚 Deliver your order # to Russia Moscow Avito in minutes!\n'),
    ],
)
def test_cli_order(pizza: str, size: str, address: str, message: str):
    """
    Testing the process of ordering with correct different parameters
    :param pizza: str, name of some type of pizza
    :param size: string, the size of ordered pizza
    :param address: string, address of the place
    where pizza should be delivered
    :param message: string, right output
    """
    runner = CliRunner()
    if address is None:
        result = runner.invoke(order, [pizza, '--size', size])
        out = result.output
        end_num_1 = out.find('(')
        start_time_1 = out.find('bake - ')
        end_time_1 = out.find('min')
        start_num_2 = out.find('order #')
        end_num_2 = out.find('within')
        end_time_2 = out.find('minutes')
        clean_out = (f'{out[:7:]}{out[end_num_1-1:start_time_1+7]}'
                     f'{out[end_time_1:start_num_2+7]}'
                     f'{out[end_num_2-1:end_num_2+7]}'
                     f'{out[end_time_2:]}')
    else:
        result = runner.invoke(order, [pizza, '--size', size, '--delivery',
                                       address])
        out = result.output
        end_num_1 = out.find('(')
        start_time_1 = out.find('bake - ')
        end_time_1 = out.find('min')
        start_num_2 = out.find('order #')
        end_num_2 = out.find('to')
        start_time_2 = out.find('in ')
        end_time_2 = out.find('minutes')
        clean_out = (f'{out[:7:]}{out[end_num_1 - 1:start_time_1 + 7]}'
                     f'{out[end_time_1:start_num_2 + 7]}'
                     f'{out[end_num_2 - 1:start_time_2 + 3]}'
                     f'{out[end_time_2:]}')
    assert clean_out == message


if __name__ == '__main__':
    test_set_attributes_size_error()
    test_set_attributes_properly()
    test_dict_simple()
    test_dict()
    test_icon_mixin_str()
    test_icon_mixin_repr()
    test_equal()
    test_not_equal()
    test_equal_error()
    test_name()
    test_cli_menu()
    test_cli_menu_values()
    test_cli_order_error_argument()
    test_cli_order_error_pizza()
    test_cli_order()

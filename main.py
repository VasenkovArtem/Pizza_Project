from abc import ABC


class IconPizzaMixin:
    """
    Specifies a string representation to display to users the name
    of the pizza, its icon and ingredients (by grams). Also supports
    displaying a representation of different types of pizza in the form of
    its name, icon, list of ingredients and available sizes
    """

    ICONS_PIZZA = {
        'Margherita': '\U0001F9C0',
        'Pepperoni': '\U0001F355',
        'Hawaiian': '\U0001F34D',
    }

    def __str__(self) -> str:
        """
        Displays a string representation of the name of pizza,
        its icon and ingredients (by grams)
        Used for extended menu
        :return: string with name, icon and ingredients (by grams) of pizza
        """
        name_of_pizza = self.name
        icon = self.ICONS_PIZZA[name_of_pizza]
        return f'- {name_of_pizza} {icon}:\n{self.dict()}'

    def __repr__(self) -> str:
        """
        Displays the name of the pizza, its icon and list of ingredients
        Used for short menu
        :return: string with name, icon, list of ingredients of pizza and
        its available sizes
        """
        name_of_pizza = self.name
        icon = self.ICONS_PIZZA[name_of_pizza]
        message_ingredients = ", ".join(self.ingredients).replace("_", " ")
        message_sizes = ", ".join(self.AVAILABLE_SIZES)
        return (f'- {name_of_pizza} {icon}: {message_ingredients}. '
                f'Available sizes: {message_sizes}')


class Pizza(IconPizzaMixin, ABC):
    """
    Represents an abstract pizza class, creates attributes of the
    corresponding ingredients in initialization, can display the composition
    of the pizza in the form of dictionary and compare pizzas with each other
    by type and size
    """

    AVAILABLE_SIZES = ['L', 'XL']

    def _setattributes(self, size: str):
        """
        Creates a pizza instance, checks the entered size against available
        sizes and creates instance attributes corresponding
        to the pizza ingredients and their values
        :param size: string, size of the pizza typed by the user
        """
        message_sizes = ", ".join(self.AVAILABLE_SIZES)
        assert size in self.AVAILABLE_SIZES, (f'No such size! Available '
                                              f'sizes: {message_sizes}.')
        setattr(self, '_size', size)
        for ingredient in self.ingredients:
            value = getattr(type(self), ingredient)[self._size]
            setattr(self, ingredient, value)

    def dict(self, simple=True):
        """
        Prints the composition of the pizza as a dictionary
        Supports beautiful text output design
        :param simple: boolean, specifies whether the output should
        only contain the information about the ingredients and their values
        or whether to add nice text decoration to the output
        :return: string, the composition of the pizza in the chosen style
        """
        output = ''
        if simple:
            for ingredient in self.ingredients:
                output += (f'{ingredient.replace("_", " ")}: '
                           f'{getattr(self, ingredient)},\n')
        else:
            for ingredient in self.ingredients:
                output += (f'You need {getattr(self, ingredient)} grams of '
                           f'{ingredient.replace("_", " ")},\n')
        return output[:-2]

    def __eq__(self, other):
        """
        Checks instances of pizzas among themselves for similarity in type
        and size. Raises a TypeError if the second comparison instance
        is not a pizza
        :param other: object to compare
        :return: boolean, the result of comparison of two pizzas
        between each other (by type and size)
        """
        if not isinstance(other, Pizza):
            raise TypeError('Alas, the object on the right is not a pizza!')
        return (type(self) == type(other)) and (self._size == other._size)

    @property
    def name(self) -> str:
        """
        Returns the name of the class of the object (type of the pizza)
        :return: string, the name of the class of the object
        """
        return type(self).__name__


class Margherita(Pizza):
    """
    Describes the pizza Margherita, specifically the ingredients and its
    amounts needed for different sizes
    """

    ingredients = ['tomato_sauce', 'mozzarella', 'tomatoes']
    tomato_sauce = {'L': 250, 'XL': 400}
    mozzarella = {'L': 500, 'XL': 800}
    tomatoes = {'L': 300, 'XL': 500}

    def __init__(self, size: str = 'L'):
        """
        Sets the attributes to the created instance of pizza Margherita
        (size and ingredients with its amounts)
        :param size: string, the size of the pizza
        """
        super()._setattributes(size)


class Pepperoni(Pizza):
    """
    Describes the pizza Pepperoni, specifically the ingredients and its
    amounts needed for different sizes
    """

    ingredients = ['tomato_sauce', 'mozzarella', 'pepperoni']
    tomato_sauce = {'L': 250, 'XL': 400}
    mozzarella = {'L': 400, 'XL': 600}
    pepperoni = {'L': 700, 'XL': 1000}

    def __init__(self, size: str = 'L'):
        """
        Sets the attributes to the created instance of pizza Pepperoni
        (size and ingredients with its amounts)
        :param size: string, the size of the pizza
        """
        super()._setattributes(size)


class Hawaiian(Pizza):
    """
    Describes the pizza Hawaiian, specifically the ingredients and its
    amounts needed for different sizes
    """

    ingredients = ['tomato_sauce', 'mozzarella', 'chicken', 'pineapples']
    tomato_sauce = {'L': 250, 'XL': 400}
    mozzarella = {'L': 300, 'XL': 500}
    chicken = {'L': 400, 'XL': 700}
    pineapples = {'L': 200, 'XL': 500}

    def __init__(self, size: str = 'L'):
        """
        Sets the attributes to the created instance of pizza Hawaiian
        (size and ingredients with its amounts)
        :param size: string, the size of the pizza
        """
        super()._setattributes(size)


if __name__ == '__main__':
    pizza_1 = Margherita('L')
    print(pizza_1)
    pizza_2 = Pepperoni('L')
    print(repr(pizza_2))
    print(pizza_1 == pizza_2)
    pizza_3 = Margherita('L')
    print(pizza_3 == pizza_1)
    pizza_4 = Hawaiian('XL')
    print(pizza_4.dict())

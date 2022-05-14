class Procedure:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2


    def one(var1):
        """

        This function accepts any positive whole number and returns the sum of all whole numbers up to and including the variable

        :param var1: the number provided by the user

        :return: int
        """

        if var1 == 1:
            return 1
        else:
            return var1 + one((var1-1))


    def two(var1, var2):
        """

        This function raises a number to a power

        :param var1: the number to be raised to a power
        :param var2: the exponent

        :return: int
        """

        if var1 == 0:
            return 1
        else:
            var1 ** var2


    def three(var1):
        """

        This function prints out all of the positive whole numbers leading up to that number
        :param var1:

        :return:
        """

        if var1 == 0:
            return 1
        else:
            print(var1, end=' ')
            var1 -= 1
            three(var1)
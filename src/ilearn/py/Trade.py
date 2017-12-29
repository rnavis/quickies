class Trade:
    __product = None
    __qty = 0.0
    __price = 0.0
    __priceType = ""

    def __init__(self, product, qty, price, priceType):
        self.__product = product
        self.__qty = qty
        self.__price = price
        self.__priceType = priceType

    def set_product(self, product):
        self.__product = product

    def get_product(self):
        return self.__product

    def set_qty(self, qty):
        self.__qty = qty

    def get_qty(self):
        return self.__qty

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_priceType(self, priceType):
        self.__priceType = priceType

    def get_priceType(self):
        return self.__priceType

    def get_type(self):
        return "Trade"

    def toString(self):
        return "{} is of {} qty and {} price and priceType {}".format(self.__product,
                                                                        self.__qty,
                                                                        self.__price,
                                                                        self.__priceType)
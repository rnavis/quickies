from Trade import Trade

class Equity(Trade):
    __broker = ""

    def __init__(self, product, qty, price, priceType, broker):
        super(Equity, self).__init__(product, qty, price, priceType)
        self.__broker = broker

    def set_broker(self, broker):
        self.__broker = broker

    def get_broker(self):
        return self.__broker

    def get_type(self):
        return "Equity"

    def toString(self):
        return "{} is of {} product and {} qty and  price {} , {} as the primary broker".format(self.get_product(), self.get_qty(),
                                                                                                self.get_price(), self.get_priceType(),
                                                                                                self.__broker)

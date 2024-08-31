class Store:

    def __init__(self):
        """
        set two dictionaries:
        - warehouse: nested dictionary; for each good will be specified amount, purchase and selling price
        - cash: nested dictionary; describe total amount of purchases and sales; both entries are initialized
                to zero
        """
        self.warehouse = {}
        self.cash = {"purchases": 0, "sales": 0}

    def getStore(self):
        """
        :return: show the warehouse contents
        """
        return self.warehouse

    def inStore(self, good):
        """
        :param good: str -> name of good
        :return: True: if the good is present in the warehouse; False: if the good is not present
        """
        if good in self.warehouse:
            return True
        else:
            return False

    def add(self, name, amount, purchase, sale):
        """
        :param name: str -> name of product
        :param amount: int-> amount of product
        :param purchase: float -> purchasing price
        :param sale: float -> selling price
        :return: warehouse with product added
        """
        self.warehouse[name] = {
            "amount": amount,
            "purchase_price": purchase,
            "selling_price": sale
        }

        return self.warehouse

    def increase(self, good, quantity):
        """
        :param good: product added to warehouse
        :param quantity: product quantity to add to original amount
        :return: warehouse
        increase the amount of good added in warehouse
        """
        self.warehouse[good]["amount"] += quantity

    def decrease(self, good, quantity):
        """
        :param good: product to sell
        :param quantity: quantity of product to sell
        :return: warehouse
        decrease the amount of good to sell in warehouse
        """

        self.warehouse[good]["amount"] -= quantity

    def buy(self, name, quantity):
        """
        :param good: str -> name of good bought
        :param quantity: int -> amount of good bought
        :return: cash dict
        """
        purchase = round(quantity * self.getStore()[name]["purchase_price"], 2)
        self.cash["purchases"] += purchase

        return self.cash

    def inStock(self, good, quantity):
        """
        check if the good to sell is present in warehouse and his amount is available
        :param good: str -> name of  good to sell
        :param quantity: int -> amount to sell
        :return: True if the amount is available; False if it's not available

        """
        try:
            assert(quantity <= self.warehouse[good]["amount"]), "Attention: the request quantity is not available\"" \
                                                                 "in stock"
            return True

        except Exception as e:
            print(e)
            return False

    def sale(self, good, quantity):
        """
        record the sale
        :param good: name of the product to sell
        :param quantity: int -> amount of good to sell
        :return: cash dict
        """

        sale = round(quantity * self.warehouse[good]["selling_price"], 2)
        self.cash["sales"] += sale

        return sale

    def grossProfit(self):
        """
        :return: show the gross profit -> only the sales
        """
        return round(self.cash["sales"], 2)

    def netProfit(self):
        """
        :return: show the net profit -> subtracts purchases from sales
        """

        return round(self.cash["sales"] - self.cash["purchases"], 2)
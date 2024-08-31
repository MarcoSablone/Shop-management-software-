from store import Store

class Actions():
    """
    This class contains the main actions of the market, like:
    - buy a product
    - sell a product
    - show the contents of warehouse
    - show the gross and net profit
    - show the available commands
    - input the commands
    """

    def renderBuy(self, store):
        """
        :param store: object of class Store
        It describes the purchase steps
        :return: print on file the products purchased
        """
        prod_bought = {}  # key = name; value = quantity
        answer_list = ["yes", "no"]
        demand = answer_list[0]

        while demand == "yes":
            name = input("Enter a product: ")

            if store.inStore(name) is False:
                amount = int(input("Enter the amount: "))
                purchase = float(input("Enter purchase price: "))
                sale = float(input("Enter selling price: "))

                store.add(name, amount, purchase, sale)
                store.buy(name, amount)
                prod_bought[name] = amount

                demand = input("Would you buy another product? [yes/no]: ")

            else:
                amount = int(input("Enter the amount: "))
                store.increase(name, amount)
                store.buy(name, amount)
                prod_bought[name] = amount

                demand = input("Would you buy another product? [yes/no]: ")

        with open("Bio Market Sas", "a+", encoding= "utf-8") as f:

            f.write("\n----REGISTERED PURCHASE----\n\n")
            f.write("ADDED:\n\n")

            for key, value in prod_bought.items():
                f.write(f"- N. {value} X {key}\n")


    def renderSale(self, store):
        """
        :param store: object of class Store
        It describes the sale steps
        :return: print on file the products sold and the total cash collected
        """

        prod_sold = {} #key = name; value = {quantity; total sale}
        answer_list = ["yes", "no"]
        demand = answer_list[0]

        while demand == "yes":
            name = input("Enter the product to sell: ")

            if store.inStore(name) is True:
                quantity = int(input("Enter the quantity to sell: "))

                if store.inStock(name, quantity) is True:
                    round( store.sale(name, quantity), 2 )
                    store.decrease(name, quantity)
                    prod_sold[name] = {"quantity": quantity, "sell": store.sale(name, quantity)}

                    total_sold = 0
                    total_sold += store.sale(name, quantity)

                    demand = input("Would you sell another product? [yes/no]: ")

        with open("Bio Market Sas", "a+", encoding= "utf-8") as f:

            f.write("\n-----REGISTERED SALE-----\n\n")

            for key, value in prod_sold.items():
                f.write( "- %d X %s: %f €\n" % ( value["quantity"], key, round(value["sell"], 2) ) )

            f.write(f"\nTotal sale: {total_sold} €\n")


    def renderShow(self, store):
        """
        :param store: object of class Store
        :return: show and print on file the current contents of warehouse
        """

        with open("Bio Market Sas", "a") as f:

            f.write("\n----- BIO MARKET WAREHOUSE -----\n\n")

            for num, value in enumerate(store.getStore().items()):
                f.write(f"{num + 1} - {value[0]}: {value[1]}\n")


    def renderProfit(self, store):
        """
        :param store: object of class Store
        :return: print on file gross and net profit
        """
        with open("Bio Market Sas", "a+", encoding= "utf-8") as f:
            f.write("\n-----CURRENT BADGET-----\n\n")
            f.write(f"Gross profit: {store.grossProfit()} €\n")
            f.write(f"Net profit: {store.netProfit()} €\n\n")


    def helpMenu(self):
        """
        :return: show and print on file the list of available commands
        """
        cmd = {
            "buy": "purchase a product",
            "sale": "sell a product",
            "show": "show warehouse contents",
            "cash": "show gross and net profit",
            "exit": "exit the program"
        }

        with open("Bio Market Sas", "a+", encoding= "utf-8") as file:
            file.write("---MENU COMMANDS LIST---\n\n")

            for key, value in cmd.items():
                file.write(f"- Digit {key} to {value} \n")

    def insertCmd(self, store):
        """
        :param store: object of class Store
        :return: input the command to run
        """

        cmd = ""

        while cmd != "exit":
            cmd = input("Enter a command: ")
            if cmd == "buy":
                self.renderBuy(store)

            elif cmd == "sale":
                self.renderSale(store)

            elif cmd == "show":
                self.renderShow(store)

            elif cmd == "cash":
                self.renderProfit(store)

            elif cmd == "help":
                self.help()

            else:
                if cmd == "exit":
                    print("Bye")
                else:
                    print("This command is not available")
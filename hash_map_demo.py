from hash_map import HashMap


with open('reconin.txt') as inputfile:
    data = inputfile.read()

class TransactionParser(object):

    def __init__(self):
        self.cash = 0
        self.stocks = HashMap()

    def reconcile(self, recon_in):
        transactions = recon_in.split("\n\n")
        original_setting = transactions.pop(0)
        final_setting = transactions.pop()
        stocks = HashMap()
        original_settings = original_setting.split("\n")

        self.parse_initial_settings(original_settings)
        self.parse_transactions(transactions)
        return self.difference(final_setting)

    def parse_initial_settings(self, settings):
        i = 1
        while i < len(settings):
            line = settings[i].split(" ")
            if line[0] == "Cash":
                self.cash = float(line[1])
            else:
                self.stocks[line[0]] = float(line[1])
            i += 1

    def parse_transactions(self, transactions):
        transactions = transactions[0].split("\n")
        transactions.pop(0)
        i = 0
        while i < len(transactions):
            line = transactions[i].split(" ")
            if line[0] == "Cash":
                self.parse_cash_transaction(line)
            else:
                self.parse_stock_transaction(line)

            i += 1

    def declared_settings(self, settings):
        params = HashMap()

        for line in settings:
            line = line.split(" ")
            if len(line) == 2:
                stock = line[0]
                num_stocks = float(line[1])
                params[stock] = num_stocks

        return params



    def difference(self, settings):
        lines = settings.split("\n")
        lines.pop(0)
        differences = []

        declared_results = self.declared_settings(lines)

        for stock in self.stocks.keys():
            if declared_results[stock]:
                if int(declared_results[stock] - self.stocks[stock]) != 0:
                    differences.append(stock + " " + str(int(declared_results[stock] - self.stocks[stock])))
            elif self.stocks[stock] != 0:
                differences.append(stock + " " + str(int(-1 * self.stocks[stock])))


        for line in lines:
            line = line.split(" ")
            stock = line[0]
            if len(line) == 2:
                if not self.stocks[stock] and stock != "Cash":
                    differences.append(stock + " " + line[1])
                elif stock == "Cash":
                    cash_difference = float(line[1]) - self.cash
                    differences.insert(0, "Cash " + str(int(cash_difference)))

        return "\n".join(differences)


    def parse_cash_transaction(self, transaction):
        if transaction[1] == "DEPOSIT":
            self.cash += int(transaction[3]) - int(transaction[2])
        else:
            self.cash -= int(transaction[3]) - int(transaction[2])

    def parse_stock_transaction(self, transaction):
        stock = transaction[0]
        command = transaction[1]

        num_stocks = float(transaction[2])
        cash_difference = float(transaction[3])
        if command == "SELL":
            if not self.stocks[stock]:
                self.stocks[stock] = 0
            self.stocks[stock] = self.stocks[stock] - num_stocks
            self.cash = self.cash + cash_difference
        elif command == "BUY":
            if not self.stocks[stock]:
                self.stocks[stock] = 0
            self.stocks[stock] = self.stocks[stock] + num_stocks
            self.cash = self.cash - cash_difference
        elif command == "DIVIDEND":
            self.cash = self.cash + (float(transaction[3]) - float(transaction[2]))

transaction_parser = TransactionParser()
print(transaction_parser.reconcile(data))

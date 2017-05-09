from hash_map import HashMap


class TransactionParser(object):

    # Initialize with cash set to zero and stocks as empty hash map
    def __init__(self):
        self.cash = 0
        self.stocks = HashMap()


    def parse_initial_settings(self, settings):
        for line in settings:
            name, num = line.split(" ")

            if name == "Cash":
                self.cash = float(num)
            else:
                self.stocks[name] = float(num)


    def process_transactions(self, transactions):
        for line in transactions:
            line = line.split(" ")
            if line[0] == "Cash":
                self.parse_cash_transaction(line)
            else:
                self.parse_stock_transaction(line)

    def reconcile(self, recon_in):
        transactions = recon_in.split("\n\n")
        original_settings = self.format_settings(transactions.pop(0))
        final_settings = self.format_settings(transactions.pop())
        middle_transactions = self.format_settings(transactions[0])

        self.parse_initial_settings(original_settings)
        self.process_transactions(middle_transactions)
        return self.overall_diff(final_settings)



    def declared_settings(self, settings):
        settings.pop()
        stocks = HashMap()

        for line in settings:
            stock, num_stocks = line.split(" ")
            stocks[stock] = float(num_stocks)

        return stocks


    def cash_diff(self, declared_results):
        for key in declared_results.keys():
            if key == "Cash":
                declared_cash = float(declared_results[key])

        return int(declared_cash - self.cash)


    def format_settings(self, settings):
        lines = settings.split("\n")
        lines.pop(0)
        return lines;


    def stock_diff(self, key, declared_results):
        if self.stocks[key] and declared_results[key]:
            return float(declared_results[key]) - self.stocks[key]
        elif self.stocks[key]:
            return -1 * self.stocks[key]
        elif declared_results[key] and key != "Cash":
            return float(declared_results[key])
        else:
            return None


    def overall_diff(self, settings):
        diffs = []
        declared = self.declared_settings(settings)
        all_keys = list(set(self.stocks.keys() + declared.keys()))

        for key in all_keys:
            diff = self.stock_diff(key, declared)
            if diff and diff != 0:
                diffs.append(key + " " + str(int(diff)))

        diffs.insert(0, "Cash " + str(self.cash_diff(declared)))
        return "\n".join(diffs)


    def parse_cash_transaction(self, transaction):
        command, cash = transaction[1], float(transaction[3])

        if command == "DEPOSIT":
            self.cash += cash
        else:
            self.cash -= cash


    def parse_stock_transaction(self, transaction):
        stock, command, num_stocks, cash_difference = transaction
        num_stocks = int(num_stocks)
        cash_difference = int(cash_difference)
        owned_stocks = self.stocks.get(stock, 0)

        if command == "SELL":
            self.stocks[stock] = owned_stocks - num_stocks
            self.cash += cash_difference
        elif command == "BUY":
            self.stocks[stock] = owned_stocks + num_stocks
            self.cash -= cash_difference
        elif command == "DIVIDEND":
            self.cash += (cash_difference - num_stocks)


with open('reconin.txt') as inputfile:
    data = inputfile.read()

transaction_parser = TransactionParser()
print(transaction_parser.reconcile(data))

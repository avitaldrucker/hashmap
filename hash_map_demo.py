from account import Account
from hash_map import HashMap


class TransactionParser(object):

    # Initialize transaction parser object with real account
    # (accurate measure of cash and stocks) and declared account
    # (portrayal of account given D1-POS)
    def __init__(self):
        self.realAccount = Account()
        self.declaredAccount = Account()


    # Set the real account's cash and stocks to original settings,
    # given D0-POS
    def parse_initial_settings(self, settings):
        for line in settings:
            name, num = line.split(" ")

            if name == "Cash":
                self.realAccount.cash = float(num)
            else:
                self.realAccount.set_stock(name, float(num))


    # Modify real account according to transactions that took place on
    # D1-TRN
    def process_transactions(self, transactions):
        for line in transactions:
            line = line.split(" ")
            if line[0] == "Cash":
                self.process_cash_transaction(line)
            else:
                self.process_stock_transaction(line)


    # Main method for class - provide a difference between the actual
    # cash and stock portfolio, and what is given at D1-POS
    def reconcile(self, recon_in):
        transactions = recon_in.split("\n\n")

        original_settings = self.format_settings(transactions.pop(0))
        final_settings = self.format_settings(transactions.pop())
        middle_transactions = self.format_settings(transactions[0])

        self.parse_initial_settings(original_settings)
        self.process_transactions(middle_transactions)

        final_settings = self.declared_settings(final_settings)
        return self.realAccount.compare(final_settings)


    # Method that creates an Account object reflecting the cash and
    # stocks declared at D1-POS
    def declared_settings(self, settings):
        settings.pop()
        stocks = HashMap()

        for line in settings:
            stock, num_stocks = line.split(" ")
            if stock == "Cash":
                self.declaredAccount.cash = num_stocks
            else:
                self.declaredAccount.set_stock(stock, float(num_stocks))

        return self.declaredAccount


    # Formatter of transactions
    def format_settings(self, settings):
        lines = settings.split("\n")
        lines.pop(0)
        return lines;


    # Processing for any cash transaction, e.g. Cash DEPOSIT 0 1000
    def process_cash_transaction(self, transaction):
        command, cash = transaction[1], float(transaction[3])

        if command == "DEPOSIT":
            self.realAccount.cash += cash
        else:
            self.realAccount.cash -= cash


    # Processing for any stock transaction, e.g. AAPL SELL 100 30000
    def process_stock_transaction(self, transaction):
        stock, command, num_stocks, cash_difference = transaction
        num_stocks = int(num_stocks)
        cash_difference = int(cash_difference)
        owned_stocks = self.realAccount.get_stock(stock)

        if command == "SELL":
            self.realAccount.set_stock(stock, owned_stocks - num_stocks)
            self.realAccount.cash += cash_difference
        elif command == "BUY":
            self.realAccount.set_stock(stock, owned_stocks + num_stocks)
            self.realAccount.cash -= cash_difference
        elif command == "DIVIDEND":
            self.realAccount.cash += (cash_difference - num_stocks)



with open('reconin.txt') as inputfile:
    data = inputfile.read()

transaction_parser = TransactionParser()
print(transaction_parser.reconcile(data))

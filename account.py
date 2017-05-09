from hash_map import HashMap


class Account(object):


    # Initialize Account object with cash and hash map of stocks, where
    # stock name points to number of shares
    def __init__(self):
        self.cash = 0
        self.stocks = HashMap()


    # Compare account's cash and stocks with that of another account
    # Used in TransactionParser's reconcile() method
    def compare(self, other_acct):
        diffs = []
        other_stocks = other_acct.stocks
        all_keys = list(set(self.stocks.keys() + other_stocks.keys()))

        for key in all_keys:
            diff = self.stock_diff(key, other_stocks)
            if diff and diff != 0:
                diffs.append(key + " " + str(int(diff)))

        diffs.insert(0, "Cash " + str(self.cash_diff(other_acct.cash)))

        return "\n".join(diffs)


    def cash_diff(self, other_cash):
        return int(other_cash) - self.cash


    # Calculates differences in shares of stocks between two accounts
    def stock_diff(self, key, declared_results):
        if self.stocks[key] and declared_results[key]:
            return float(declared_results[key]) - self.stocks[key]
        elif self.stocks[key]:
            return -1 * self.stocks[key]
        elif declared_results[key] and key != "Cash":
            return float(declared_results[key])
        else:
            return None


    # Wrapper for setting a stock into self.stocks
    def set_stock(self, name, value):
        self.stocks[name] = value


    # Wrapper for getting a stock
    def get_stock(self, stock):
        return self.stocks.get(stock, 0)

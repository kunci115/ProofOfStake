class TransactionPool():
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def transaction_exist(self, transaction):
        for pool in self.transactions:
            if pool.compare(transaction):
                return True

        return False
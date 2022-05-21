from Transaction import Transaction
from TransactionPool import TransactionPool
from Wallet import Wallet

if __name__ == '__main__':
    sender = "Nurul"
    receiver = "Joko"
    amount = 10
    tf_type = "TRANSFER"
    wallet = Wallet()
    wallet_2_ = Wallet()
    pool = TransactionPool()

    transaction = wallet.create_transaction(receiver=receiver,
                                            amount=amount,
                                            tf_type=tf_type)
    if pool.transaction_exist(transaction=transaction) == False:
        pool.add_transaction(transaction=transaction)
    if pool.transaction_exist(transaction=transaction) == False:
        pool.add_transaction(transaction=transaction)
    print(pool.transactions)
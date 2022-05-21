from Transaction import Transaction
from Wallet import Wallet

if __name__ == '__main__':
    sender = "Nurul"
    receiver = "Joko"
    amount = 10
    tf_type = "TRANSFER"
    wallet = Wallet()
    transaction = wallet.create_transaction(receiver=receiver,
                                            amount=amount,
                                            tf_type=tf_type)
    signature_validation = Wallet.sign_validator(transaction.payload(), transaction.signature,
                                                 wallet.public_key_string())
    print(signature_validation)
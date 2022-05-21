from Transaction import Transaction
from Wallet import Wallet

if __name__ == '__main__':
    sender = "Nurul"
    receiver = "Joko"
    amount = 10
    tf_type = "TRANSFER"
    t = Transaction(sender_publickey=sender, receiver_publickey=receiver,
                    amount=amount, tf_type=tf_type)
    wallet = Wallet()
    signature = wallet.sign(t.toJson())
    t.sign(signature)
    print(t.toJson())
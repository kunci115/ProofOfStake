from BlockchainUtils import BlockchainUtils
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from Transaction import Transaction


class Wallet():
    """
    We need RSA-key pair for wallet to validate transaction
    """
    def __init__(self):
        self.key_pair = RSA.generate(2048)

    def sign(self, data):
        data_hash = BlockchainUtils.hash_(data)
        signature_schema = PKCS1_v1_5.new(self.key_pair)
        signature = signature_schema.sign(data_hash)
        return signature.hex()

    @staticmethod
    def sign_validator(data, signature, public_key_string):
        signature = bytes.fromhex(signature)
        data_hash = BlockchainUtils.hash_(data)
        pub_key = RSA.importKey(public_key_string)
        signature_scheme = PKCS1_v1_5.new(pub_key)  # validate only need public key
        validation_result = signature_scheme.verify(data_hash, signature)
        return validation_result

    def public_key_string(self):
        public_key_string = self.key_pair.public_key().exportKey('PEM').decode('utf-8')
        return public_key_string

    def create_transaction(self, receiver, amount, tf_type):
        transaction = Transaction(sender_publickey=self.public_key_string(),
                                  receiver_publickey=receiver, amount=amount, tf_type=tf_type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction

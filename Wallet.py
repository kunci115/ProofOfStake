from BlockchainUtils import BlockchainUtils
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


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


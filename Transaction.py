import uuid
import time
import copy

# Basic Transaction
class Transaction():
    def __init__(self, sender_publickey, receiver_publickey, amount, tf_type):
        self.sender_publickey = sender_publickey
        self.receiver_publickey = receiver_publickey
        self.amount = amount
        self.tf_type = tf_type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        return self.__dict__

    def sign(self, signature):
        self.signature = signature

    def payload(self):
        json_representation = copy.deepcopy(self.toJson())
        json_representation['signature'] = ''
        return json_representation

    def compare(self, transaction):
        if self.id == transaction.id:
            return True
        else:
            return False
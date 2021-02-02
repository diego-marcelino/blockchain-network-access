from datetime import datetime
import hashlib

class Block:
    """Block class."""

    def __init__(self, transactions, previous_hash=''):
        """Initialize object."""
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        string_for_hashing = ''.join(transactions) + previous_hash + \
            str(self.timestamp)
        self.block_hash = hashlib.sha256(
            string_for_hashing.encode()).hexdigest()

    def __str__(self):
        """String representation."""
        return self.block_hash


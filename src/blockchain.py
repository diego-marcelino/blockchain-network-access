from typing import List, Set
from datetime impor datetime
import json
import hashlib


class BlockChain:
    """Main class for BlockChain."""

    def __init__(self):
        self.chain: List = []
        self.current_transactions: List = []
        self.validations_nodes: Set = {}
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """Create new blocks on chain."""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': datetime.now(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.get_hash(self.last_block)
        }
        # TODO: add validation for block
        self.current_transactions = []
        self.chain.append(block)
        return block

    @property
    def last_block(self):
        return self.chain[-1]

    @property
    def full_chain(self):
        return self.chain, len(self.chain)

    @property
    def transactions(self):
        return [block['transactions'] for block in self.chain]

    def new_transaction(self, **kwargs):
        self.current_transactions.append(kwargs)
        self.last_block['index'] + 1

    @property
    def blocks(self):
        return [block for block in self.chain]

    @staticmethod
    def get_hash(block):
        """Gets hash for a block."""
        block_str = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_str).hexdigest()


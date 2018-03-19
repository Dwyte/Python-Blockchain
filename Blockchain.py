import hashlib
import time


class Header:
    index = 0
    previousHash = ""
    timestamp = ""
    nonce = 0

    def __init__(self, index, nonce, timestamp=str(time.time()), previousHash=""):
        self.index = index
        self.timestamp = timestamp
        self.nonce = nonce
        self.previousHash = previousHash


class Block:
    header = Header(Header.index, Header.nonce)
    transactions = []
    blockHash = ""

    def __init__(self, header, blockHash, transactions):
        self.header = header
        self.transactions = transactions
        self.blockHash = self.calculateHash(header)

    def calculateHash(self, header):
        x = (header.previousHash + header.timestamp).encode()
        return hashlib.sha256(x).hexdigest()


class Blockchain:
    chain = []

    def AddBlock(self):
        block = Block()
        self.chain.append(block)


# Test
headr = Header(0, 1)
block = Block(headr, Block.blockHash, Block.transactions)
print(block.blockHash)

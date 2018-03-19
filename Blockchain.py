import hashlib
import datetime


class Transaction:
    fromAddress = ""
    toAddress = ""
    amount = 0

    def __init__(self, fromAddress, toAddress, amount):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount

    # String representation of this object class
    def __repr__(self):
        return "\n   From: " + self.fromAddress + "\n" +\
                "   To: " + self.toAddress + "\n" +\
                "   Amount: " + str(self.amount) + "\n"

# Header of a block
class Header:
    index = 0
    previousHash = ""
    timestamp = ""
    nonce = 0

    def __init__(self, index, nonce, timestamp=str(datetime.datetime.now().time()), previousHash=""):
        self.index = index
        self.timestamp = timestamp
        self.nonce = nonce
        self.previousHash = previousHash

    # String representation of this object class
    def __repr__(self):
        return "\nHeader: \n{\n" \
                "   Index: " + str(self.index) + "\n" \
                "   Time: " + self.timestamp + "\n" \
                "   Nonce: " + str(self.nonce) + "\n" \
                "   Previous Hash: " + self.previousHash + "\n},"

# Block of a chain
class Block:
    header = Header(Header.index, Header.nonce)
    transactions = []
    blockHash = ""

    def __init__(self, header, blockHash, transactions):
        self.header = header
        self.transactions = transactions
        self.blockHash = self.calculateHash()

    def calculateHash(self):
        x = (self.header.previousHash + self.header.timestamp).encode() + bytes(self.header.nonce + self.header.index)
        return hashlib.sha256(x).hexdigest()

    def mineBlock(self, difficulty):
        # Set how many zeroes needed depeneding on the difficulty
        zeroes = ""
        for x in range(0, difficulty):
            zeroes += "0"

        # While the first strings of the hash is not equal to the number of zeroes needed depending to the difficulty
        while self.blockHash[:difficulty] != zeroes:
            self.header.nonce += 1
            self.blockHash = self.calculateHash()

    # String representation of this object class
    def __repr__(self):
        return str(self.header) + "\n" +\
                "Transactions:\n" + str(self.transactions) + ",\n"\
                "Block Hash: " + self.blockHash + "\n"


# The Chain
class Blockchain:
    chain = []
    pendingTransactions = []
    difficulty = 3sipp

    # Function to add a new transaction to the pending transaction pool
    def createTransaction(self, tx):
        self.pendingTransactions.append(tx)

    def minePendingTransactions(self):
        newBlockHeader = Header(len(self.pendingTransactions), Header.nonce)
        newBlock = Block(newBlockHeader, Block.blockHash, self.pendingTransactions)
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)
        self.pendingTransactions = []
        self.createTransaction(Transaction("", "MinerAddress", 50))

    # String representation of this object class
    def __str__(self):
        return "Chain: {\n" + str(self.chain) + "\n\n\n" + \
                "Pending Transactions Pool:\n" + str(self.pendingTransactions)


# Create the chain and print
chain = Blockchain()
chain.createTransaction(Transaction("Alice", "Bob", 50))
chain.minePendingTransactions()
print(chain)

from hash import generateHash
import json
from time import time

# Cretae Block class
class Block:
    # Define __init__ method with index, timestamp, transaction, previousHash parameters
    def __init__(self, index, timestamp, transaction, previousHash):
        # Store index, transaction, timeStamp, previousHash in respective object variables
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()
    
    # Calculate currentHash using the currentHash() method
    def calculateHash(self):
    
    # Create currentHash() method
     blockString = str(self.index) + str(self.timestamp) + str(self.previousHash) + str(self.transaction)
     return generateHash(blockString)
        # Create a variable blockString and store a string made by concatinating index, timestamp, previousHash and transaction 
   
        # Generating hash for blockString and return it
        
        
    
sender = "Mike"
receiver = "Sam"
sender = generateHash(sender)
receiver = generateHash(receiver)

transaction = { 
        "sender": sender, 
        "receiver": receiver, 
        "amount": 1000
    }

blockData = {
        'index': 1,
        'timestamp': time(),
        'transaction': transaction,
        'previousHash': "No Previous Hash Present. Since this is the first block.",
    }

# Use Block class and blockData to create a newBlock object.
newBlock = Block(blockData["index"], 
blockData["timestamp"], 
blockData["transaction"], 
blockData['previousHash'])

# Display content fo the newBlock

print(newBlock.index)
print(newBlock.timestamp)
print(newBlock.transaction)
print(newBlock.previousHash)
print(newBlock.currentHash)
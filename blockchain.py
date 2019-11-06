def lightening_hash(data):
    return data + '*'  # simplistic hash


class Block:  # creating class and defining it
    def __init__(self, data, hash, last_hash):  # init method
        self.data = data
        self.hash = hash
        self.last_hash = last_hash


# temp_block = Block('test', 'hash', 'last_hash')  # this is the creation of a dummy object from the above class
#
# print(temp_block.data)  # this prints the value of the current block
# print(temp_block.hash)
# print(temp_block.last_hash)

class Blockhain:
    def __init__(self):
        genesis = Block('gen_data', 'gen_hash', 'gen_last_hash')  # creating genesis block and adding data
        self.chain = [genesis]  # creating a list

    def add_block(self, data):
        last_hash = self.chain[-1].hash  # final entry of the chain list is the last hash
        hash = lightening_hash(data + last_hash)  # generating new hash
        block = Block(data, hash, last_hash)
        self.chain.append(block)


test_blockchain = Blockhain() # creating an instance of blockchain

test_blockchain.add_block('one') #adding blocks
test_blockchain.add_block('two')
test_blockchain.add_block('three')

for block in test_blockchain.chain: #printing blocks from the list
    print(block.__dict__) #using __dict__ to print the blocks as a key-value pair

import datetime  # for generating timestamps
import hashlib   # for creating SHA264 hashing of a block


# Block Class
class Block:
    BlockNumber = 0
    data = None
    ''' 
    Data here can be anything ranging from 
    transaction details to a voters' choice of candidates
    This data can also be encrypted using PKI (Public Key Interface)
    '''
    next = None  # Next Block in the sequence
    hash = None
    TimeStamp = datetime.datetime.now()
    '''
    nonce:
    "number only used once," which is a number added to a hashed—or encrypted—block in a blockchain that
    The nonce is the number that blockchain miners are solving for
    when rehashed, meets the difficulty level restrictions
    '''
    nonce = 0
    PreviousHash = 0x0
    ''' Hexadec notation for 0 as we are
    outputting hashes as a hexadecimal string'''

    def __init__(self, data):
        self.data = data

    def hash(self):
        '''
        Passing all the informtion inside a block + 
        hash of previous block to generate a new Hash
        '''
        h = hashlib.sha256()
        h.update(
            str(self.TimeStamp).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.PreviousHash).encode('utf-8') +
            str(self.nonce).encode('utf-8') +
            str(self.BlockNumber).encode('utf-8'))
        return h.hexdigest()

    def __str__(self):
        return "\nBlock No. "+str(self.BlockNumber)+"\nData : "+str(self.data)+"\nHashing : "+str(self.hash())+"\nhashes : "+str(self.nonce)+'\n---------------'


# block1 = Block("Transaction1")
# print(block1)
class BlockChain:
    MaxNonce = 2**32
    block = Block('Genesis')  # First Block in the Blockchain
    dummy = head = block
    ''' Both head and block are pointing to a dummy variable'''

    ''' The difficulty is a measure of how difficult it is to mine a Bitcoin block,
        or in more technical terms, to find a hash below a given target.
        A high difficulty means that it will take more computing power to mine the same number of blocks,
        making the network more secure against attacks.'''

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.TargetNonce = 2**(256-difficulty)

    def addNewBlock(self, NewBlock):
        NewBlock.PreviousHash = self.block.hash()
        NewBlock.BlockNumber = self.block.BlockNumber + 1
        self.block.next = NewBlock
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.MaxNonce):
            if int(block.hash(), 16) <= self.TargetNonce:
                self.addNewBlock(block)
                # print(block)
                break
            else:
                block.nonce += 1


'''
We will set a difficulty ourself
'''
simpleBLockChain = BlockChain(difficulty=20)
'''
Create blocks and mine it into the blockchain 
'''
for i in range(5):
    simpleBLockChain.mine(Block('Block'+str(i+1)+' Data'))

'''
Printing blocks in order 
'''
while simpleBLockChain.head != None:
    print(simpleBLockChain.head)
    simpleBLockChain.head = simpleBLockChain.head.next

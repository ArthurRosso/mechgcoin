from blockchain import BlockChain
from block import Block

blockchain = BlockChain()

print("***Mining mechgCoin about to start***")
print(blockchain.chain)

last_block = blockchain.latest_block
last_proof_no = last_block.proof_no
proof_no = blockchain.proof_of_work(last_proof_no)

blockchain.new_data(
    sender="0",  #it implies that this node has created a new block
    recipient="Joziel CDB",  #let's send Joziel some coins!
    quantity=
    1,  #creating a new block (or identifying the proof number) is awarded with 1
)

last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_no, last_hash)

print("***Mining mechgCoin has been successful***")
print(blockchain.chain)
from block import Block

blockchain = []

first_block = Block(['zé enter network'])
blockchain.append(first_block)

second_block = Block(['John enter network'], first_block.block_hash)
blockchain.append(second_block)

for blk in blockchain:
    print(blk)

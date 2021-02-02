from block import Block

blockchain = []

first_block = Block(['zé enter network'])
second_block = Block(['John enter network'], first_block.block_hash)


print(first_block)
print(second_block)


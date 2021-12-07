import hashlib


class Ranjana_coin:

    def __init__(self, previous_block_hash, transcation_list):
        self.previous_block_hash = previous_block_hash
        self.transcation_list = transcation_list

        self.block_data = "-".join(transcation_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Ranjana send 4C to Abhishek"
t2 = "Abhishek send 4C to Ranjana"
t3 = "Ranjana send 3.5C to Sunny"
t4 = "Sunny send 1C to Abhishek"

initial_block = Ranjana_coin("Initial String", [t1, t2])
print(initial_block.block_data)
print(initial_block.block_hash)

second_block = Ranjana_coin(initial_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = Ranjana_coin(second_block.block_hash, [t1, t4])
print(third_block.block_data)
print(third_block.block_hash)

import hashlib

Nonce_Limit = 100000000
zeros = 5


def miner(block_no, transcation_no, previous_hash_value):
    for nonce in range(Nonce_Limit):
        base_text = str(block_no) + transcation_no + previous_hash_value + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()

        if hash_try.startswith("56789"):
            print(f"Hash found")
            return hash_try


block_number = 24
transcation = "497636563f7557868d99aa3e003e183e6e4b2c32b6688c76c1c9297b37192b01"
previous_hash = "342db1274c45dff2334d4c8ded5693ea2ef314d15c3001f3af277a857561e13d"
t = miner(block_number, transcation, previous_hash)
print(t)

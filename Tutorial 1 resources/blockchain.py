import json
from hashlib import sha256

with open('blockchain.json') as blockchain_json, open('keys.json') as keys_json, open('mempool.json') as mempool_jason:
    blockchain = json.load(blockchain_json)
    keys = json.load(keys_json)
    mempool = json.load(mempool)

    

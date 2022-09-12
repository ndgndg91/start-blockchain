import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse


# Part 1 - Building a Blockchain
def proof_of_work(previous_proof):
    new_proof = 1
    check_proof = False
    while check_proof is False:
        hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
        if hash_operation[:4] == '0000':
            check_proof = True
        else:
            new_proof += 1
    return new_proof


def create_hash(block):
    encoded_block = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(encoded_block).hexdigest()


def is_chain_valid(chain):
    previous_block = chain[0]
    block_index = 1
    while block_index < len(chain):
        block = chain[block_index]
        if block['previous_hash'] != create_hash(previous_block):
            return False
        previous_proof = previous_block['proof']
        proof = block['proof']
        hash_operation = hashlib.sha256(str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()
        if hash_operation[:4] != '0000':
            return False

        previous_block = block
        block_index += 1
    return True


class Blockchain:

    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof=1, previous_hash='0')
        self.nodes = set()

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),  # 채굴된 시간
            'proof': proof,  # 작업 증명
            'previous_hash': previous_hash,  # 이전 블락 해시
            'transaction': self.transactions
        }
        self.transactions = []
        self.chain.append(block)
        return block

    # last block
    def get_previous_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        previous_block = self.get_previous_block()
        return previous_block['index'] + 1

    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and is_chain_valid(chain):
                    longest_chain = chain
                    max_length = length
        if longest_chain:
            self.chain = longest_chain
            return True
        return False


# Running the app
if __name__ == '__main__':
    # Par 2 - Mining our Blockchain

    # Creating a Web App
    app = Flask(__name__)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

    # Creating an address for the node on Port 8080
    node_address = str(uuid4()).replace('-', '')

    # Creating a Blockchain
    blockchain = Blockchain()

    # Mining a new block
    @app.route('/mine_block', methods=['GET'])
    def mine_block():
        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block['proof']
        proof = proof_of_work(previous_proof=previous_proof)
        previous_hash = create_hash(previous_block)
        blockchain.add_transaction(sender=node_address, receiver='giri', amount=1)
        block = blockchain.create_block(proof, previous_hash)
        response = {
            'message': 'Congratulations, you just mined a block!',
            'index': block['index'],
            'timestamp': block['timestamp'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash'],
            'transactions': block['transactions']
        }
        return jsonify(response), 200

    # Getting the full Blockchain
    @app.route('/get_chain', methods=['GET'])
    def get_chain():
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain)
        }
        return jsonify(response), 200

    # Check Blockchain is valid
    @app.route('/is_valid', methods=['GET'])
    def is_valid_chain():
        valid = is_chain_valid(blockchain.chain)
        message = 'Houston, we have a problem. The Blockchain is not valid.'
        if valid:
            message = 'All good. The Blockchain is valid.'
        return jsonify({
            'valid': valid,
            'message': message
        }), 200

    # Adding a new transaction to the Blockchain
    @app.route('/add_transaction', methods=['POST'])
    def add_transaction():
        request_body = request.get_json()
        transaction_keys = ['sender', 'receiver', 'amount']
        if not all(key in request_body for key in transaction_keys):
            return jsonify({
                'message': 'Some elements of the transaction are missing!'
            }), 400
        index = blockchain.add_transaction(
            request_body['sender'],
            request_body['receiver'],
            request_body['amount']
        )
        return jsonify({
            'message': f'This transaction will be added to Block {index}'
        }), 201

    # Part 3 - Decentralizing our Blockchain

    # Connecting new nodes
    @app.route('/connect_node', methods=['POST'])
    def connect_node():
        request_body = request.get_json()
        nodes = request_body.get('nodes')
        if nodes is None:
            return jsonify({
                'message': 'No node'
            }), 400
        for node in nodes:
            blockchain.add_node(node)
        return jsonify({
            'message': 'All the nodes are now connected. The giricoins the followings nodes:',
            'total_nodes': list(blockchain.nodes)
        }), 201

    # Replacing the chain by the longest chain if needed
    @app.route('/replace_chain', methods=['GET'])
    def replace_chain():
        replaced = blockchain.replace_chain()
        message = 'The nodes had different chains so the chain was replaced by the longest chains.'
        if replaced:
            message = 'All good. Then chain is the longest one.'
        return jsonify({
            'replaced': replaced,
            'message': message,
            'chain': blockchain.chain
        }), 200

    app.run(
        host='0.0.0.0',
        port=8080
    )

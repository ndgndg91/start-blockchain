from uuid import uuid4
from blockchain.blockchain import Node

# Running the app
if __name__ == '__main__':
    node = Node(port=8082, node_address=str(uuid4()).replace('-', ''))
    node.run()

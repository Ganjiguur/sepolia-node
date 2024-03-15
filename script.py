import time
from web3 import Web3

# Connect to the Ethereum node
node_url = 'http://localhost:8545'
web3 = Web3(Web3.HTTPProvider(node_url))

if not web3.is_connected():
    print("Failed to connect to the Ethereum node.")
else:
    print("Connected to the Ethereum node.")

def log_node_status():
    block_height = web3.eth.block_number
    peer_count = web3.net.peer_count
    gas_price = web3.eth.gas_price
    syncing_status = web3.eth.syncing
    chain_id = web3.eth.chain_id
    client_version = web3.client_version
    latest_block = web3.eth.get_block
    latest_block_tx_count = web3.eth.get_block_transaction_count

    print(f"Current block height: {block_height}")
    print(f"Number of peers connected: {peer_count}")
    print(f"Gas price: {gas_price} wei")
    print(f"Syncing status: {syncing_status}")
    print(f"Chain ID: {chain_id}")
    print(f"Client version: {client_version}")
    print(f"Latest block transaction count: {latest_block_tx_count}")

# Set the interval in seconds
interval = 10

try:
    while True:
        log_node_status()
        time.sleep(interval)
except KeyboardInterrupt:
    print("Script terminated by user.")
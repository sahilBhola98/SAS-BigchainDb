from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
import random

# Connect to BigchainDB
bdb = BigchainDB('https://test.bigchaindb.com')

# Generate a keypair
alice = generate_keypair()

# Define locations and spectrum bands
locations = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
spectrum_bands = ['Band1', 'Band2', 'Band3', 'Band4', 'Band5']

def create_asset(location, bands):
    # Create an asset
    asset = {
        'data': {
            'asset': {
                'properties': {
                    'location': location,
                    'spectrum bands': bands
                }
            }
        }
    }

    # Prepare the transaction with the digital asset and issue it to the network
    prepared_creation_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=alice.public_key,
        asset=asset
    )

    # Fulfill and send the transaction
    fulfilled_creation_tx = bdb.transactions.fulfill(
        prepared_creation_tx,
        private_keys=alice.private_key
    )
    sent_creation_tx = bdb.transactions.send_commit(fulfilled_creation_tx)

    return fulfilled_creation_tx

def transfer_asset(fulfilled_creation_tx, recipient):
    # Transfer the asset
    bob = generate_keypair()

    asset_id = fulfilled_creation_tx['id']

    transfer_asset = {
        'id': asset_id
    }

    output_index = 0
    output = fulfilled_creation_tx['outputs'][output_index]

    transfer_input = {
        'fulfillment': output['condition']['details'],
        'fulfills': {
            'output_index': output_index,
            'transaction_id': fulfilled_creation_tx['id']
        },
        'owners_before': output['public_keys']
    }

    prepared_transfer_tx = bdb.transactions.prepare(
        operation='TRANSFER',
        asset=transfer_asset,
        inputs=transfer_input,
        recipients=bob.public_key
    )

    fulfilled_transfer_tx = bdb.transactions.fulfill(
        prepared_transfer_tx,
        private_keys=alice.private_key
    )
    sent_transfer_tx = bdb.transactions.send_commit(fulfilled_transfer_tx)

# Create and transfer assets
for i in range(100):
    location = random.choice(locations)
    bands = random.sample(spectrum_bands, random.randint(3, 5))
    created_asset = create_asset(location, bands)
    transfer_asset(created_asset, 'RecipientPublicKey')
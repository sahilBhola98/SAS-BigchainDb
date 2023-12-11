# BigchainDB

This is an   api running on top of the BigchainDB python driver.
This repository contains a prototype implementation of an Inter-SAS Allocation system using BigchainDB, a blockchain database. The system is designed to manage spectrum usage requests from devices, convert them into transactions, sign them with a private key, and send them to the BigchainDB blockchain database.

# Description

The system is composed of several Python scripts:

- app.py: This is the main Flask application that sets up a GraphQL endpoint for querying the BigchainDB database.

- prepopulate.py: This script generates a set of assets (representing spectrum bands at different locations) and transfers them to a recipient.

- sendSAS.py: This script simulates a SAS server that receives spectrum usage requests from devices, converts them into transactions, and sends them to the BigchainDB blockchain database.

- schema.py: This script defines the GraphQL schema for querying the BigchainDB database.

The system also includes two JSON files (tx_create.json and tx_transfer.json) that represent example CREATE and TRANSFER transactions in BigchainDB.


### Note

The BigchainDB driver tries to connect to BigchainDB server running on
`localhost:9984`. It you want to change this you need to edit `prepopulate.py`
and `schema.py` and pass the correct parameters to the initialization of the
BigchainDB python driver.

### Setup

1. Install the requirements:
```bash
$ pip install -r requirements.txt
```

2. Start the - app:
```bash
$ python app.py
```

4. Make sure BigchainDB server is running

5. (Optional) Prepopulate BigchainDB with the example transactions:
```bash
$ python prepopulate.py
```

6. To simulate a SAS server, run the following command:
```bash
$ python sendSAS.py
```





# Spectrum Access System (SAS) Server

This repository contains the implementation of a Spectrum Access System (SAS) server using BigchainDB, a blockchain database.
Description

The SAS server is responsible for managing spectrum usage requests from devices. It receives requests, converts them into transactions, signs them with its private key, and sends them to the BigchainDB blockchain database.
Installation

To run this project, you need to install the BigchainDB Python driver. You can install it using pip:
driver
Usage

The main class in this project is SAS_Server. It has two main methods: receive_request and send_transactions.

- receive_request(request): This method receives a request (in the form of a Python dictionary), converts it into a transaction, signs it with the server's private key, and adds it to the input set.

- send_transactions(): This method sends all the transactions in the input set to the BigchainDB blockchain database.

# EC2 Cloud Setup for  Prototype

- This project implements a prototype of  on the Amazon AWS cloud computing platform.

# System Setup

- Our system setup includes {4} EC2 instances in Ohio, N Virginia, N California and Oregon region serving as SAS servers, with a single desktop in our lab acting as the spectrum user. Each server instance is configured as an EC2 T2.Large node, featuring two vCPUs, 8GB of memory, and a 32GB disk. These server instances are distributed across four different geographical regions in the U.S., reflecting the real-world deployment of SAS servers.

# Network Simulation

- To simulate network conditions, we assessed network latency between the lab desktop and the cloud servers. We have chosen BigchainDB as the blockchain database, with each server hosting a BigchainDB implementation forming a network. We employ the Python driver of BigchainDB to implement the coordination mechanism. BigchainDB offers two transaction templates: create for registration transactions and transfer for other transactions. Transaction details are included in the asset and metadata fields of these templates. The underlying consensus protocol used by BigchainDB is Tendermint.

# Performance Evaluation

- Our performance evaluation focuses on throughput and latency under specific traffic volume conditions. We anticipate approximately 400 CBSDs within a typical spectrum sharing zone, each capable of sending requests within a 300-second heartbeat interval. This results in an input rate of 80 transactions per minute (TPM). In real scenarios, we expect around 10 TPM. Stress tests are conducted at various input rates, including {30, 60, 90, 120, 150, 180} TPM, with each request specifying desired spectrum bands and locations. The decision finalization intervals vary within the range {30, 60, 90, 120} seconds while maintaining a fixed input rate.


-  we  assessed the decision finalization phase, with a focus on latency. For four servers, we evaluated the system's performance under maximum (90 TPM) and normal (30 TPM) input rates. As the input rate increased, processing latency  rise due to additional processing time for transaction commitments and allocation generation. Latency also  increases linearly with the polling interval but  remained smaller than the designated interval n.

- With seven servers, we got a similar latency trend, albeit with larger values. At a fixed input rate of 30 TPM, latency with seven servers is os to be higher than with four, still following a linear relationship with the polling interval. However, for an input rate of 90 TPM, latency exceed the designated interval. 



# Screenshots
- Snapshot of the EC2 Dashboard of all ec2 instances setup
<img width="1511" alt="Screenshot 2023-11-30 at 2 07 27 PM" src="https://github.com/sahilBhola98/SAS-BigchainDb/assets/23173443/2783c235-4189-422b-ad16-1c973e9a82a6">


- Snapshot of the setting up ec2 server for bigchaindb
<img width="918" alt="Screenshot 2023-11-29 at 6 29 39 PM" src="https://github.com/sahilBhola98/SAS-BigchainDb/assets/23173443/a1de75ee-114c-4b4c-97e1-68f9a50654dc">

- Snapshot of the setting up ec2 server for bigchaindb
<img width="916" alt="Screenshot 2023-11-29 at 4 02 05 PM" src="https://github.com/sahilBhola98/SAS-BigchainDb/assets/23173443/15266763-aec5-4cad-8201-c6db45f3bbd5">




Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
License

MIT

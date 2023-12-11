# BigchainDB

This is an   api running on top of the BigchainDB python driver.


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

This are the transactions used in the next examples.


### Spectrum Access System (SAS) Server

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

### EC2 Cloud Setup for  Prototype

- This project implements a prototype of  on the Amazon AWS cloud computing platform.
System Setup

- Our system setup includes {4} EC2 instances in Ohio, N Virginia, N California and Oregon region serving as SAS servers, with a single desktop in our lab acting as the spectrum user. Each server instance is configured as an EC2 T2.Large node, featuring two vCPUs, 8GB of memory, and a 32GB disk. These server instances are distributed across four different geographical regions in the U.S., reflecting the real-world deployment of SAS servers.
Network Simulation

- To simulate network conditions, we assess network latency between the lab desktop and the cloud servers. We have chosen BigchainDB as the blockchain database, with each server hosting a BigchainDB implementation forming a network. We employ the Python driver of BigchainDB to implement the coordination mechanism. BigchainDB offers two transaction templates: create for registration transactions and transfer for other transactions. Transaction details are included in the asset and metadata fields of these templates. The underlying consensus protocol used by BigchainDB is Tendermint.
Performance Evaluation

- Our performance evaluation focuses on throughput and latency under specific traffic volume conditions. We anticipate approximately 400 CBSDs within a typical spectrum sharing zone, each capable of sending requests within a 300-second heartbeat interval. This results in an input rate of 80 transactions per minute (TPM). In real scenarios, we expect around 10 TPM. Stress tests are conducted at various input rates, including {30, 60, 90, 120, 150, 180} TPM, with each request specifying desired spectrum bands and locations. The decision finalization intervals vary within the range {30, 60, 90, 120} seconds while maintaining a fixed input rate.
Future Experiments

- In future experiments, we will assess the decision finalization phase, with a focus on latency. For four servers, we will evaluate the system's performance under maximum (90 TPM) and normal (30 TPM) input rates. As the input rate increases, processing latency is expected to rise due to additional processing time for transaction commitments and allocation generation. Latency is also anticipated to increase linearly with the polling interval but should remain smaller than the designated interval n.

- With seven servers, we expect a similar latency trend, albeit with larger values. At a fixed input rate of 30 TPM, latency with seven servers is expected to be higher than with four, still following a linear relationship with the polling interval. However, for an input rate of 90 TPM, latency may exceed the designated interval. This future experiment will provide a comprehensive assessment of the system's performance.
Contributing

### Screenshots
- Snapshot of the EC2 Dashboard of all ec2 instances setup
<img width="1511" alt="Screenshot 2023-11-30 at 2 07 27 PM" src="https://github.com/sahilBhola98/SAS-BigchainDb/assets/23173443/9e5b5f09-c29d-47d8-b267-85d35766774b">

- Snapshot of the setting up ec2 server for bigchaindb
<img width="918" alt="Screenshot 2023-11-29 at 6 29 39 PM" src="https://github.com/sahilBhola98/SAS-BigchainDb/assets/23173443/a1de75ee-114c-4b4c-97e1-68f9a50654dc">


Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
License

MIT

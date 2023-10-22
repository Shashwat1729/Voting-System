# Voting System using Zero-Knowledge Proof on Blockchain

This is a Python-based implementation of a voting system on the blockchain that incorporates zero-knowledge proof for secure and confidential voting. This system allows users to propose candidates, authenticate voters, cast their votes, and view transaction history. It uses a simple blockchain structure for maintaining transaction records.

## How It Works

### Blockchain
- The blockchain is a linked list of blocks, with each block containing a set of transactions.
- Each block has an `index`, `timestamp`, `transactions`, `previousHash`, `nonce`, and `hash`.
- Blocks are mined to ensure they meet a certain difficulty level (`difficulty`) before being added to the blockchain.

### Transaction
- Each vote is represented as a `Transaction` object.
- A sender (voter), receiver (candidate), and proposal index are recorded for each transaction.
- A timestamp is generated when the transaction is created.
- A zero-knowledge proof is used to verify the transaction's authenticity.

### Verifier
- A `Verifier` object is used to create public keys and verify transactions.
- It generates a public key `B` and a shared key `K` for each transaction.

### Blockchain Operations
- Users can propose candidates (`add_proposal`) and authenticate voters (`authenticate_user`).
- Voters can cast their votes (`vote`) after authentication, and the votes are added to the pending transactions.
- Users can view their transaction history (`view_user`) to ensure transparency.
- The total vote count for each candidate can be obtained (`get_vote_count`).

## Getting Started
1. Create an instance of the blockchain:
   ```python
   blockchain = Blockchain()
   ```

2. Add proposals for candidates:
   ```python
   proposals = ["a", "b", "c", "d"]
   for i in proposals:
       blockchain.add_proposal(i)
   ```

3. Authenticate voters:
   ```python
   voters = ["manas", "amlan", "amarjeet", "bilal", "waleed", "ayushman", "jaskirat", "tarun", "ankit", "shaantanu"]
   for j in voters:
       blockchain.authenticate_user(j)
   ```

4. Cast votes for candidates:
   ```python
   for j in voters:
       candidate = input("Enter your candidate " + j + ":")
       blockchain.vote(j, candidate)
       blockchain.mine_pending_transaction()
   ```

5. Retrieve transaction history for each user:
   ```python
   for j in voters:
       transactionHistory[j] = blockchain.view_user(j)
   ```

6. Obtain the vote count for each candidate:
   ```python
   for i in proposals:
       print("Vote count of " + i + " : " + str(blockchain.get_vote_count(i)))
   ```

7. View the transaction history for each user:
   ```python
   for j in voters:
       print("Transaction for " + j + " : " + str(transactionHistory[j]))
   ```

## Dependencies
- This code depends on a Python script named `createprime.py` to generate prime numbers.

## Security and Zero-Knowledge Proof
- This system uses a zero-knowledge proof to verify the authenticity of transactions.
- Voters authenticate using their private keys (`a`) to generate public keys (`A`) for each transaction.
- Public keys are used to create a shared key (`K`) for the transaction.
- The system checks whether `K` and `K_prime` match to ensure that the sender is genuine, without revealing the private key.

## Important Notes
- This implementation is a simplified example and does not provide complete security.
- In a real-world application, you would need additional layers of security, encryption, and more comprehensive authentication mechanisms.
- Blockchain technology has a wide range of use cases beyond voting systems.

## License
This project is open-source and available under the MIT License. You are free to use and modify the code according to your needs.

Please feel free to contribute to this repository and improve the code, security, and usability. Your contributions are highly appreciated!

**Happy Voting!**

# RSA Algorithm

This project is an implementation of the RSA algorithm, a widely-used asymmetric encryption technique. The RSA algorithm allows for secure data transmission by using a pair of keys: a public key for encryption and a private key for decryption.

## Features

- Generation of public and private keys using two prime numbers.

- Encryption of plaintext using the public key.

- Decryption of ciphertext using the private key.

## Files

- rsa.py: Contains the main code for generating RSA keys, encrypting data, and decrypting it.

## How to Use

### Prerequisites

- Python 3.x installed on your system.

- The sympy library for prime checking and modular inverse calculation. You can install it using:
```bash
pip install sympy
```

## Running the Code

### Clone the repository:
```bash
git clone https://github.com/your-username/RSA-Algorithm.git
cd RSA-Algorithm
```
Run the script to generate keys, encrypt, and decrypt a message:
```bash
python rsa.py
```
## Example

The script will prompt you to enter two prime numbers. It then generates the public and private keys, encrypts a user-provided plaintext, and decrypts it to verify correctness.

- Primes: You can input any two prime numbers, e.g., 61 and 53.

- Plaintext: The plaintext must be an integer, e.g., 65.

The script will then display:

- Generated public and private keys.

- The encrypted ciphertext.

- The decrypted plaintext, which should match the original input.

## Project Structure

- Key Generation: Uses two prime numbers to generate public and private keys based on Euler's Totient function and ensures e is coprime with φ(n).

- Encryption: Uses the public key (e, n) to encrypt the plaintext.

- Decryption: Uses the private key (d, n) to decrypt the ciphertext.

## Learning Objectives

This project helps in understanding:

- The basics of RSA encryption and decryption.

- The importance of key generation, including prime selection and Euler's Totient function.

- How asymmetric encryption works to secure data transmission.

## References

- Wikipedia - RSA (cryptosystem)


## License

- This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

- Contributions are welcome! If you have ideas for improvement or want to fix an issue, feel free to open an issue or submit a pull request.

# Contact

- Created by Jakob. If you have any questions or feedback, feel free to reach out!

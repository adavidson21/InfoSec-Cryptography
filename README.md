# Project 3

## Task 1 - Warm-up, Get Familiar with RSA

### Prompt: 
You are given an RSA key pair (N , e) and d, and a unique encrypted message c. 

You are required to get the decrypted message m. Implement task_1 to decrypt the message.

### Solution: 
The formula to use for decryption is: m = c^d mod N. 
The function ```task_1``` accepts 3 string parameters that correlate to ```N```, ```d```, and ```c```, which are as follows:

- ```N``` is an encrypted value of the public key
- ```d``` is the encrypted private key 
- ```c``` is the encrypted cipher string

The function works as follows:

1. Converts the 3 arguments (```n```, ```d```, and ```c```) to a base 16 integer.

2. Using the power function, it calculates ```c``` to the power of ```d```, modulus ```n``` and sets ```m``` equal to that value  
([Documentation for ```pow()```]())

3. The function returns the hex value of ```m```, with any trailing 'L' characters removed.  
([Documentation for ```rstrip()```](https://www.w3schools.com/python/ref_string_rstrip.asp))

## Task 2 - Warm-up, Get Familiar with Hashes

### Prompt:
You are given a list of some of the most commonly-used passwords on the Internet. You are also given the S​HA256 ​hash of a password randomly selected from this list.  

Your job is to discover the plaintext password behind the hash. 

### Solution:
The list of possible passwords has to be traversed, the password for comparison needs to be hashed and compared to the given hashed password. 

Once the match is found, then the non-hashed version of the password is returned.

The function works as follows:

1. The list of common passwords is provided (as a list of strings, called ```common_password_list```).

2. Loop through each password string in the list

3. Convert the current password being compared (from the list) to the SHA256 hash version. 

4. Check if the new hash password (```hashed_password```) matches the passed hash value (```password_hash```). 
    - If they are equal, then we know what the non-hashed version of the passed password is, which is stored as ```password```.
    - If they are not equal, continue to the next value in the ```common_password_list```.

## Task 3 - 

## Task 4 -

## Task 5 -

## Task 6 -

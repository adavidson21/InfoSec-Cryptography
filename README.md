# Project 3

## Task 1 - Warm-up, Get Familiar with RSA

### Prompt: 
You are given an RSA key pair (N , e) and d, and a unique encrypted message c. 

You are required to get the decrypted message m. Implement task_1 to decrypt the message.

### Solution: 
The formula to use for decryption is: m = c^d mod N. 

The function ```task_1``` accepts 3 string parameters that correlate to ```N```, ```d```, and ```c```, which are as follows:

- `N` is an encrypted value of the public key
- `d` is the encrypted private key 
- `c` is the encrypted cipher string

The function works as follows:

1. Converts the 3 arguments (`n`, `d`, and `c`) to a base 16 integer.

2. Using the power function, it calculates `c` to the power of `d`, modulus `n` and sets `m` equal to that value  
([Documentation for `pow()`]())

3. The function returns the hex value of `m`, with any trailing 'L' characters removed.  
([Documentation for `rstrip()`](https://www.w3schools.com/python/ref_string_rstrip.asp))

## Task 2 - Warm-up, Get Familiar with Hashes

### Prompt:
You are given a list of some of the most commonly-used passwords on the Internet. You are also given the S​HA256 ​hash of a password randomly selected from this list.  

Your job is to discover the plaintext password behind the hash. 

### Solution:
The list of possible passwords has to be traversed, the password for comparison needs to be hashed and compared to the given hashed password. 

Once the match is found, then the non-hashed version of the password is returned.

The function works as follows:

1. The list of common passwords is provided (as a list of strings, called `common_password_list`).

2. Loop through each password string in the list

3. Convert the current password being compared (from the list) to the SHA256 hash version. 

4. Check if the new hash password (`hashed_password`) matches the passed hash value (`password_hash`). 
    - If they are equal, then we know what the non-hashed version of the passed password is, which is stored as `password`.
    - If they are not equal, continue to the next value in the `common_password_list`.

## Task 3 - Kernelcoin

### Prompt:
You’ve discovered a brand new cryptocurrency called kernelcoin (symbol: RTI). 

You plan to start mining kernelcoin so that you can earn more. In order to do so, you need to create a valid block to append to the previous block. 

A valid block contains the lowest nonce value that, when concatenated with the transaction string, and the hash of the previous block (in that order, i.e. nonce + transaction string + previous block hash), will produce a SHA256 hash with two leading zeros (the proof-of-work for this particular blockchain). Transaction strings have the syntax “UserID1:UserID2:X”, indicating that UserID1has transferred X kernelcoin to UserID2. 

You are given all of these values, and your goal is to find the lowest possible nonce value for the resulting block.

### Solution
The nonce value has to be incremented and tested as a part of the string that gets hashed in order to find the proof of work value. 

If the proof of work (the first two characters of the hash, accessed using `hash[:2]`) is not "00", then we know that the nonce value that was used was incorrect, and that we have to increment by 1 and retest. 

We know that it is the lowest possible value because we are starting at 0 and continue to increase by 1, so as soon as the function hits the lowest possible correct value it will return that value.

The function `task_3` works as follows:

1. The `nonce` integer is initialized to 0, the lowest possible nonce value that could be used.

2. The `end_hash` string is set to the static "end" of the string. Since the only value that is to be changed throughout the function is the `nonce`, `end_hash` is initialized to a concatenation of `user_id_1`, ":" `user_id_2`, ":", `str(amount)`, and `prev_block_hash`.

3. The `hash` string is initialized to the `end_hash` string being combined with the initial `nonce` value of 0, and then converted to SHA256. 

4. The function will loop through each nonce value, starting at zero, until the correct `nonce` is found, which at that point it will simply return that correct nonce value.
    - `nonce` is determined to be correct when the hash string that it is included in has "00" as the first two characters.

## Task 4 -

## Task 5 -

## Task 6 -

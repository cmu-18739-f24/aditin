# rat-CTFs

This holds my two CTF problems,`rat-clone-1` and `rat-clone-2`.

Problem 1 deals with an affine cipher. I wanted to look into a different cipher/encryption scheme that we hadn't gone over in class. The solution approach is to realize that it is an affine cipher, then use the encryption oracle to encrypt a known plaintext. Then iterate over the possible a and b values to find out what values of a and b were used to encrypt it, then use these values to decrypt the encrypted cheese.

Problem 2 deals with an insufficiently salted hash. I had heard about salting hashes before and done research on these vulnerabilities before, and wanted to implement a simple version of these vulnerabilities. The solution involves creating a rainbow table with all possible 1 byte salts, then SHA-256 encrypting every cheese in cheese_list.txt, and cross referencing these encryptions with the encryption provided by the program in order to realize what the actual value is!

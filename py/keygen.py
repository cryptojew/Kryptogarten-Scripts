# Example program from the book Mastering Bitcoin (Unlocking digital currencies), by Andreas M. Antonopoulos. Not to be used in production code. 
# Author: The CryptoJew 
# Date  : April 19th 2016 

import bitcoin 

#Generate a random private key 
valid_private_key = False 

while not valid_private_key: 
  private_key = bitcoin.random.key()
  decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
  valid_private_key  = 0 < decoded_private_key < bitcoin.N 
  
print "Private key(hex) is: ", private_key
print "Private key(dec) is: ", decoded_private_key

#Convert private key to WIF format
wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
print "Private key(wif) is: ", private_key

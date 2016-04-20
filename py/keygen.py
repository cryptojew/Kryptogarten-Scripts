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

#Add suffix 01 to indicate a compressed private key
compressed_private_key = private_key + '01'
print "Private key compressed (hex) is: ", compressed_private_key

#Generate a WIF format from the compressed private key (WIF-compressed) 
wif_compressed_private_key = bitcoin.encode_privkey(bitcoin_decode_privkey(compressed_private_key, 'hex'), 'wif')
print "Private key (WIF-compressed) is: ", wif_compressed_private_key 

#Multiply the EC generator point G with the private key to get a public key point 
public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)
print "Public key (x,y) coordinates is: ", public_key

#Encode as hex, prefix 04 
hex_encoded_public_key = bitcoin.encode_pubkey(public_key, 'hex')
print "Public key (hex) is: ", hex_encoded_public_key 

#Compress public key, adjust prefix depending on whether y is even or odd 
(public_key_x, public_key_y) = public_key
if(public_key_y % 2) == 0: 
  compressed_prefix = '02'
else:
  compressed_prefix = '03'
hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)
print "Compressed Public key (hex) is: ", hex_compressed_public_key



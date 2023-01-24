
import os
import sys
import time
import textwrap

#======================================================================================

BLOCK_SIZE = 16

AUTH = "-u admin:hammertime"
HOST = "--socks5-hostname 127.0.0.1:9150"
URL = "http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/check_secret.html"
OPTIONS = "--http0.9 -s"
PAYLOAD = "--data-raw secret="
OUTFILE ="tmp.txt"

#======================================================================================

def generate_command(secret):
	return "curl "+AUTH+" "+HOST+" "+URL+" "+OPTIONS+" "+PAYLOAD+secret+" > "+OUTFILE

def bytearray_to_string(bytearr):
	result = ""
	for byte in bytearr:
		h = hex(byte).replace("0x", "")
		if len(h)!=2:
			h = '0' + h
		result += h
	return result

def check_output():
	file = open(OUTFILE)
	lines = file.readlines()
	if not lines:
		return 0
	print(lines[0], end='', flush=True)
	if str(lines[0]) != 'invalid padding\n':
		#print("FOUND")
		return 1
	return 0

def ask_oracle(iv, ct):
	tries = 3
	while True:
		os.system(generate_command(bytearray_to_string( bytearray(iv+ct) )))
		response = check_output()
		if response != None:
			break
		if tries == 0:
			return False
		tries -= 1
		print("No response: Retrying...")

	return response

#======================================================================================

def single_block_attack(block, oracle):
    """Returns the decryption of the given ciphertext block"""

    # zeroing_iv starts out nulled. each iteration of the main loop will add
    # one byte to it, working from right to left, until it is fully populated,
    # at which point it contains the result of DEC(ct_block)
    zeroing_iv = [0] * BLOCK_SIZE

    for pad_val in range(1, BLOCK_SIZE+1):
        print("   Byte:", pad_val-1)
        bytestart = time.time()
        padding_iv = [pad_val ^ b for b in zeroing_iv]

        for candidate in range(256):
            padding_iv[-pad_val] = candidate
            iv = bytes(padding_iv)
            if oracle(iv, block):
                if pad_val == 1:
                    # make sure the padding really is of length 1 by changing
                    # the penultimate block and querying the oracle again
                    padding_iv[-2] ^= 1
                    iv = bytes(padding_iv)
                    if not oracle(iv, block):
                        continue  # false positive; keep searching
                break
        else:
            raise Exception("no valid padding byte found (is the oracle working correctly?)")

        zeroing_iv[-pad_val] = candidate ^ pad_val
        print("      Found value:",zeroing_iv[-pad_val])
        print("      Byte Completed in", time.time()-bytestart, "seconds")

    return zeroing_iv


def full_attack(iv, ct, oracle):
    """Given the iv, ciphertext, and a padding oracle, finds and returns the plaintext"""
    assert len(iv) == BLOCK_SIZE and len(ct) % BLOCK_SIZE == 0

    msg = iv + ct
    blocks = [msg[i:i+BLOCK_SIZE] for i in range(0, len(msg), BLOCK_SIZE)]
    result = b''

    # loop over pairs of consecutive blocks performing CBC decryption on them
    iv = blocks[0]
    for i, ct in enumerate(blocks[1:]):
        print(" > Block:",i)
        start = time.time()
        dec = single_block_attack(ct, oracle)
        pt = bytes(iv_byte ^ dec_byte for iv_byte, dec_byte in zip(iv, dec))
        result += pt
        iv = ct
        print("   Block Completed in", time.time()-start, "seconds")
        print("   Result:",result)
        print("   dec:   ",dec)
        print("   iv:    ",iv)

    return result

#======================================================================================

enc_hex = 'ad8bb176da1f40a98385ad0ae9777c3208b78ae57a7fec84092b2cbbaf2ab1c0'
ciphertext = bytes(bytearray.fromhex(enc_hex))

#print(ciphertext[0:BLOCK_SIZE], ciphertext[BLOCK_SIZE:])

result = full_attack(ciphertext[0:BLOCK_SIZE], ciphertext[BLOCK_SIZE:], ask_oracle)
print(result)

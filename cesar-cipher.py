import string

def cesar_cipher(message, key):
	alphabet = string.printable 
	crypted_message = ""
	for char in message:
		"""
		on va chiffrer le caractère 
			1- trouver la positon du carac dans l'alphabet
			2- y rajouter la clef à la positon du carac dans l'alphabet
			3- reccupérer le caractère chiffré
		on va stocker le caractère chiffrer
		"""
		index_carac_in_printable = alphabet.index(char)
		index_crypted_char = (index_carac_in_printable + key) % len(alphabet)
		cryted_char = alphabet[index_crypted_char]

		crypted_message += cryted_char
	
	return crypted_message



message = 'jad'
key = 160
print(cesar_cipher(message, key))
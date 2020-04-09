from stegano import lsb
print("_______Python steganographer___")
print(''' Enter option :
1. Encode
2. Decode
''')
op=int(input(">"))
if op==1:
	path=input("Provide the name of the image with extension[keep in current working directory]")
	messg=input("Enter message to hide:")
	updated_filename=input("enter new image name:")
	secret=lsb.hide(path,messg)
	secret.save(updated_filename)
elif op==2:
	path=input("Enter the image to be decoded:")
	secret_message=lsb.reveal(path)
	print("secret message=",secret_message)
	

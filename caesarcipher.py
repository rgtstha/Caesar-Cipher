#Get message input from user. 
print ('==============================================')
print(		'CREATED BY RANJIT SHRESTHA')
print ('==============================================')
message = input ('Enter the message = ')
#get key input from user.
key = int(input('enter the key[1-25] = '))
#if inputed key is not in between 0 and 26 while loop will be executed again and again.
while not key in range(0,26):
	print('\n\nSorry key should be in between [0-26] ')
	key = int(input('enter the key[1-25] = '))
mode = input('Do you want to encrypt or decrypt ? [e/d] = ')


translated = ''
#converting all messages in to upper case.
message = message.upper()

#the index that contains all possible alphabets which are in messsage. 
index = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for i in message:

	if i in index:
		#finds position of alphabet in index.
		position = index.find(i)

		#store the newposition after adding the key.
		if mode == 'e':
			newposition = (position + key )%26
		else :
			newposition = (position - key )% 26
		translated = translated + index [newposition]
	else:
		translated = translated + i


print ('The translated message is : ' +translated)
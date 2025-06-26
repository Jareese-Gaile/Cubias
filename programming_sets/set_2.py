def shift_letter(letter, shift):  
    if letter==" ":
        return " "
    base=ord("A")
    shifted=(ord(letter)-base+shift)%26
    return chr(base+shifted)

def caesar_cipher(message, shift):
    result=""
    for char in message:
        if char==" ":
            result+=" "
        else:
            base=ord("A")
            shifted=(ord(char)-base+shift)%26
            result+=chr(base+shifted)
    return result

def shift_by_letter(letter, letter_shift):
    if letter==" ":
        return " "
    shift_value=ord(letter_shift)-ord("A")
    base=ord("A")
    shifted=(ord(letter)-base+shift_value)%26
    return chr(base+shifted)

def vigenere_cipher(message, key):
    message_codes=[]
    key_shifts=[]
    encrypted_result=[]
    base=ord('A')
    for ch in message:
        if ch==' ':
            message_codes.append(' ')
        else:
            message_codes.append(ord(ch))
    full_key=(key*((len(message)//len(key))+1))[:len(message)]
    for k in full_key:
        key_shifts.append(ord(k)-base)
    for i in range(len(message_codes)):
        if message_codes[i]==' ':
            encrypted_result.append(' ')
        else:
            shifted=(message_codes[i]-base+key_shifts[i])%26
            encrypted_result.append(chr(base+shifted))
    return ''.join(encrypted_result)

def scytale_cipher(message, shift):
    while len(message)%shift!=0:
        message+="_"
    num_rows=len(message)//shift
    encoded=""
    for i in range(len(message)):
        index=(i//shift)+num_rows*(i%shift)
        encoded+=message[index]
    return encoded

def scytale_decipher(message, shift):
    num_rows=len(message)//shift
    decoded=[""]*len(message)
    for i in range(len(message)):
        original_index=(i%shift)*num_rows+(i//shift)
        decoded[original_index]=message[i]
    return "".join(decoded)

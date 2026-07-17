import argparse

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
   
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        
        if char.isalpha():
          
            ascii_offset = 65 if char.isupper() else 97
            
           
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
            
    return result

def main():


    parser = argparse.ArgumentParser(description="Caesar Encryption and Decryption Tool")
    parser.add_argument("-m", "--mode", choices=['encrypt', 'decrypt'], required=True, 
                        help="transaction type: 'encrypt' or 'decrypt'")
    parser.add_argument("-t", "--text", required=True, help="text to be processed")
    parser.add_argument("-s", "--shift", type=int, required=True, help="shift amount")

    args = parser.parse_args()

    result = caesar_cipher(args.text, args.shift, args.mode)

    print(f"\nresult: {result}\n")

if __name__ == "__main__":
    main()
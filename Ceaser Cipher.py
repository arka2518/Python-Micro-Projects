alphabet = [" a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else: 
            if encode_or_decode == "decode":
                shift_amount *= -1
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is you {encode_or_decode}d message: {output_text}")

should_continue =  True
while should_continue:
    direction = input("Would you like to encode or decode? ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Would like to continue (Yes or No): ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")


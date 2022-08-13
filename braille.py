def solution(s):
    # Get iterable of the word(s) to be converted
    list_to_convert = list(s)
    
    # Initialize the output
    braille = ""
    # Loop through each letter to be converted
    for i in list_to_convert:
        # Deal with uppercase letters
        if i.isupper():
            braille += "000001"
            # Then convert them (if any) to lowercase
            i = i.lower()
            # Find the corresponding braille translation
        braille += convert_to_braille(i)
    # Output the result converted to braille
    print(braille)
    
    
    
def convert_to_braille(letter):
    # Key:Value dictionary of each braille letter conversion
    braille_dict = {
        " ": "000000",
        "a": "100000",
        "b": "110000",
        "c": "100100",
        "d": "100110",
        "e": "100010",
        "f": "110100",
        "g": "110110",
        "h": "110010",
        "i": "010100",
        "j": "010110",
        "k": "101000",
        "l": "111000",
        "m": "101100",
        "n": "101110",
        "o": "101010",
        "p": "111100",
        "q": "111110",
        "r": "111010",
        "s": "011100",
        "t": "011110",
        "u": "101001",
        "v": "111001",
        "w": "010111",
        "x": "101101",
        "y": "101111",
        "z": "101011"
    }
    return braille_dict[letter]

solution('Braille')
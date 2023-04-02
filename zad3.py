def caesar_cipher(data, klucz,*mas):
    data = data.lower()
    if klucz > 0:
        ilosc = int(klucz / 26)
        if ilosc > 0:
            klucz = klucz - ilosc * 26
    else:
        ilosc = int(klucz * -1 / 26)
        if ilosc > 0:
            klucz = klucz + ilosc * 26

    new_string = ""
    for c in data:
        if ord('z') >= ord(c) >= ord('a'):
            if ord(c) + klucz > ord('z'):
                new_string += (chr(ord('a') + ord(c) + klucz - ord('z') - 1))
            elif ord(c) + klucz < ord('a'):
                new_string += (chr(ord('z') - (ord('a') - ord(c) - klucz - 1)))
            else:
                new_string += (chr(ord(c) + klucz))
        else:
            new_string += c

    if mas:
        new_string += '\n' + data.replace((mas[0])[0], (mas[0])[1])

    return new_string + '\n'



data = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll"
enc = caesar_cipher(data, 5)
print(enc)
enc = caesar_cipher(data, 3,["a","B"])
print(enc)

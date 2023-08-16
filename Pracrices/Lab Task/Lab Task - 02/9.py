def decimalToHex(decimalValue):
    hex_chars = '0123456789ABCDEF'
    hex_string = ''
    while decimalValue > 0:
        hex_value = decimalValue % 16
        hex_string = hex_chars[hex_value] + hex_string
        decimalValue = decimalValue // 16
    return hex_string

def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return str(hexValue)
    else:
        return chr(ord('A') + hexValue - 10)

decimalValue = int(input("Enter a decimal number: "))
print("Hex: ", decimalToHex(decimalValue))



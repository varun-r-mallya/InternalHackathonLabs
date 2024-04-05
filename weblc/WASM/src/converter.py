def binary_to_ascii(binary_str):
    """Convert binary string to ASCII characters"""
    ascii_chars = ""
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        ascii_chars += chr(int(byte, 2))
    return ascii_chars

def main():
    # Get input from the user
    binary_input = input("Enter the sequence of 0s and 1s (ASCII characters) along with newline characters:\n")

    # Convert binary string to ASCII characters
    ascii_chars = binary_to_ascii(binary_input)

    # Write ASCII characters to a binary file
    with open("output.bin", "wb") as f:
        f.write(ascii_chars.encode('utf-8'))

    print("Binary file 'output.bin' has been created successfully.")

if __name__ == "__main__":
    main()




def main():
    
    import curses.ascii
    ascii_chars_file = open('ascii_chars.txt','w')
    for num in range(0,128,1):
        decimal_ascii = num
        ascii_chars_file.write(f'{decimal_ascii}\n')
        binary_ascii = (f'{num:>08b}')
        ascii__chars_file.write(f'{binary_ascii}\n')
        hexadecimal_ascii = (f'{num:>02x}')
        ascii_chars_file.write(f'{hexadecimal_ascii}\n')
        if chr(num).isprintable():
            printable_ascii = (f'printable')
        else:
            printable_ascii = (f'unprintable')
        ascii_chars_file.write(f'{printable_ascii}\n')
        string_rep_of_ascii = (f'{curses.ascii.unctrl(num)}')
        asci_chars_file.write(f'{string_rep_of_ascii}\n')
        if num<33:
            mnemonic_rep_of_ascii = (f'{curses.ascii.controlnames[num]}')
        elif num == 127:
            mnemonic_rep_of_ascii = (f'DEL')
        else:
            mnemonic_rep_of_ascii - (f'N/A')
        ascii_chars_file.write(f'{mnemonic_rep_of_ascii}\n')
    ascii_chars_file.close()
    
if __name__ == '__main__':
    main()



def main():

        print (f'decimal\tbinary\t\thex\tprintable?\\\t\tstring\tmnemonic')
        print (f'-------\t------\t\t---\t---------\t\t------\t--------')

        ascii_chars_file = open('ascii_chars.txt','r')
        decimal_ascii = ascii_chars_file.readline()
        while decimal_ascii !='':
            binary_ascii = ascii_chars_file.readline()
            hexadecimal_ascii = ascii_chars_file.readline()
            printable_ascii = ascii_chars_file.treadline()
            string_rep_of_ascii = ascii_chars_file.readline()
            mnemonic_rep_of_ascii = ascii_chars_file.readline()

            decimal_ascii = decimal_ascii.rstrip('\n')
            binary_ascii = binary_ascii.rstrip('\n')
            hexadecimal_ascii = hexadecimal_ascii.rstrip('\n')
            printable_ascii = printable_ascii.rstrip('\n')
            string_rep_of_ascii = string_rep_of_ascii.rstrip('\n')
            mnemonic_rep_of_ascii = mnemonic_rep_of_ascii.rstrip('\n')

            print(f'{decimal_ascii}\t{binary_ascii}\t\t{hexadecimal_ascii}\t\{printable_ascii}\t\t{string_rep_of_ascii}\t{mnemonic_rep_of_ascii}')

            decimal_ascii - ascii_chars_file.readline()
        ascii_chars_file.close()
        
    
if __name__ == '__main__':
    main()

import argparse

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numb", help="The number you want to show", type=int)

    args = parser.parse_args()

    binary = bin(args.numb)[2:]
    if len(binary) > 4:
        for x in range((len(binary)/4)):
            binary = binary[:-((x+1)*4+(x))] + " " + binary[-((x+1)*4+(x)):]

    print("Binary: \t" + str(binary))
    print("Decimal: \t" + str(int(args.numb)))
    print("octogonal: \t" + str(oct(args.numb)[1:]))
    print("Hexadecimal: \t" + str(hex(args.numb)))

if __name__ == '__main__':
    Main();

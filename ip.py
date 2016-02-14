import argparse

def toBinary(numb):
    return str(bin(int(numb)))[2:]

def Main():
    parser = argparse.ArgumentParser(description='shows info about the ip')
    parser.add_argument('IP',nargs='+',help='the ip-address')
    args = parser.parse_args()

    numbers = args.IP[0].split('.')
    binary = []
    for x in numbers:
        binary.append(toBinary(x))

    t = '|{:>{}s}.{:>{}s}.{:>{}s}.{:>{}s}|'
    print(t.format(numbers[0],len(binary[0]),
                   numbers[1],len(binary[1]),
                   numbers[2],len(binary[2]),
                   numbers[3],len(binary[3])))

    print(args.IP[1])

    print(t.format(toBinary(numbers[0]),len(binary[0]),
                   toBinary(numbers[1]),len(binary[1]),
                   toBinary(numbers[2]),len(binary[2]),
                   toBinary(numbers[3]),len(binary[3])))

if __name__ == '__main__':
    Main()

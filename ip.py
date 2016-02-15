import argparse

def toBinary(numb):
    return str(bin(int(numb)))[2:]

def fancyPrint(add):
    print('|',end="")
    for x in range(4):
        print(t.format(numbers[x],len(binary[x])),end="")
        if x < 3:
            print('.',end='')
    print('|')
def Main():
    parser = argparse.ArgumentParser(description='shows info about the ip')
    parser.add_argument('IP',nargs='+',help='the ip-address')
    args = parser.parse_args()

    numbers = args.IP[0].split('.')
    binary = []
    for x in numbers:
        binary.append(toBinary(x))

    t = '{:>{}s}'

    print('|',end="")
    for x in range(4):
        print(t.format(numbers[x],len(binary[x])),end="")
        if x < 3:
            print('.',end='')
    print('|')

    print('|',end="")
    for x in range(4):
        print(t.format(toBinary(numbers[x]),len(binary[x])),end="")
        if x < 3:
            print('.',end='')
    print('|')

    #print(args.IP[1])

if __name__ == '__main__':
    Main()

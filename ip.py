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

    ip = args.IP[0].split('.')
    mask = args.IP[1].split('.')
    binary = [ip[0],ip[1],ip[2],ip[3],
                mask[0],mask[1],mask[2],mask[3]]
    for x in range(8):
        binary[x] = toBinary(binary[x])

    t = '{:>{}s}'

    print('|',end="")
    for x in range(4):
        print(t.format(ip[x],len(binary[x])),end="")
        if x < 3:
            print('.',end='')

    print(' : ',end="")
    for x in range(4):
        print(t.format(mask[x],len(binary[x+4])),end="")
        if x < 3:
            print('.',end='')
    print('|')

    print('|',end="")
    for x in range(4):
        print(t.format(toBinary(ip[x]),len(binary[x])),end="")
        if x < 3:
            print('.',end='')

    print(' : ',end="")
    for x in range(4):
        print(t.format(toBinary(mask[x]),len(binary[x+4])),end="")
        if x < 3:
            print('.',end='')
    print('|')

    #print(args.IP[1])

if __name__ == '__main__':
    Main()

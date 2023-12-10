import sys,os

DEFAULT_DATA = 'switchport trunk allowed vlan add 1108, 1110-1114, 2110'
CONFIG_FILE = 'VlansInit\input_vlans_init.cfg'
EXISTING_VLANS = 'VlansInit\existing_vlans.txt'

def input(file:str) -> list:
    with open(file,encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.append(line)
        return lines

def output(data:str):
    # Example uses single and vlan ranges
    words = data.strip('switchport trunk allowed vlan add')
    words = words.replace(' ','')
    words = words.split(',')

    for number in words:
        if number.__contains__('-'):
            numberList = number.split('-')
            n = int(numberList[0])
            while (n <= int(numberList[1])):
                print('Vlan %s' % (n))
                n+=1
        # Not a range
        else:
            print('Vlan %s' % (number))

def output_dict(data:str,dataDict:dict,existing_vlans:dict) -> dict:
    # Example uses single and vlan ranges
    words = data.strip('switchport trunk allowed vlan add')
    words = words.replace(' ','')
    words = words.replace('\n','') 
    words = words.split(',')

    for number in words:
        if number.__contains__('-'):
            numberList = number.split('-')
            n = int(numberList[0])
            while (n <= int(numberList[1])):
                if n in existing_vlans:
                    n+=1
                    continue

                dataDict[n]='Vlan %d' % (n)
                n+=1

        # Not a range
        else:
            if int(number) in existing_vlans:
                continue

            dataDict[int(number)]='Vlan %d' % int(number)

    return dataDict

def main():
    # An array collection
    input_data = None
    existing_vlans = None

    if os.path.isfile(EXISTING_VLANS):
        existing_vlans = input(EXISTING_VLANS)

    # (Optional) If file exists, create an array
    if os.path.isfile(CONFIG_FILE):
        input_data = input(CONFIG_FILE)
    
    # (Optional) Overwrite data with main() argument
    elif len(sys.argv) > 1:
        data = sys.argv[1]

    # (Optional) Overwrite variable
    else:
        data = DEFAULT_DATA

    current_vlans = {}
    if existing_vlans != None:
        for e in existing_vlans:
            e = e.replace('\n','')
            words = e.split(' ')
            current_vlans[int(words[1])]=e


    if input_data != None:
        dataDict = {}
        for data in input_data:
            if data.__contains__('switchport trunk allowed vlan add') == False:
                continue
            else:
                dataDict = output_dict(data,dataDict,current_vlans)

        for key in dataDict:
            print(dataDict[key])

    # When using a string instead of a CONFIG_FILE
    else:
        print('Input: %s' % (data))
        output(data)

main()

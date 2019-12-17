



import re





def main():
    ress = re.split('\n',s)
    for each in ress:
        res = re.split('\:',each)
        print('"{}":"{}"'.format(res[0],res[1]))

if __name__ == '__main__':
    s = ''''''
    main()
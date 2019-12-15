
import csv




def main():

    with open('demo.csv','w',newline="") as f:      # csv 文件写入
        f_csv = csv.writer(f)
        f_csv.writerow(header)
        f_csv.writerows(rows)



    with open('demo.csv','r') as f:       # csv 文件读取输出
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print(row.get('Username'),row.get('Password'))







if __name__ == '__main__':
    header = ['ID', 'Username', 'Password', 'Age', 'Country']
    rows = [(1001, 'qiye', 'qiye_pass', 24, 'China'),
            (1002, 'Mary', 'Mary_pass', 20, 'USA'),
            (1003, 'Jack', 'Jack_pass', 'USA')]
    main()
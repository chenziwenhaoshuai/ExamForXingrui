import os

if __name__ == '__main__':

    out_dict = {'name': '', 'lei': '', 'sub_fund': ''}
    sub_fund_dict = {'title': '', 'isin': ''}
    isin = []
    sub_fund = []
    with open('long_text.txt', 'r') as f:
        long_text = f.read()
        long_text = long_text.split('\n')
        out_dict['name'] = long_text[0]
        out_dict['lei'] = long_text[1]
        for line in long_text[2:]:
            if '.' in line:
                if len(isin):
                    sub_fund_dict['isin'] = isin
                    sub_fund.append(sub_fund_dict)
                    sub_fund_dict = {'title': '', 'isin': ''}
                sub_fund_dict['title'] = line.split('.')[1]
                isin = []
            else:
                isin.append(line)
        out_dict['sub_fund'] = sub_fund

    print(out_dict)
from bs4 import BeautifulSoup



def csv_write(file_name, data):
    with open(file_name, 'a') as f:
        f.write(','.join(data) + '\n')

if __name__ == '__main__':
    html_path = './web.html'
    f = open(html_path, 'r', encoding='utf-8')
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find(attrs={'class':'VirusTable_1-1-345_38pQEh'}).children
    for item in items:
        if len(item.contents) ==1:
            titles = item.contents[0].contents
            title1 = []
            for title in titles:
                ti = title.contents[0].contents[0].contents[0]
                title1.append(ti)
            print(title1)
            csv_write('./out.csv',title1)
        else:
            for i in item.contents:
                city = i.contents[0].contents[0].contents[1].contents[0]
                xinzeng = i.contents[1].contents[0]
                leiji = i.contents[2].contents[0]
                zhiyu = i.contents[3].contents[0]
                siwang = i.contents[4].contents[0]
                num = [city, xinzeng, leiji, zhiyu, siwang]
                print(num)
                csv_write('./out.csv',num)
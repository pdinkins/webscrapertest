


def webscraper():
    from bs4 import BeautifulSoup
    import requests
    '''
    input file name
    input target website url
    

    '''

    print("================")
    print("Website Scrapper")
    print("====================")
    print("file will be saved as an .html\nin the folder the script is run from")
    print("====================")

    filename = input(str("filesavename: "))
    print("========================")
    url = input(str("url: "))
    print("========================")

    r = requests.get(url)

    soup = BeautifulSoup(r.text)
    for i in range(1000000):
        print(i * 1.1)
    print(soup.prettify())


    f = open(filename + ".html", "w+")
    f.write(soup.prettify())
    f.close()


from bs4 import BeautifulSoup
import requests



def bs4_file_creater(url_id : tuple):
    try:
        
        response = requests.get(url_id[1])
        soup = BeautifulSoup(response.text,'html.parser')
        soup.encode("utf-8")
        # print(soup.text)
        try:
            s = str(soup.select_one(".td-post-title .entry-title").text)
        except Exception as eee:
            print('error ')
            response = requests.get(url_id[1])
            soup = BeautifulSoup(response.text,'html.parser')
            s = str(soup.select_one(".td-post-title .entry-title").text)
        
            
            
        
        
        # s = soup.find_all("html_element", class_="td-post-title")
        p = str(soup.select_one('.td-post-content').text)
        print(p+s)
    # print(s)
    except Exception as e:
        print(e)
        return 'skip'
    else:
        return s+p

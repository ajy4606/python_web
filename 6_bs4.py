import requests
from bs4 import BeautifulSoup

url = "https://land.naver.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element 반환
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a[href]) # a element 의 href 속성 '값' 정보를 출력

# print(soup.find("a", attrs={"class":"NPI=a:article_beta"})) # class="NPI=a:article_beta"인 a element를 찾아줘
# print(soup.find(attrs={"class":"NPI=a:article_beta"})) # class="NPI=a:article_beta"인 element를 찾아줘

# print(soup.find("li", attrs={"class":"menu main_isale"}))
# rank1 = soup.find("li", attrs={"class":"menu main_isale"})
# print(rank1.a)
# print(rank1.a.get_text())
print(rank1.next_sibling.next_sibling)
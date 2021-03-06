# 사용전 필수 패키지들입니다
# pip install selenium // cmd 창에서 입력
# https://chromedriver.chromium.org/downloads  // 자신의 크롬 버전과 맞는 드라이버 다운 후 소스파일과 같은 디렉터리 안에 exe 파일을 저장해주세요
# 크롬 버전은 우측 상단의 점 3개 -> 도움말 -> chrome 정보에서 확인 가능합니다


from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
start_point = input("출발 지점: ")
end_point = input("도착 지점: ")
try:
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_experimental_option('excludeSwitches',['enable-logging'])
    wd = webdriver.Chrome('./chromedriver.exe',options=op)
    wd.get('https://map.naver.com/v5/directions/-/-/-/transit?c=14237419.6299418,4431807.5627088,15,0,0,0,dh')
    wd.implicitly_wait(5)
    start=wd.find_element_by_xpath('/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[1]/directions-search-box[1]/div/div/div[1]/input')
    start.send_keys(start_point)
    start.send_keys(Keys.RETURN)
    time.sleep(1)
    end=wd.find_element_by_xpath('/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[1]/directions-search-box[2]/div/div/div[1]/input')
    end.send_keys(end_point)
    end.send_keys(Keys.RETURN)
    time.sleep(1)
    wd.find_element_by_xpath('/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/directions-search/div[2]/button[2]').click()
    wd.implicitly_wait(5)
    wd.find_element_by_xpath('/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/directions-summary-list/directions-hover-scroll/div/ul/li[1]/directions-summary-item-pubtransit/div[2]/div/button').click()
    time.sleep(1)
    a=wd.find_elements_by_class_name('path_name_text')
    print(a[0].text+' - 출발')
    for i in a[1:-1]:
        print(i.text)
    print(a[-1].text+' - 도착')
except:pass

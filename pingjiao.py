import time
from selenium.webdriver.common.by import By
from selenium import webdriver
 
driver = webdriver.Edge()
 
driver.get(r'https://1.tongji.edu.cn/')

print('1')

while True:
    zhuangtai=1
    cuowu=0
    button=driver.find_elements_by_xpath("//*[contains(text(),' 评教')]")

    while zhuangtai<2:
        try:
            button[0].click()
            time.sleep(2)
            excellent=driver.find_elements_by_xpath("//*[contains(text(),' Excellent')]")
            for j in excellent:
                j.click()
            time.sleep(0.1)
            tijiao=driver.find_elements_by_xpath("//*[contains(text(),'提交')]")[-1].click()
            time.sleep(0.2)
            queding=driver.find_elements_by_class_name('el-button--default')[-1].click()
            time.sleep(3)
            zhuangtai=zhuangtai+1
        except:
            print('错误')
            button=driver.find_elements_by_xpath("//*[contains(text(),' 评教')]")
            cuowu=cuowu+1
        if cuowu>10:
            break
    if cuowu>10:
        break



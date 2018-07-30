from selenium import webdriver
from time import *
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from retry import retry
#from collections import Counter
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#from check_irisnet_chaolian import *
from selenium.webdriver.common.action_chains import ActionChains  #鼠标事件

driver=webdriver.Firefox()
#driver.maximize_window()

#driver.set_page_load_timeout(10)
try:
    driver.get("https://stage.irisnet.org/")
except TimeoutException:
    print('time out after 10 seconds when loading page')
    driver.execute_script('window.stop()') #当页面加载时间超过设定时间，通过执行Javascript来stop加载，即可执行后续动作
    #driver.quit()
    driver.implicitly_wait(10)  # 隐性等待，最长等10秒
#校验按钮的字样显示是否正确
def ck_tf(bt,date):
    for i in range(1,10):
        e=bt.text.strip().replace('\n',' ')
        n=len(e)
        if n==0:
            print("路线图阶段鼠标悬停时没取到内容,正尝试重试%r" %i)
        else:
            break
    if e!=date:
        #print("显示正确%r " %date)
    #else:
        print("显示错误,应该是%r ，目前显示%r" %(date,e))

sleep(2)
#判断导航按钮名称显示是否正确
#首页
bt_home=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/a[1]")
txt_bt_home="Home"
txt_bt_home_CN="主页"
ck_tf(bt_home,txt_bt_home)
#白皮书
bt_whitepaper=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/a[2]")
txt_bt_whitepaper="Whitepaper"
txt_bt_whitepaper_CN="白皮书"
ck_tf(bt_whitepaper,txt_bt_whitepaper)
#网络
bt_network=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/a[3]")
txt_bt_network="Network"
txt_bt_network_CN="网络"
ck_tf(bt_network,txt_bt_network)
#路线图
bt_roadmap=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/a[4]")
txt_bt_roadmap="Roadmap"
txt_bt_roadmap_CN="路线图"
ck_tf(bt_roadmap,txt_bt_roadmap)
#合伙人
bt_Collaboration=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/a[5]")
txt_bt_Collaboration="Collaboration"
txt_bt_Collaboration_CN="合作方"
ck_tf(bt_Collaboration,txt_bt_Collaboration)
#联系
bt_Contact=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/a[6]")
txt_bt_Contact="Contact"
txt_bt_Contact_CN="联系方式"
ck_tf(bt_Contact,txt_bt_Contact)
#中英文切换
bt_English=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/div[2]/div")
txt_bt_English="English"
txt_bt_Chinese="中文"
ck_tf(bt_English,txt_bt_English)

#什么是irisnet按钮
bt_what=driver.find_element_by_xpath(".//*[@id='#']/div/div[1]/a/div/span")
txt_bt_what="What is IRISnet"
txt_bt_what_CN="什么是IRISnet"
ck_tf(bt_what,txt_bt_what)

lab_iris=driver.find_element_by_xpath(".//*[@id='#']/div/div[1]/div/div[1]")
txt_lab_iris="IRIS Network"
txt_lab_iris_CN="IRIS网络"
ck_tf(lab_iris,txt_lab_iris)

#irisnet介绍
# hometext1=driver.find_element_by_class_name("home_txt1").text.strip() #移除字符串头尾的空格或换行符或序列
# hometext=hometext1.replace('\n',' ')   #去除换行符
lab_irisvalue=driver.find_element_by_class_name("home_txt1")  #这样也可以
txt_lab_irisvalue="Inter-chain Service Infrastructure and Protocol Technology Foundation for a Distributed Business Ecosystem"
txt_lab_irisvalue_CN="跨链服务基础协议 新一代分布式商业生态的技术基础"
ck_tf(lab_irisvalue,txt_lab_irisvalue)

#点击what is irisnet 按钮定位
bt_what.click()
sleep(2) #强制等待2秒
#判断是否跳转到IRIS介绍区域
IRIS_introduce=driver.find_element_by_xpath(".//*[@id='#/0/1'] \
                 /div/div[1]/div[1]").is_displayed()
#print(IRIS_introduce)
for i in range(0,5):
    if IRIS_introduce:
        #print("what is IRISnet导航正确")
        break
    else:
        print("what is IRISnet导航错误")
        bt_what.click()


#核心创新标签显示是否正确
lab_keyInnovations=driver.find_element_by_xpath(".//*[@id='#/0/1']/div/div[1]/div[1]")
txt_lab_keyInnovations="Key Innovations"
ck_tf(lab_keyInnovations,txt_lab_keyInnovations)
#核心创新内容是否正确
lab_introduce1=driver.find_element_by_xpath(".//*[@id='#/0/1']/div/div[1]/div[2]")
txt_lab_introduce1="Incorporation of a service-oriented infrastructure into Cosmos"
ck_tf(lab_introduce1,txt_lab_introduce1)
lab_introduce2=driver.find_element_by_xpath(".//*[@id='#/0/1']/div/div[1]/div[3]")
txt_lab_introduce2="Integration of business services offered by heterogeneous "\
+"systems, including public & consortium chains as well as legacy systems"
ck_tf(lab_introduce2,txt_lab_introduce2)
lab_introduce3=driver.find_element_by_xpath(".//*[@id='#/0/1']/div/div[1]/div[4]")
txt_lab_introduce3="Interoperability of those services across an internet of blockchains"
ck_tf(lab_introduce3,txt_lab_introduce3)

#白皮书按钮是否正确
bt_whitepaper2=driver.find_element_by_xpath(".//*[@id='#/0/1']/div/div[1]/div[5]/a/div/span")
txt_bt_whitepaper2="WHITE PAPER"
ck_tf(bt_whitepaper2,txt_bt_whitepaper2)
#导航到网络区域
bt_network.click()

#网络标签显示是否正确
lab_network=driver.find_element_by_xpath(".//*[@id='#/0/2']/div/div[1]/div[1]")
txt_lab_network="Network Design"
ck_tf(lab_network,txt_lab_network)
#网络内容是否正确
lab_network1=driver.find_element_by_xpath(".//*[@id='#/0/2']/div/div[1]/div[2]")
txt_lab_network1="Definition of standard ABCI transaction types supporting " \
+"registration, binding, invocation, query, profiling and governance of " \
+"IRIS Services (a.k.a. iServices)"
ck_tf(lab_network1,txt_lab_network1)

lab_network2=driver.find_element_by_xpath(".//*[@id='#/0/2']/div/div[1]/div[3]")
txt_lab_network2="iService providers act as adaptors of business logic "\
+"residing in public and consortium blockchains as well as enterprise legacy systems"
ck_tf(lab_network2,txt_lab_network2)

lab_network3=driver.find_element_by_xpath(".//*[@id='#/0/2']/div/div[1]/div[4]")
txt_lab_network3="iServices can be invoked across an internet of blockchains over an extended IBC protocol"
ck_tf(lab_network3,txt_lab_network3)

#点击合作伙伴导航
bt_Collaboration.click()
#合作伙伴标签
lab_Collaboration=driver.find_element_by_xpath(".//*[@id='#/0/3']/div/h2")
txt_lab_Collaboration="Collaboration"
ck_tf(lab_Collaboration,txt_lab_Collaboration)

lab_Technology=driver.find_element_by_xpath(".//*[@id='#/0/3']/div/div[2]/article/h4")
txt_lab_Technology="Core Development Teams"
ck_tf(lab_Technology,txt_lab_Technology)

lab_partners=driver.find_element_by_xpath(".//*[@id='#/0/3']/div/div[3]/article/h4")
txt_lab_partners="Strategic Partners"
ck_tf(lab_partners,txt_lab_partners)

lab_partners=driver.find_element_by_xpath(".//*[@id='#/0/3']/div/div[4]/article/h4")
txt_lab_partners_Ecosystem="Ecosystem Partners"
ck_tf(lab_partners,txt_lab_partners_Ecosystem)

lab_Institutions=driver.find_element_by_xpath(".//*[@id='#/0/3']/div/div[5]/article/h4")
txt_lab_Institutions="Institutional Supporters( Listed in no particular order )"
ck_tf(lab_Institutions,txt_lab_Institutions)

lab_Institutions_tishi=driver.find_element_by_xpath(".//*[@id='#/0/3']/div/div[5]/article/h4/span[2]")
txt_lab_Institutions_tishi="( Listed in no particular order )"
ck_tf(lab_Institutions_tishi,txt_lab_Institutions_tishi)

#点击联系导航
bt_Contact.click()
lab_Contact=driver.find_element_by_xpath(".//*[@id='#/0/5']/div/div/div[1]")
txt_lab_Contact="Contact"
ck_tf(lab_Contact,txt_lab_Contact)

#IRIS名字底部介绍
lab_jieshao=driver.find_element_by_xpath(".//*[@id='#/0/5']/div/div/div[4]/p[1]")
txt_lab_jieshao="IRISnet is named after Greek goddess Iris, said to be the personification of the rainbow and the faithful messenger between heaven and humanity"
ck_tf(lab_jieshao,txt_lab_jieshao)

#底部版权
lab_banquan=driver.find_element_by_xpath(".//*[@id='app']/div/div[2]")
txt_lab_banquan="Copyright © 2018 IRIS Foundation Ltd. All rights reserved. Privacy & Terms"
ck_tf(lab_banquan,txt_lab_banquan)


#邮件
lab_email=driver.find_element_by_xpath(".//*[@id='#/0/5']/div/div/div[2]/div[1]/span")
txt_lab_email="Newsletter"
ck_tf(lab_email,txt_lab_email)

lab_Subscribe=driver.find_element_by_xpath(".//*[@id='#/0/5']/div/div/div[2]/a/div/span")
txt_lab_Subscribe="Subscribe"
ck_tf(lab_Subscribe,txt_lab_Subscribe)


lab_tishi=driver.find_element_by_xpath(".//*[@id='#/0/5']/div/div/div[2]/div[2]/input")
txt_lab_tishi="Please enter your email address"
if lab_tishi.get_attribute("placeholder").strip().replace('\n',' ')!=txt_lab_tishi:
    #print("显示正确%r " %txt_lab_tishi)
#else:
    e=lab_tishi.get_attribute("placeholder")
    print("显示错误,应该是%r ，目前显示%r" %(txt_lab_tishi,e))




#路线图导航
bt_roadmap.click()
#路线标签名称
lab_roadmap=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[1]")
txt_lab_roadmap="Roadmap"
ck_tf(lab_roadmap,txt_lab_roadmap)

#盘古
lab_pangu=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[1]/h5/strong")
txt_lab_pangu="PANGU"
ck_tf(lab_pangu,txt_lab_pangu)

lab_pangu_date=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[1]/h5/span")
txt_lab_pangu_date="JAN 2018 - SEP 2018"
ck_tf(lab_pangu_date,txt_lab_pangu_date)

#女娲
lab_nvwa=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[2]/h5/strong")
txt_lab_nvwa="NÜWA"
ck_tf(lab_nvwa,txt_lab_nvwa)

lab_nvwa_date=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[2]/h5/span")
txt_lab_nvwa_date="OCT 2018 - DEC 2018"
ck_tf(lab_nvwa_date,txt_lab_nvwa_date)

#夸父
lab_KUAFU=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[3]/h5/strong")
txt_lab_KUAFU="KUAFU"
ck_tf(lab_KUAFU,txt_lab_KUAFU)

lab_KUAFU_date=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[3]/h5/span")
txt_lab_KUAFU_date="JAN 2019 - JUN 2019"
ck_tf(lab_KUAFU_date,txt_lab_KUAFU_date)

#后羿
lab_HOUYI=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[4]/h5/strong")
txt_lab_HOUYI="HOUYI"
ck_tf(lab_HOUYI,txt_lab_HOUYI)

lab_HOUYI_date=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[4]/h5/span")
txt_lab_HOUYI_date="BEYOND JUL 2019"
ck_tf(lab_HOUYI_date,txt_lab_HOUYI_date)

#鼠标悬停盘古上,前面的等6秒是为了让控件的一些事件方法加载完整，否则悬停无法显示内容

sleep(6)
ActionChains(driver).move_to_element(lab_pangu).perform()

lab_pangu_val=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[1]/p")
txt_lab_pangu_val="The first stage of the IRIS project will focus on having "\
+"the IRIS Hub up and running and connected to the Cosmos Hub. We also intend "\
+"to release an initial version of the mobile client for the IRIS network."

ck_tf(lab_pangu_val,txt_lab_pangu_val)
#悬停在女娲
sleep(6)
ActionChains(driver).move_to_element(lab_nvwa).perform()
lab_nvwa_val=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[2]/p")
txt_lab_nvwa_val="The second stage will focus on building the fundamental IRIS "\
+"Service Layer. This will involve enabling service definition, binding, "\
+"invocation and query. In this stage we are also aiming to have a beta "\
+"version of the IRIS SDK ready for developers."
ck_tf(lab_nvwa_val,txt_lab_nvwa_val)
#悬停在夸父
sleep(6)
ActionChains(driver).move_to_element(lab_KUAFU).perform()
lab_KUAFU_val=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[3]/p")
txt_lab_KUAFU_val="The third stage will focus on incremental upgrades to the IRIS network in order to support our planned advanced IRIS Service governance features."
ck_tf(lab_KUAFU_val,txt_lab_KUAFU_val)

#悬停在后羿
sleep(6)
ActionChains(driver).move_to_element(lab_HOUYI).perform()
lab_HOUYI_val=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[4]/p")
txt_lab_HOUYI_val="The fourth stage will focus on further technology innovations to the IRIS network, IRIS SDK and mobile client, as well as developer engagement."
ck_tf(lab_HOUYI_val,txt_lab_HOUYI_val)

sleep(6)
#悬停中英文切换上
ActionChains(driver).move_to_element(bt_English).perform()
#点击中文显示
bt_Chinese=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/div[2]/a")
bt_Chinese.click()
driver.implicitly_wait(10)

#######################
bt_home=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/a[1]")
ck_tf(bt_home,txt_bt_home_CN)
#白皮书
bt_whitepaper=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/a[2]")
ck_tf(bt_whitepaper,txt_bt_whitepaper_CN)
#网络
bt_network=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/a[3]")
ck_tf(bt_network,txt_bt_network_CN)
#路线图
bt_roadmap=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/a[4]")
ck_tf(bt_roadmap,txt_bt_roadmap_CN)
#合伙人
bt_Collaboration=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/a[5]")
ck_tf(bt_Collaboration,txt_bt_Collaboration_CN)
#联系
bt_Contact=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/a[6]")
ck_tf(bt_Contact,txt_bt_Contact_CN)
#中英文切换
bt_Chinese=driver.find_element_by_xpath(".//*[@id='index']/div[1]/div/div/div[2]/div")
ck_tf(bt_Chinese,txt_bt_Chinese)

#什么是irisnet按钮
bt_what_CN=driver.find_element_by_xpath(".//*[@id='#']/div/div[1]/a/div/span")
ck_tf(bt_what_CN,txt_bt_what_CN)
lab_iris=driver.find_element_by_xpath(".//*[@id='#']/div/div[1]/div/div[1]")
ck_tf(lab_iris,txt_lab_iris_CN)

#irisnet介绍
lab_irisvalue=driver.find_element_by_class_name("home_txt1")
ck_tf(lab_irisvalue,txt_lab_irisvalue_CN)


#############################
bt_what_CN.click()
sleep(2) #强制等待2秒
#判断是否跳转到IRIS介绍区域
IRIS_introduce=driver.find_element_by_xpath(".//*[@id='#/0/1'] \
                 /div/div[1]/div[1]").is_displayed()
#print(IRIS_introduce)
for i in range(0,5):
    if IRIS_introduce:
        #print("what is IRISnet导航正确")
        break
    else:
        print("what is IRISnet导航错误")
        bt_what.click()


#核心创新标签显示是否正确
lab_keyInnovations=driver.find_element_by_xpath(".//*[@id='#/0/1']/div/div[1]/div[1]")
txt_lab_keyInnovations_CN="核心创新"
ck_tf(lab_keyInnovations,txt_lab_keyInnovations_CN)
#核心创新内容是否正确
lab_introduce1=driver.find_element_by_xpath(".//*[@id='#/0/1']/div/div[1]/div[2]")
txt_lab_introduce1_CN="将面向服务的基础设施融入到Cosmos网络中"
ck_tf(lab_introduce1,txt_lab_introduce1_CN)
lab_introduce2=driver.find_element_by_xpath(".//*[@id='#/0/1']/div/div[1]/div[3]")
txt_lab_introduce2_CN="整合由异构系统提供的商业服务，包括公共链、联盟链以及现有系统"
ck_tf(lab_introduce2,txt_lab_introduce2_CN)
lab_introduce3=driver.find_element_by_xpath(".//*[@id='#/0/1']/div/div[1]/div[4]")
txt_lab_introduce3_CN="通过区块链互联网实现服务的互联互通"
ck_tf(lab_introduce3,txt_lab_introduce3_CN)

#白皮书按钮是否正确
bt_whitepaper2=driver.find_element_by_xpath(".//*[@id='#/0/1']/div/div[1]/div[5]/a/div/span")
txt_bt_whitepaper2_CN="白皮书"
ck_tf(bt_whitepaper2,txt_bt_whitepaper2_CN)
#导航到网络区域
bt_network.click()

#网络标签显示是否正确
lab_network=driver.find_element_by_xpath(".//*[@id='#/0/2']/div/div[1]/div[1]")
txt_lab_network_CN="网络设计"
ck_tf(lab_network,txt_lab_network_CN)
#网络内容是否正确
lab_network1=driver.find_element_by_xpath(".//*[@id='#/0/2']/div/div[1]/div[2]")
txt_lab_network1_CN="通过标准的ABCI交易实现IRIS服务（也称为iServices）的注册，绑定，调用，查询，分析和管理"
ck_tf(lab_network1,txt_lab_network1_CN)

lab_network2=driver.find_element_by_xpath(".//*[@id='#/0/2']/div/div[1]/div[3]")
txt_lab_network2_CN="iService提供商充当公共链、联盟区块链以及现有企业系统中业务逻辑的适配器"
ck_tf(lab_network2,txt_lab_network2_CN)

lab_network3=driver.find_element_by_xpath(".//*[@id='#/0/2']/div/div[1]/div[4]")
txt_lab_network3_CN="可以通过扩展的IBC协议在区块链互联网中调用iServices"
ck_tf(lab_network3,txt_lab_network3_CN)

#点击合作伙伴导航
bt_Collaboration.click()
#合作伙伴标签
lab_Collaboration=driver.find_element_by_xpath(".//*[@id='#/0/3']/div/h2")
txt_lab_Collaboration_CN="合作方"
ck_tf(lab_Collaboration,txt_lab_Collaboration_CN)

lab_Technology=driver.find_element_by_xpath(".//*[@id='#/0/3']/div/div[2]/article/h4")
txt_lab_Technology_CN="核心开发团队"
ck_tf(lab_Technology,txt_lab_Technology_CN)

lab_partners=driver.find_element_by_xpath(".//*[@id='#/0/3']/div/div[3]/article/h4")
txt_lab_partners_CN="战略合作伙伴"
ck_tf(lab_partners,txt_lab_partners_CN)

lab_partners_Ecosystem=driver.find_element_by_xpath(".//*[@id='#/0/3']/div/div[4]/article/h4")
txt_lab_partners_Ecosystem_CN="生态合作伙伴"
ck_tf(lab_partners_Ecosystem,txt_lab_partners_Ecosystem_CN)



lab_Institutions=driver.find_element_by_xpath(".//*[@id='#/0/3']/div/div[5]/article/h4")
txt_lab_Institutions_CN="支持机构( 排名不分先后 )"
ck_tf(lab_Institutions,txt_lab_Institutions_CN)


txt_lab_Institutions_tishi=driver.find_element_by_xpath(".//*[@id='#/0/3']/div/div[5]/article/h4/span[2]")
txt_lab_Institutions_tishi_CN="( 排名不分先后 )"
ck_tf(lab_Institutions_tishi,txt_lab_Institutions_tishi_CN)

#点击联系导航
bt_Contact.click()
lab_Contact=driver.find_element_by_xpath(".//*[@id='#/0/5']/div/div/div[1]")
txt_lab_Contact_CN="联系方式"
ck_tf(lab_Contact,txt_lab_Contact_CN)

#IRIS名字底部介绍
lab_jieshao=driver.find_element_by_xpath(".//*[@id='#/0/5']/div/div/div[4]/p[1]")
txt_lab_jieshao_CN="IRISnet以希腊彩虹女神Iris命名，她是在人间和天堂之间传递信息的忠诚使者"
ck_tf(lab_jieshao,txt_lab_jieshao_CN)

#底部版权
lab_banquan=driver.find_element_by_xpath(".//*[@id='app']/div/div[2]")
txt_lab_banquan_CN="Copyright © 2018 IRIS Foundation Ltd. All rights reserved. Privacy & Terms"
ck_tf(lab_banquan,txt_lab_banquan_CN)


#邮件
lab_email=driver.find_element_by_xpath(".//*[@id='#/0/5']/div/div/div[2]/div[1]/span")
txt_lab_email_CN="获取最新资讯"
ck_tf(lab_email,txt_lab_email_CN)

lab_Subscribe=driver.find_element_by_xpath(".//*[@id='#/0/5']/div/div/div[2]/a/div/span")
txt_lab_Subscribe_CN="提交"
ck_tf(lab_Subscribe,txt_lab_Subscribe_CN)


lab_tishi=driver.find_element_by_xpath(".//*[@id='#/0/5']/div/div/div[2]/div[2]/input")
txt_lab_tishi_CN="请输入你的邮箱地址"
if lab_tishi.get_attribute("placeholder").strip().replace('\n',' ')!=txt_lab_tishi_CN:
    #print("显示正确%r " %txt_lab_tishi_CN)
#else:
    e=lab_tishi.get_attribute("placeholder")
    print("显示错误,应该是%r ，目前显示%r" %(txt_lab_tishi_CN,e))




#路线图导航
bt_roadmap.click()
#路线标签名称
lab_roadmap=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[1]")
txt_lab_roadmap_CN="路线图"
ck_tf(lab_roadmap,txt_lab_roadmap_CN)

#盘古
lab_pangu=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[1]/h5/strong")
txt_lab_pangu_CN="盘古"
ck_tf(lab_pangu,txt_lab_pangu_CN)

lab_pangu_date=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[1]/h5/span")
txt_lab_pangu_date_CN="2018年1月- 2018年9月"
ck_tf(lab_pangu_date,txt_lab_pangu_date_CN)

#女娲
lab_nvwa=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[2]/h5/strong")
txt_lab_nvwa_CN="女娲"
ck_tf(lab_nvwa,txt_lab_nvwa_CN)

lab_nvwa_date=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[2]/h5/span")
txt_lab_nvwa_date_CN="2018年10月 - 2018年12月"
ck_tf(lab_nvwa_date,txt_lab_nvwa_date_CN)

#夸父
lab_KUAFU=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[3]/h5/strong")
txt_lab_KUAFU_CN="夸父"
ck_tf(lab_KUAFU,txt_lab_KUAFU_CN)

lab_KUAFU_date=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[3]/h5/span")
txt_lab_KUAFU_date_CN="2019年1月 - 2019年6月"
ck_tf(lab_KUAFU_date,txt_lab_KUAFU_date_CN)

#后羿
lab_HOUYI=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[4]/h5/strong")
txt_lab_HOUYI_CN="后羿"
ck_tf(lab_HOUYI,txt_lab_HOUYI_CN)

lab_HOUYI_date=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[4]/h5/span")
txt_lab_HOUYI_date_CN="2019年7月之后"
ck_tf(lab_HOUYI_date,txt_lab_HOUYI_date_CN)

#鼠标悬停盘古上,前面的等6秒是为了让控件的一些事件方法加载完整，否则悬停无法显示内容

sleep(6)
ActionChains(driver).move_to_element(lab_pangu).perform()

lab_pangu_val=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[1]/p")
txt_lab_pangu_val_CN="作为 IRISnet 项目的第一阶段，我们将专注于构建 IRISnet，"\
+"以及完成 Cosmos 生态中第一个区域性枢纽 IRIS Hub 和 Cosmos Hub的链接。同时，我们"\
+"将发布一个初始版本的IRIS网络移动客户端。"

ck_tf(lab_pangu_val,txt_lab_pangu_val_CN)
#悬停在女娲
sleep(6)
ActionChains(driver).move_to_element(lab_nvwa).perform()
lab_nvwa_val=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[2]/p")
txt_lab_nvwa_val_CN="在这一阶段，我们将建立 IRISnet 基本服务层： 升级网络以实现服务"\
+"定义、绑定、调用和查询; 为开发者准备了beta版的IRIS SDK，并升级移动客户端以支持IRIS"\
+"服务; 与分布式应用链项目形成战略联盟，支持应用链（分区）连接IRIS枢纽。"
ck_tf(lab_nvwa_val,txt_lab_nvwa_val_CN)
#悬停在夸父
sleep(6)
ActionChains(driver).move_to_element(lab_KUAFU).perform()
lab_KUAFU_val=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[3]/p")
txt_lab_KUAFU_val_CN="第三阶段主要专注于完成IRIS网络的增强功能，升级网络以支持复杂的IRIS"\
+"服务管理功能，例如：分析和争议解决; 不断完善SDK和手机客户端; 加速拓展网络，连接更多"\
+"的分区，整合更多的服务提供商。"
ck_tf(lab_KUAFU_val,txt_lab_KUAFU_val_CN)

#悬停在后羿
sleep(6)
ActionChains(driver).move_to_element(lab_HOUYI).perform()
lab_HOUYI_val=driver.find_element_by_xpath(".//*[@id='#/0/4']/div[2]/div[1]/div/div[4]/p")
txt_lab_HOUYI_val_CN="通过不懈的技术创新，完善的社区建设和可持续的开发者支持以实现分布式商业生态系统。"
ck_tf(lab_HOUYI_val,txt_lab_HOUYI_val_CN)

print("测试完成")
input("是否退出？按回车即可退出")
driver.quit()

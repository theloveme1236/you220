import os
import subprocess
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from pymongo import MongoClient
import requests
import pickle
from datetime import datetime, timedelta
import base64
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
import sys
import random
from seleniumbase import get_driver
cluster = MongoClient('mongodb+srv://theloveme1238:zx5LtPcgLpcpIh7D@cluster0.pzuhxov.mongodb.net/?retryWrites=true&w=majority')
db = cluster["my_database"]
collection = db["users"]        
driver = get_driver("chrome")
driver.implicitly_wait(10)
            
driver.maximize_window()
con = 0
errrrroo = 0
Subscribe_erro_stop_time= 'start'
like_erro_stop_time = 'start'
stop_def_Subscribe = 'start'
def cookis_like():
    global driver
    for cookie in cookies:
        
        fields = cookie.strip().split('\t')
        if len(fields) >= 7:
            cookie_dict = {'name': fields[5],'value': fields[6],'domain': fields[0],'path': fields[2],'expires': int(fields[4]),'secure': bool(fields[3])}
            driver.add_cookie(cookie_dict)
    driver.refresh()

def like3like_login():
    global email
    global driver
    current_url = driver.current_url
    if current_url=='https://www.like4like.org/login/':
        
        print('https://www.like4like.org/login/')
        for cookies_totel in os.listdir(os.getcwd()):    
            cookies_totel_1 = cookies_totel.split('_cookies')[0]
            if cookies_totel_1=='like':
                email = cookies_totel.split('like_cookies_')[-1].split('.pkl')[0]
                print(email)
                password = '1234thelove'
                driver.get("https://www.like4like.org/login/")
                time.sleep(2)
                driver.find_element(By.ID, 'username').send_keys(email)
                time.sleep(2)
                driver.find_element(By.ID, 'password').send_keys(password)
                time.sleep(2)
                try:
                    driver.find_element(By.XPATH, '/html/body/div[6]/form/fieldset/table/tbody/tr[8]/td/span').click()
                except:
                    pass
                time.sleep(10)
                driver.get("https://www.like4like.org/user/")
                time.sleep(10)
                current_url = driver.current_url
                if current_url=='https://www.like4like.org/user/':
                    print(current_url)
                    print('login_usearname_passowrd')
                    driver.get("https://www.like4like.org/#social-media-platform-list")
                    time.sleep(5)
                    cookies_add = "like_cookies_{}.pkl".format(email)
                    pickle.dump(driver.get_cookies(), open("like_cookies_{}.pkl".format(email), "wb"))
                    email_to_find = email
                    user_data = collection.find_one({"email": email_to_find})
                    new_login_like_1 = 'true_login'
                    collection.update_one(
                        {"email": email_to_find},
                        {"$set": {"login_like": new_login_like_1}}
                    )
                    print('login_usearname_passowrd_true')
                    
                else:
                    print('first_logon_cookies')
                    driver.get("https://www.like4like.org/#social-media-platform-list")
                    cookies = pickle.load(open('{}'.format(cookies_totel), "rb"))
                    for cookie in cookies:
                        try:
                            driver.add_cookie(cookie)
                        except Exception as ss:
                            print(ss)
                            continue
                    driver.get("https://www.like4like.org/user/")
                    time.sleep(15)
                    current_url = driver.current_url
                    if current_url=='https://www.like4like.org/user/':
                        email_to_find = email
                        user_data = collection.find_one({"email": email_to_find})
                        new_login_like_2 = 'login_cookies'
                        collection.update_one(
                            {"email": email_to_find},
                            {"$set": {"login_like": new_login_like_2}}
                        )
                        print('first_logon_cookies_true')
                    else:
                        print('first_logon_cookies_flase')
                        email_to_find = email
                        user_data = collection.find_one({"email": email_to_find})
                        new_login_like = 'false'

                        collection.update_one(
                            {"email": email_to_find},
                            {"$set": {"login_like": new_login_like}}
                        )
                        driver.quit()
                
for cookies_totel in os.listdir(os.getcwd()):
    cookies_totel_1 = cookies_totel.split('_cookies')[0]
    if cookies_totel_1=='like':
        email = cookies_totel.split('like_cookies_')[-1].split('.pkl')[0]
        print(email)
        password = '1234thelove'
        driver.get("https://www.like4like.org/login/")
        time.sleep(2)
        driver.find_element(By.ID, 'username').send_keys(email)
        time.sleep(2)
        driver.find_element(By.ID, 'password').send_keys(password)
        time.sleep(2)
        try:
            driver.find_element(By.XPATH, '/html/body/div[6]/form/fieldset/table/tbody/tr[8]/td/span').click()
        except:
            pass
        time.sleep(10)
        driver.get("https://www.like4like.org/user/")
        time.sleep(10)

        current_url = driver.current_url
        if current_url=='https://www.like4like.org/user/':
            print(current_url)
            driver.get("https://www.like4like.org/#social-media-platform-list")
            time.sleep(5)
            cookies_add = "like_cookies_{}.pkl".format(email)
            pickle.dump(driver.get_cookies(), open("like_cookies_{}.pkl".format(email), "wb"))
            email_to_find = email
            user_data = collection.find_one({"email": email_to_find})
            new_login_like_4 = 'login_fisrt_cookies'
            collection.update_one(
                {"email": email_to_find},
                {"$set": {"login_like": new_login_like_4}}
            )

        else:
            print('else')
            driver.get("https://www.like4like.org/#social-media-platform-list")
            cookies = pickle.load(open('{}'.format(cookies_totel), "rb"))
            for cookie in cookies:
                try:
                    driver.add_cookie(cookie)
                except Exception as ss:
                    print(ss)
                    continue
            driver.get("https://www.like4like.org/user/")
            time.sleep(15)
            current_url = driver.current_url
            if current_url=='https://www.like4like.org/user/':
                print('login_cookies')
                email_to_find = email
                user_data = collection.find_one({"email": email_to_find})
                new_login_like_6 = 'login_cookies'
                collection.update_one(
                    {"email": email_to_find},
                    {"$set": {"login_like": new_login_like_6}}
                )
            else:
                print('false_cookies')
                email_to_find = email
                user_data = collection.find_one({"email": email_to_find})
                new_login_like = 'false_cookies'

                collection.update_one(
                    {"email": email_to_find},
                    {"$set": {"login_like": new_login_like}}
                )
                driver.quit()
                sys.exit()
                
    if cookies_totel_1=='youtube':
        driver.get("https://www.youtube.com/")
        print(cookies_totel)

        for cookies_totel in os.listdir(os.getcwd()):
            cookies_totel_1 = cookies_totel.split('_cookies')[0]
            if cookies_totel_1=='youtube':
                
                email = cookies_totel.split('youtube_cookies_')[-1].split('.txt')[0]
                with open(cookies_totel, 'r') as file:
                    cookies = file.readlines()
                cookis_like()
                driver.get("https://www.youtube.com/account")
                time.sleep(10) 
                account_true = driver.current_url
                if account_true=='https://www.youtube.com/account' or account_true=='https://www.youtube.com/account/':
                    
                    email_to_find = email
                    user_data = collection.find_one({"email": email_to_find})
                    new_login_youtube = 'youtube_cookies_true'

                    collection.update_one(
                        {"email": email_to_find},
                        {"$set": {"login_youtube": new_login_youtube}}
                        )
                else:
                    
                    email_to_find = email
                    user_data = collection.find_one({"email": email_to_find})
                    new_login_youtube = 'youtube_cookies_false'

                    collection.update_one(
                        {"email": email_to_find},
                        {"$set": {"login_youtube": new_login_youtube}}
                        )
                    driver.quit()
                    sys.exit()

        
def limeit_all_ike4like():
    global driver
    if like_erro_stop_time == 'stop':#Subscribe_erro_stop_time == 'stop' and 
        
        email_to_find = email
        user_data = collection.find_one({"email": email_to_find})
        failed_stop_all = 'Sub_like'
        collection.update_one(
            {"email": email_to_find},
            {"$set": {"limit": failed_stop_all}})
        print('failed_stop_all_like4like')
        sys.exit()
def check_driver_open():
    try:
        all_windows = driver.window_handles
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                driver.switch_to.window(window)
                driver.close()
            driver.switch_to.window(driver.window_handles[0])
    except Exception as ddfrs:
        print('check_driver_open: ' , ddfrs)
def no_Window_driver():
    global driver
    print('NoSuchWindowException_stop')
    driver = get_driver("chrome")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.like4like.org/#social-media-platform-list")
    time.sleep(10)
    like3like_login()
    print('NoSuchWindowException_open')    
def failed_success_minutes():
    global Subscribe_erro_stop_time
    global like_erro_stop_time
    global driver
    global stop_def_Subscribe
    try:
        erro_minutes=driver.find_element(By.ID, 'error-text').text
        You_have_failed  = erro_minutes.split(' success rate validation')[0]
        if You_have_failed == str('You have failed our'):
            print('You have failed our')
            stop_def_Subscribe= 'stop'
            minutes_to_add =  erro_minutes.split('next ')[-1].split(' minutes.')[0]
            print(minutes_to_add)
            current_time = datetime.utcnow()
            time_delta = timedelta(minutes=int(minutes_to_add))
            new_time = current_time + time_delta
            new_date = new_time.date()
            formatted_time = new_time.strftime('%H:%M')
            failed_success= "date:" + str(new_date) + "time:"+ str(formatted_time)
            print(failed_success)
            email_to_find = email
            user_data = collection.find_one({"email": email_to_find})
            
            
           
            current_url = driver.current_url
            if current_url=='https://www.like4like.org/earn-credits.php?feature=youtubes':
                print('Subscribe_erro_stop_time')
                Subscribe_erro_stop_time = 'stop'
                collection.update_one(
                {"email": email_to_find},
                {"$set": {"limit_sub": failed_success}}) 
            if current_url=='https://www.like4like.org/earn-credits.php?feature=youtube':
                print('like_erro_stop_time')
                like_erro_stop_time = 'stop'
                collection.update_one(
                {"email": email_to_find},
                {"$set": {"limit_like": failed_success}})
            
        if erro_minutes == 'No tasks are currently available, please try again later...':
            print('No tasks are currently available')
            stop_def_Subscribe= 'stop'
        #driver.quit()
    except NoSuchWindowException:
        print('failed_success_minutes')
        no_Window_driver()
        like3like_login()

    except NoSuchElementException:
        limeit_all_ike4like()
        like3like_login()
        print('NoSuchElementException_failed_success_minutes')
    except Exception as ssssd2:
        like3like_login()
        print('failed_success_minutes:  ',ssssd2)
def Subscribe_erroo():
    global driver
    global con_sub
    failed_success_minutes()
    limeit_all_ike4like()
    driver.switch_to.window(driver.window_handles[0])
    driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")
    time.sleep(10)
    like3like_login()
    check_driver_open()
    if Subscribe_erro_stop_time == 'stop':
        print('stop_Subscribe')
        #like()
    con_sub +=1
    if con_sub == 5:
        print('con_sub')
        #like()
def Subscribe():
    global driver
    global con_sub
    driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")
    con_sub = 0
    for s in range(25):
        try:
            
            driver.maximize_window()
            driver.implicitly_wait(15)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1);")
            time.sleep(5)
            if stop_def_Subscribe == 'stop':
                print('stop_def_Subscribe_stop_def_Subscribe_stop_def_Subscribe')
                break
            driver.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
             
            #element_control_click.click()
            driver.switch_to.window(driver.window_handles[-1])
            subscribe_button = driver.find_element(By.CSS_SELECTOR, "div#subscribe-button button span.yt-core-attributed-string").text
            if subscribe_button== "Subscribe" or subscribe_button == "اشتراك":
                sub_old_count = driver.find_element(By.ID, 'subscriber-count').text
                time.sleep(2)
                driver.find_element(By.ID, 'subscribe-button').click()
                time.sleep(2)
                driver.refresh()
                time.sleep(2)
                sub_new_count = driver.find_element(By.ID, 'subscriber-count').text
                if sub_new_count == sub_old_count:
                    print('sub_old_count:',sub_old_count)
                    print('==')
                    print('sub_new_count:',sub_new_count)
                    if 'K' in sub_new_count or 'ألف' in sub_new_count:
                        result = "find"
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        time.sleep(5)
                        driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()
                    else:
                        result = "no fond"
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        time.sleep(5)
                        driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")

                    print(result)

                    
                elif sub_old_count < sub_new_count  :
                    print('_______________________________________________________________')
                    print('sub_old_count:',sub_old_count)
                    print('<')
                    print('sub_new_count:',sub_new_count)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(5)
                    driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()
                    
                elif sub_old_count > sub_new_count:
                    print('_______________________________________________________________')
                    print('sub_old_count:',sub_old_count)
                    print('>')
                    print('sub_new_count:',sub_new_count)
                    '''
                    driver.find_element(By.CSS_SELECTOR, "#items > ytd-menu-service-item-renderer:nth-child(4)").click()
                    time.sleep(2)
                    driver.find_element(By.CSS_SELECTOR, "#confirm-button > yt-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill").click()
                    time.sleep(2)
                    '''
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(5)
                    driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")
                else:
                    print('خطاء')
                     
                
          
            else:
                print('unsubscribe')
                '''
                driver.switch_to.window(driver.window_handles[1])
                
                driver.find_element(By.ID, 'subscribe-button').click()
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer[4]]").click()
                time.sleep(2)
                '''
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(random.randrange(3, 7))
                driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")



            email_to_find = email
            user_data = collection.find_one({"email": email_to_find})
            if user_data:
                current_sub_value = int(user_data.get("sub", 0))
                new_sub_value = current_sub_value + 1
                print('sub', int(new_sub_value))
                collection.update_one(
                    {"email": email_to_find},
                    {"$set": {"sub": new_sub_value}}
                )

            else:
                
                pass
        except NoSuchWindowException:
            print('sub: NoSuchWindowException_stop')
            no_Window_driver()
            like3like_login()
            print('sub: NoSuchWindowException_open')
        except NoSuchElementException:
            print('NoSuchElementException_sub')
            Subscribe_erroo()

                
        except Exception as s2:
            print('Subscribe_erroo:   ',s2)
            Subscribe_erroo()

def like_erro():
    global driver
    global con_like
    limeit_all_ike4like()
    failed_success_minutes()
    try:
        if like_erro_stop_time == 'stop':
            print('Subscribe__stop_time_NoSuchElementException')
            #Subscribe()
        con_like+=1
        if con_like == 5:
            print('con_like')
            #Subscribe()
        driver.switch_to.window(driver.window_handles[0])
        driver.get("https://www.like4like.org/earn-credits.php?feature=youtube")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
        time.sleep(10)
        like3like_login()
        check_driver_open()


    except Exception as s3:
        print(s3)
    
def like():
    global driver
    global con_like
    driver.get("https://www.like4like.org/earn-credits.php?feature=youtube")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

    con_like = 0
    for s in range(30):
        try:
            
            driver.maximize_window()
            driver.implicitly_wait(15)
            time.sleep(5)
            element_control_click = driver.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)
            like_old_count = driver.find_element(By.ID, 'segmented-like-button').text
            time.sleep(2)
            driver.find_element(By.ID, 'segmented-like-button').click()
            time.sleep(2)
            driver.refresh()
            time.sleep(2)
            like_new_count = driver.find_element(By.ID, 'segmented-like-button').text
            if like_new_count == like_old_count:
                print('like_old_count:',like_old_count)
                print('==')
                print('like_new_count:',like_new_count)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(5)
                driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()
            elif like_old_count < like_new_count  :
                print('_______________________________________________________________')
                print('like_old_count:',like_old_count)
                print('<')
                print('like_new_count:',like_new_count)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(5)
                driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()
                    
            elif like_old_count > like_new_count:
                print('_______________________________________________________________')
                print('like_old_count:',like_old_count)
                print('>')
                print('like_new_count:',like_new_count)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(5)
                driver.get("https://www.like4like.org/earn-credits.php?feature=youtube")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            else:
                print('errro')            
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(5)
                driver.get("https://www.like4like.org/earn-credits.php?feature=youtube")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            email_to_find = email
            user_data = collection.find_one({"email": email_to_find})
            
            if user_data:
                current_sub_value = int(user_data.get("like", 0))

                # تعديل القيمة وإضافة +1
                new_sub_value = current_sub_value + 1
                print('like', int(new_sub_value))
                # تحديث الوثيقة بالقيمة الجديدة لـ sub
                collection.update_one(
                    {"email": email_to_find},
                    {"$set": {"like": new_sub_value}}
                    )
        except NoSuchWindowException:
            print('like: NoSuchWindowException_stop')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

            no_Window_driver()
            print('like: NoSuchWindowException_open')
        except NoSuchElementException:
            print('NoSuchElementException_like')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

            like_erro()
        except Exception as s:
            print('Subscribe_erroo:   ',s)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            like_erro()

Subscribe()
like()

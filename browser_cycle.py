
# coding: utf-8

# In[2]:


import webbrowser
import os, signal
import time

def check_kill_process(pstring):
    for line in os.popen("ps ax | grep " + pstring + " | grep -v grep"):
        fields = line.split()
        pid = fields[0]
    os.kill(int(pid), signal.SIGKILL)
    
alexa_top_25 = [
             'http://www.google.com',
             'http://www.youtube.com',
#              'http://www.facebook.com',
#              'http://www.baidu.com',
#              'http://www.wikipedia.org',
#              'http://www.yahoo.com',
#              'http://www.reddit.com',
#              'http://www.qq.com',
#              'http://www.taobao.com',
#              'http://amazon.com',
#              'http://www.twitter.com',             
#              'http://www.instagram.com', 
#              'http://www.tmall.com',
#              'http://www.sohu.com',
#              'http://www.live.com',
#              'http://www.vk.com',
#              'http://www.jd.com',
#              'http://www.sina.com.cn',
#              'http://www.weibo.com',
#              'http://www.yandex.ru',
#              'http://www.360.cn',
#              'http://www.blogspot.com',
#              'http://www.netflix.com',
#              'http://www.login.tmall.com',
#              'http://www.linkedin.com',
#              'http://www.twitch.tv',
#              'http://www.microsoft.com',
#              'http://www.csdn.net',
#              'http://www.bing.com',
#              'http://www.alipay.com',
#              'http://www.office.com',
#              'http://www.msn.com ',
#              'http://www.aliexpress.com'
               ]
    

for x in range (1 ,10):                             
    for y in alexa_top_25:
        webbrowser.open(y)
        time.sleep(15)
        check_kill_process('firefox'')
        time.sleep(5)





    


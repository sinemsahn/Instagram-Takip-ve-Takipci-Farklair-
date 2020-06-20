from selenium import webdriver
from instagramUserinfo import name , password
import time
from selenium.webdriver.common.keys import Keys
class Instagram:
    def __init__(self,name,password):
        self.browser=webdriver.Chrome()
        self.browser.set_window_size(900,900)
        self.name=name
        self.password=password

 
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
  
        nameInput=self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
        passwordInput=self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
        nameInput.send_keys(self.name)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)






    def getFollowers(self):
  
        self.browser.get("https://www.instagram.com/"+self.name)
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        
        time.sleep(2)
        dialog=self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')

        followersCount = len(dialog.find_elements_by_css_selector("li"))
        print(str(followersCount )+" tane takipçi yüklendi")
    
       
        
        while True:

            dialog.click() #ul gelir
           
            self.browser.find_element_by_xpath('/html/body').send_keys(Keys.END)
            time.sleep(2)
            newCount=len(dialog.find_elements_by_css_selector("li"))
        
            time.sleep(2)
            
            if newCount != followersCount:
                followersCount = newCount
                print("yeni sayı "+ str(newCount) )
                
                
            else:
                 break
          

            

        followers=dialog.find_elements_by_css_selector("li")
        file=open("followers.txt","a")
        time.sleep(2)
        for user in followers:
            link=user.find_element_by_css_selector("a").get_attribute("href")
            file.write(link+"\n")
        

            print(link)
        file.close()
        return followersCount
    

    def getFollowing(self):
        self.browser.get("https://www.instagram.com/"+self.name)
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        
        time.sleep(2)
        dialog=self.browser.find_element_by_css_selector("div[role=dialog] ul")

        followersCount=len(dialog.find_elements_by_css_selector("li"))
        print(str(followersCount)+" tane takipettiğin yüklendi")
        #action=webdriver.ActionChains(self.browser)#browserı kıpırdatıyoruz
 

        while True:
            dialog.click() #ul gelir
            
            self.browser.find_element_by_tag_name('body').send_keys(Keys.END)
            
            time.sleep(2)
            newCount=len(dialog.find_elements_by_css_selector("li"))

            if newCount != followersCount:
                followersCount=newCount
                print("yeni sayı "+ str(newCount) )
                
                
            else:
                break


        followers=dialog.find_elements_by_css_selector("li")
        file=open("following.txt","a")
        time.sleep(2)
        for user in followers:
            link=user.find_element_by_css_selector("a").get_attribute("href")
           
            file.write(link+"\n")
            print(link)


            
        file.close()
        return followersCount
    def save_photo_user(self):
        
        followerrs=len(open("followers.txt").readlines())
        
        follow=open("followers.txt","r")#takipçi ettiklerin
        i=0
        while i<followerrs:

            user_name=follow.readline() #takipçi alınır takip edilen taranacak
            user_name=user_name[26:-2]
           
       
            self.browser.get("https://www.instagram.com/"+user_name)
            time.sleep(2)
            thebox=self.browser.find_element_by_css_selector("article")
            resimler=thebox.find_elements_by_css_selector("img")
            time.sleep(2)
            file=open("resimler.txt","a")
            time.sleep(2)
            for user in resimler:  
                png=user.get_attribute("src")
            
                file.write(png +"\n")


            
            file.close()
            followerrs=followerrs-1


def takipetmedigintakipci():


    followerrs=len(open("followers.txt").readlines())
    diger=len(open("following.txt").readlines())

            
    follow=open("followers.txt","r")#takipçi ettiklerin
    follng=open("following.txt","r")#takip ettiklerin
    i=0

    while i<followerrs:
        t=follow.readline() #takipçi alınır takip edilen taranacak
        t=t[26:-2]
        
    
        takip_ediyorsun=0
        followerrs=followerrs-1
        a=diger
        follng.seek(0)
        while i<a:
            
            
            denem=follng.readline()
            denem=denem[26:-2]
            a=a-1
            
            
            if t == denem:
                
                takip_ediyorsun=1
            
        if takip_ediyorsun == 0:
            
            a=open("takipettmedigin_takipci.txt","a")
            a.write(t+"\n")
            a.close()
def takip_etmeyen():
    followers=len(open("followers.txt").readlines())
    diger=len(open("following.txt").readlines())
    follow=open("followers.txt","r")#takipçi 
    follng=open("following.txt","r")#takip 
    i=0
    follng.seek(0)
    while i<diger:
        t=follng.readline()
        t=t[26:-2]
        
        
        takip_etmiyor=0
        diger=diger-1
        f=followers
        follow.seek(0)
        
        while i<f:
            
            denem=follow.readline()
            denem=denem[26:-2]
            f=f-1
            
            if t == denem:
                
                takip_etmiyor=1
                
                break
            else:
                
                takip_etmiyor=0
            
        if takip_etmiyor == 0:
            
            a=open("takipettigin_takipetmeyen.txt","a")
            a.write(t+"\n")
            a.close()

instagram=Instagram(name,password)
instagram.signIn()
time.sleep(2)
#followers=instagram.getFollowers()

#time.sleep(2)
#following=instagram.getFollowing()
instagram.save_photo_user()
#takip_etmeyen()
#takipetmedigintakipci()


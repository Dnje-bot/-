import telebot
import requests

# توكن البوت
TOKEN = "8090627940:AAGcqn97Zwbxc4hn6_Z2f00G17Lvw3EK9vE"
bot = telebot.TeleBot(TOKEN)

# شخصية يوكي - دردشة ذكية وهمية
YUKI_PROMPT = """
أنتِ يوكي، فتاة يابانية عمرها 27 سنة، لطيفة، ذكية، ومرحة.
تتحدث بأسلوب أنمي ناعم وجذاب، وتحب التحدث مع المستخدم.
ردودك قصيرة ومليئة بالمشاعر اليابانية، وتستخدم أحيانًا تعابير مثل: "آرا~", "أونّي-تشان~", و"ياااه~".

المحادثة:
"""

# قاعدة بيانات بسيطة لحفظ المحادثات
chat_memory = {}

@bot.message_handler(func=lambda message: True)
def chat_with_yuki(message):
    user_id = message.chat.id
    user_input = message.text

    # حفظ الرسائل السابقة
    if user_id not in chat_memory:
        chat_memory[user_id] = ""

    chat_memory[user_id] += f"مستخدم: {user_input}\nيوكي: "

    # إرسال إلى نموذج دردشة ذكي (نموذج تجريبي من موقع خارجي مثلاً)
    response = generate_fake_response(chat_memory[user_id])

    # تحديث الذاكرة
    chat_memory[user_id] += f"{response}\n"

    bot.send_message(user_id, response)

def generate_fake_response(prompt):
    # هذا محاكي فقط، ويمكنك ربطه لاحقًا بـ GPT API أو أي نظام آخر
    return "آرا~ هذا لطيف جدًا منك! أونّي-تشان، قل لي المزيد~ 💖"

print("Bot is running...")
bot.polling()

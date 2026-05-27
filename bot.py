from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8637728588:AAHgd9gY91mnILAo51mILzeKuv-5lHThIJw"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mesaj = """
👋 Hoş Geldin

BENSON x RAIJIN RENT botuna hoş geldin.

📌 Komutlar

/hesaplar
/fiyat
/destek
/kurallar
"""

    await update.message.reply_text(mesaj)

# /hesaplar
async def hesaplar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🎮 Hesap 1", url="https://t.me/BENSONxRAIJIN/122")],
        [InlineKeyboardButton("🎮 Hesap 2", url="https://t.me/BENSONxRAIJIN/126")],
        [InlineKeyboardButton("🎮 Hesap 3", url="https://t.me/BENSONxRAIJIN/128")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📦 Mevcut Hesaplar\n\nAşağıdan hesap seç:",
        reply_markup=reply_markup
    )

# /fiyat
async def fiyat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mesaj = """
💰 Fiyat Listesi

🎮 Hesap 1
• 4 Saat → 75 TL
• 24 Saat → 150 TL

🎮 Hesap 2
• 4 Saat → 75 TL
• 24 Saat → 150 TL

🎮 Hesap 3
• 4 Saat → 80 TL
• 24 Saat → 175 TL

💳 Ödeme Bilgileri

IBAN:
TR63 0086 9000 0000 0415 9635 09

Alıcı:
Meryem Kırlar

📩 Ödeme yaptıktan sonra dekont gönderin.
"""

    await update.message.reply_text(mesaj)

# /destek
async def destek(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "📩 Destek için: @kullaniciadin"
    )

# /kurallar
async def kurallar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mesaj = """
📜 BENSON x RAIJIN RENT KURALLARI

Kiralayan herkes kuralları kabul etmiş olur.
Bilmemek muafiyet sağlamayacaktır ❗️

Hesaba herhangi bir zarar gelmesi,
ülke/bölge değişmesi,
kurallara uyulmaması durumunda:

❌ KALICI YASAKLAMA
❌ ÜCRET İADESİ YOK

"Zarar vermek" şunları kapsar:

• Hile kullanımı
• Yazılım kullanımı
• Ülke/bölge değiştirme
• Bayrak değiştirme
• Popülerlik işlemleri
• UC harcama
• Üçüncü taraf uygulamalarla giriş

❌ Materyalleri ve UC'leri harcayamazsınız
❌ Hesaba UC yükleyemezsiniz
❌ Sunucu/bölge değiştirmek yasaktır
❌ Oyun tarafından yasaklanan her türlü işlem yasaktır
❌ Bayrak değiştirmek yasaktır

💸 Takma ad değiştirme bedeli: 300 TL

“Hesabınıza başka bir cihazdan giriş yapıldı”
uyarısı dışında atılırsanız tekrar giriş yapamazsınız.

📱 Cihaz kontrolü sırasında şüpheli uygulama
veya program tespit edilirse ücret iadesi yapılmaz.
"""

    await update.message.reply_text(mesaj)

# Bot sistemi
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hesaplar", hesaplar))
app.add_handler(CommandHandler("fiyat", fiyat))
app.add_handler(CommandHandler("destek", destek))
app.add_handler(CommandHandler("kurallar", kurallar))

print("Bot çalışıyor...")

app.run_polling()

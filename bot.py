from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    LabeledPrice
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    PreCheckoutQueryHandler,
    MessageHandler,
    filters
)

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

        [
            InlineKeyboardButton(
                "🎮 Hesap 1 - 400 ⭐",
                callback_data="hesap1"
            )
        ],

        [
            InlineKeyboardButton(
                "🎮 Hesap 2 - 400 ⭐",
                callback_data="hesap2"
            )
        ],

        [
            InlineKeyboardButton(
                "🎮 Hesap 3 - 450 ⭐",
                callback_data="hesap3"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📦 Mevcut Hesaplar\n\nAşağıdan hesap seç:",
        reply_markup=reply_markup
    )

# Stars ödeme sistemi
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "hesap1":

        prices = [LabeledPrice("Hesap 1", 400)]

        await context.bot.send_invoice(
            chat_id=query.message.chat_id,
            title="🎮 Hesap 1",
            description="24 Saat Kiralama",
            payload="hesap1",
            provider_token="",
            currency="XTR",
            prices=prices
        )

    elif query.data == "hesap2":

        prices = [LabeledPrice("Hesap 2", 400)]

        await context.bot.send_invoice(
            chat_id=query.message.chat_id,
            title="🎮 Hesap 2",
            description="24 Saat Kiralama",
            payload="hesap2",
            provider_token="",
            currency="XTR",
            prices=prices
        )

    elif query.data == "hesap3":

        prices = [LabeledPrice("Hesap 3", 450)]

        await context.bot.send_invoice(
            chat_id=query.message.chat_id,
            title="🎮 Hesap 3",
            description="24 Saat Kiralama",
            payload="hesap3",
            provider_token="",
            currency="XTR",
            prices=prices
        )

# Ödeme kontrolü
async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.pre_checkout_query
    await query.answer(ok=True)

# Başarılı ödeme
async def successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "✅ Ödeme başarılı!\n\n"
        "🎉 Hesabınız aktif edildi.\n"
        "📩 Destek: @bensonhackk"
    )

# /fiyat
async def fiyat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mesaj = """
💰 Fiyat Listesi

🎮 Hesap 1
• 24 Saat → 400 ⭐

🎮 Hesap 2
• 24 Saat → 400 ⭐

🎮 Hesap 3
• 24 Saat → 450 ⭐

📩 Destek:
@bensonhackk
"""

    await update.message.reply_text(mesaj)

# /destek
async def destek(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "📩 Destek için: @bensonhackk"
    )

# /kurallar
async def kurallar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mesaj = """
📜 BENSON x RAIJIN RENT KURALLARI

Kiralayan herkes kuralları kabul etmiş olur.
Bilmemek muafiyet sağlamayacaktır ❗️

❌ Hesaba zarar vermek yasaktır
❌ UC harcamak yasaktır
❌ Bayrak değiştirmek yasaktır
❌ Bölge değiştirmek yasaktır
❌ Üçüncü taraf uygulamalar yasaktır

💸 Takma ad değiştirme bedeli: 300 TL

📩 Destek:
@bensonhackk
"""

    await update.message.reply_text(mesaj)

# Bot sistemi
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hesaplar", hesaplar))
app.add_handler(CommandHandler("fiyat", fiyat))
app.add_handler(CommandHandler("destek", destek))
app.add_handler(CommandHandler("kurallar", kurallar))

app.add_handler(CallbackQueryHandler(button))

app.add_handler(
    PreCheckoutQueryHandler(precheckout_callback)
)

app.add_handler(
    MessageHandler(
        filters.SUCCESSFUL_PAYMENT,
        successful_payment
    )
)

print("Bot çalışıyor...")

app.run_polling()

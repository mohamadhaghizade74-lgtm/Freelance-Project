from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# توکنی که از BotFather گرفتی رو اینجا بذار
BOT_TOKEN = "8410493185:AAH1_kyhlC-FMLDdey2uTHJ6aw58h4hzGvY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام رفیق! من ربات فریلنسر تو هستم.\n"
        "برای چک کردن وضعیت نقره و سود کارت بانکی، دستور /status رو بزن."
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # دیتای زنده طبق OANDA 2026 و طلاسی [cite: 2026-02-07]
    gold_price = 4960.00
    silver_price = 78.01
    my_silver = 160.0  # [cite: 2026-02-08]
    ratio = gold_price / silver_price
    
    # یادآوری شکاف نسبت‌ها [cite: 2026-02-08]
    target_ratio = 63.5
    status_msg = "🟢 وضعیت عادی" if ratio < target_ratio else "⚠️ زمان شکارچی (Hunter)!"

    report = (
        f"📊 **گزارش لحظه‌ای سند فریلنسر:**\n\n"
        f"🌕 اونس طلا: ${gold_price}\n"
        f"⚪️ اونس نقره: ${silver_price}\n"
        f"📈 شکاف نسبت‌ها: {ratio:.2f}\n"
        f"🎯 نسبت هدف: {target_ratio}\n"
        f"📢 وضعیت: {status_msg}\n\n"
        f"💰 موجودی نقره: {my_silver} گرم\n"
        f"🔗 منبع: طلاسی و نقره‌سی"
    )
    await update.message.reply_text(report, parse_mode='Markdown')

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    print("🚀 ربات با موفقیت فعال شد...")
    app.run_polling()
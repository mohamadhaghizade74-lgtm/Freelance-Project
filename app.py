import asyncio
import time
from telegram import Bot

# --- تنظیمات اختصاصی شما ---
TOKEN = '8410493185:AAH1_kyhlC-FMLDdey2uTHJ6aw58h4hzGvY' 
CHAT_ID = 5660050701         
MY_SILVER = 100.0           # [cite: 2026-02-08]
TARGET_RATIO = 63.58        # [cite: 2026-02-08]

# --- 🟢 قیمت‌ها را اینجا ست کن (بدون ارور) ---
LIVE_USD = 88400            
LIVE_GOLD_18K = 5140000     # طلاسی [cite: 2026-02-07]
LIVE_SILVER_OUNCE = 78.01   # OANDA [cite: 2026-02-07]
LIVE_GOLD_OUNCE = 4960.00   # OANDA [cite: 2026-02-07]
# ------------------------------------------

async def send_final_report():
    # محاسبات فنی
    current_ratio = LIVE_GOLD_OUNCE / LIVE_SILVER_OUNCE
    silver_gram_irr = (LIVE_SILVER_OUNCE * LIVE_USD) / 31.1035
    total_value = MY_SILVER * silver_gram_irr

    # --- بازگشت به طراحی شیک و ویترینی مورد علاقه تو ---
    message = (
        f"📊 **گزارش لحظه‌ای سند فریلنسر:**\n"
        f"--------------------------\n"
        f"🇮🇷 **بازار داخلی (طلاسی/دلار):**\n"
        f"💵 دلار روز: {LIVE_USD:,} تومان\n"
        f"🔸 طلای ۱۸ عیار: {LIVE_GOLD_18K:,} تومان\n"
        f"🔘 نقره ۹۹۹ (گرمی): {int(silver_gram_irr):,} تومان\n"
        f"--------------------------\n"
        f"🌍 **بازار جهانی (OANDA):**\n"
        f"🟡 انس طلا: ${LIVE_GOLD_OUNCE:,.2f}\n"
        f"⚪️ انس نقره: ${LIVE_SILVER_OUNCE:,.2f}\n"
        f"--------------------------\n"
        f"💼 **وضعیت سبد دارایی:**\n"
        f"📦 موجودی: {MY_SILVER} گرم نقره [cite: 2026-02-08]\n"
        f"💰 ارزش کل: {int(total_value):,} تومان\n"
        f"--------------------------\n"
        f"📈 **تحلیل شکاف نسبت‌ها:**\n"
        f"🎯 هدف: {TARGET_RATIO} | فعلی: {current_ratio:.2f} [cite: 2026-02-08]\n"
        f"\n📢 وضعیت: ⏳ در انتظار نوسان شکارچی..."
    )

    try:
        bot = Bot(token=TOKEN)
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')
        print("✅ پیام با موفقیت و طراحی درست ارسال شد.")
    except Exception as e:
        print(f"❌ خطا: {e}")

if __name__ == "__main__":
    asyncio.run(send_final_report())
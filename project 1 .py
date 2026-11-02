import random
# تنظیمات بازی
max_A = 5
low = 1
high = 100
again = "y"
# حلقه بازی مجدد
while again == "y":
    secret_number = random.randint(low, high)

    print("\nیک عدد بین 1 تا 100 انتخاب شده است.")
    print("شما 5 فرصت برای حدس زدن دارید.")
    won = False
    # پنج فرصت حدس
    for attempt in range(1, max_A + 1):
        # اعتبارسنجی ورودی
        while True:
            raw = input(
                "\nتلاش " + str(attempt) + " از 5"
                + "\nجان باقی‌مانده: "
                + str(max_A - attempt + 1)
                + "\nحدس شما: "
            )

            if raw.isdigit():
                user_guess = int(raw)
                if user_guess >= low and user_guess <= high:
                    break
                else:
                    print("عدد باید بین 1 تا 100 باشد.")
            else:
                print("ورودی نامعتبر است. لطفاً فقط عدد وارد کنید.")
        # بررسی حدس
        if user_guess == secret_number:
            print("\nتبریک! برنده شدی.")
            # رتبه بندی
            if attempt == 1:
                print("رتبه شما: نمونه‌ای!")
            elif attempt == 2:
                print("رتبه شما: بسیار خوبی!")
            elif attempt == 3:
                print("رتبه شما: خوب!")
            elif attempt == 4:
                print("رتبه شما: قبول!")
            else:
                print("رتبه شما: با شانس بردی!")
            won = True
            break

        else:
            # محاسبه اختلاف و جهت حدس
            if user_guess > secret_number:
                diff = user_guess - secret_number
                direction = "عدد کوچک‌تری وارد کن."
            else:
                diff = secret_number - user_guess
                direction = "عدد بزرگ‌تری وارد کن."
            # راهنمای نزدیک و دور
            if diff <= 5:
                level = "خیلی نزدیکی!"
            elif diff <= 15:
                level = "نزدیکی، ولی هنوز فاصله داری!"
            else:
                level = "خیلی دوری!"
            print(level, direction)

    # بررسی باخت
    if won == False:
        print("\nمتأسفانه باختی!")
        print("عدد مخفی:", secret_number)

    # پرسیدن برای بازی مجدد
    while True:
        play_again = input("\nبازی مجدد؟ (y/n): ")

        if play_again == "y" or play_again == "n":
            break
        else:
            print("لطفاً فقط y یا n وارد کن.")

print("ممنون از بازی شما. خداحافظ!")

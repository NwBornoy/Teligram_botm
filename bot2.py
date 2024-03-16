import telebot,re
from telebot import types
import requests
from googletrans import Translator
translator = Translator()

TOKEN = "token"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
  try:
    user = message.from_user.first_name
    javob = f"Assalom alaykum, Xush kelibsiz! {user}😉"
    bot.send_message(chat_id = message.from_user.id, text=javob, reply_markup = keybort2)
  except:
      bot.send_message(chat_id = message.from_user.id, text="Tizimda xatolik chiqdi kiyinroq urinib ko'ring!")
      

@bot.message_handler(commands=['music'])
def send_welcome_music(message):
    try:
        user = message.from_user.first_name
        javob = f" Uzur {user} bu bo'lim hali ishlagani yuq❌"
        bot.send_message(chat_id = message.from_user.id, text=javob, reply_markup = keybort2)
    except:
        bot.send_message(chat_id = message.from_user.id, text="Tizimda xatolik chiqdi kiyinroq urinib ko'ring!")

@bot.message_handler(commands=['about'])
def send_welcome_about(message):
    try:
        user = message.from_user.first_name
        javob = f"Assalom alaykum, bu botni ko'p pag'onali yani ko'proq ish qilishi uchun harakat qilindi \n buning qo'lidan hozircha faqat 4 ta vazifani bajara oladi.\n1. Hamma viloyatlarning 5 kunlik obhavo sini ko'rsatadi\n2. Hamma viloyatlarning ro'za tqvimini  va duolarni ko'rish mumkun\n3. Bu bot tarjimonlik qiladi yani har qanday so'zni 4ta tilda tarjima qila oladi\n4. Bu asosiy 3 ta ilovadagi videolarni topib bera oladi bular, Instagram, Tiktok va Youtube\n biz hali bunga yana fo'nksia qo'shmoqchimiz shuning ustida ishlamoqdamiz\nSiz {user} qolgan funksialardan bemalol foydalanishingiz mumkun😉"
        bot.send_message(chat_id = message.from_user.id, text=javob, reply_markup = keybort2)
    except:
        bot.send_message(chat_id = message.from_user.id, text="Tizimda xatolik chiqdi kiyinroq urinib ko'ring!")
@bot.message_handler(commands=['help'])
def send_welcome(message):
    try:
        javob = "Siz /menu orqali bo'limlarimiz haqida.\n/obhavo orqali obhavolarni ko'rishingiz mumkun.\n/ramazont orqali esa ramazon taqvimlarni ko'rishingiz mumkun.\n/tarjimon orqali xohlagan textni tarjima qila olasiz.\n /video orqali 3 ta ilovadagi videolar linkini tashlab videoni topishingiz va videolarni yuklab olishingoz mumkun.\n/music bu bolimimiz hali ishga tushgani yuq buni ustida ishlayabmiz.\n/about bu esa bot haqida malumot beradi."
        bot.reply_to(message, javob)
    except:
        bot.send_message(chat_id = message.from_user.id, text="Tizimda xatolik chiqdi kiyinroq urinib ko'ring!")
	
@bot.message_handler(commands=['video'])
def send_welcome_video(message):
    try:
        id = message.from_user.id
        markup2 = types.InlineKeyboardMarkup()
        markup2.row_width = 2

        instagram = types.InlineKeyboardButton(text="Instagram🎬",switch_inline_query ="instagrami", callback_data="ins")
        tiktok = types.InlineKeyboardButton(text="Tiktok🎬", callback_data="tik")
        youtube = types.InlineKeyboardButton(text="You Tube🎬", callback_data="yut")
        orqaga = types.InlineKeyboardButton(text="orqaga", callback_data="orqaga")

        markup2.add(instagram, tiktok,youtube,orqaga)
        bot.send_message(id,"Sizga qaysi ilovadagi video kerak?📱\n🚨Video hajmi 15MB dan oshmaslik kerak!", reply_markup=markup2)
    except:
        bot.send_message(chat_id = message.from_user.id, text="Tizimda xatolik chiqdi kiyinroq urinib ko'ring!")
batton1 = types.KeyboardButton("bu kantak", request_contact=True)
batton2 = types.KeyboardButton("bu lakatsia", request_location=True)
keybort = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(batton1,batton2)

batton3 = types.InlineKeyboardButton(text="Menu", callback_data="menu" )
batton4 = types.InlineKeyboardButton(text="About", callback_data="about")
keybort2 = types.InlineKeyboardMarkup().add(batton3, batton4)

# obhavo uchun
batton5 = types.InlineKeyboardButton(text="Hozirgi vaqt va\n kun davomidagi ob havo", callback_data="hozirgi_kun_q" )
batton6 = types.InlineKeyboardButton(text="Uch kunlik \nobhavo", callback_data="uch_kunlik_q")
batton7 = types.InlineKeyboardButton(text="Uch kunlikni kun\n davomidagi obhavo", callback_data="uch_kun_davomi_q")
keybort_qa = types.InlineKeyboardMarkup().add(batton5, batton6, batton7)

batton8 = types.InlineKeyboardButton(text="Hozirgi vaqt va kun davomidagi ob havo", callback_data="hozirgi_kun_s" )
batton9 = types.InlineKeyboardButton(text="Uch kunlik obhavo", callback_data="uch_kunlik_s")
batton10 = types.InlineKeyboardButton(text="Uch kunlikni kun davomidagi obhavo", callback_data="uch_kun_davomi_s")
keybort_su = types.InlineKeyboardMarkup().add(batton8, batton9, batton10)

batton11 = types.InlineKeyboardButton(text="Hozirgi vaqt va kun davomidagi ob havo", callback_data="hozirgi_kun_x" )
batton12 = types.InlineKeyboardButton(text="Uch kunlik obhavo", callback_data="uch_kunlik_x")
batton13 = types.InlineKeyboardButton(text="Uch kunlikni kun davomidagi obhavo", callback_data="uch_kun_davomi_x")
keybort_xo = types.InlineKeyboardMarkup().add(batton11, batton12, batton13)

batton14 = types.InlineKeyboardButton(text="Hozirgi vaqt va kun davomidagi ob havo", callback_data="hozirgi_kun_qor" )
batton15 = types.InlineKeyboardButton(text="Uch kunlik obhavo", callback_data="uch_kunlik_qor")
batton16 = types.InlineKeyboardButton(text="Uch kunlikni kun davomidagi obhavo", callback_data="uch_kun_davomi_qor")
keybort_qor = types.InlineKeyboardMarkup().add(batton14, batton15, batton16)

batton17 = types.InlineKeyboardButton(text="Hozirgi vaqt va kun davomidagi ob havo", callback_data="hozirgi_kun_na" )
batton18 = types.InlineKeyboardButton(text="Uch kunlik obhavo", callback_data="uch_kunlik_na")
batton19 = types.InlineKeyboardButton(text="Uch kunlikni kun davomidagi obhavo", callback_data="uch_kun_davomi_na")
keybort_na = types.InlineKeyboardMarkup().add(batton17, batton18, batton19)

batton20 = types.InlineKeyboardButton(text="Hozirgi vaqt va kun davomidagi ob havo", callback_data="hozirgi_kun_bu" )
batton21 = types.InlineKeyboardButton(text="Uch kunlik obhavo", callback_data="uch_kunlik_bu")
batton22 = types.InlineKeyboardButton(text="Uch kunlikni kun davomidagi obhavo", callback_data="uch_kun_davomi_bu")
keybort_bu = types.InlineKeyboardMarkup().add(batton20, batton21, batton22)

batton23 = types.InlineKeyboardButton(text="Hozirgi vaqt va kun davomidagi ob havo", callback_data="hozirgi_kun_sa" )
batton24= types.InlineKeyboardButton(text="Uch kunlik obhavo", callback_data="uch_kunlik_sa")
batton25 = types.InlineKeyboardButton(text="Uch kunlikni kun davomidagi obhavo", callback_data="uch_kun_davomi_sa")
keybort_sa = types.InlineKeyboardMarkup().add(batton23, batton24, batton25)

batton26 = types.InlineKeyboardButton(text="Hozirgi vaqt va kun davomidagi ob havo", callback_data="hozirgi_kun_ji" )
batton27 = types.InlineKeyboardButton(text="Uch kunlik obhavo", callback_data="uch_kunlik_ji")
batton28 = types.InlineKeyboardButton(text="Uch kunlikni kun davomidagi obhavo", callback_data="uch_kun_davomi_ji")
keybort_ji = types.InlineKeyboardMarkup().add(batton26, batton27, batton28)

batton29 = types.InlineKeyboardButton(text="Hozirgi vaqt va kun davomidagi ob havo", callback_data="hozirgi_kun_sir" )
batton30 = types.InlineKeyboardButton(text="Uch kunlik obhavo", callback_data="uch_kunlik_sir")
batton31 = types.InlineKeyboardButton(text="Uch kunlikni kun davomidagi obhavo", callback_data="uch_kun_davomi_sir")
keybort_sir = types.InlineKeyboardMarkup().add(batton29, batton30, batton31)

batton32 = types.InlineKeyboardButton(text="Hozirgi vaqt va kun davomidagi ob havo", callback_data="hozirgi_kun_to" )
batton33 = types.InlineKeyboardButton(text="Uch kunlik obhavo", callback_data="uch_kunlik_to")
batton34 = types.InlineKeyboardButton(text="Uch kunlikni kun davomidagi obhavo", callback_data="uch_kun_davomi_to")
keybort_to = types.InlineKeyboardMarkup().add(batton32, batton33, batton34)

batton35 = types.InlineKeyboardButton(text="Hozirgi vaqt va kun davomidagi ob havo", callback_data="hozirgi_kun_an" )
batton36 = types.InlineKeyboardButton(text="Uch kunlik obhavo", callback_data="uch_kunlik_an")
batton37 = types.InlineKeyboardButton(text="Uch kunlikni kun davomidagi obhavo", callback_data="uch_kun_davomi_an")
keybort_an = types.InlineKeyboardMarkup().add(batton35, batton36, batton37)

batton38 = types.InlineKeyboardButton(text="Hozirgi vaqt va kun davomidagi ob havo", callback_data="hozirgi_kun_fa" )
batton39 = types.InlineKeyboardButton(text="Uch kunlik obhavo", callback_data="uch_kunlik_fa")
batton40 = types.InlineKeyboardButton(text="Uch kunlikni kun davomidagi obhavo", callback_data="uch_kun_davomi_fa")
keybort_fa = types.InlineKeyboardMarkup().add(batton38, batton39, batton40)

batton41 = types.InlineKeyboardButton(text="Hozirgi vaqt va kun davomidagi ob havo", callback_data="hozirgi_kun_nam" )
batton42 = types.InlineKeyboardButton(text="Uch kunlik obhavo", callback_data="uch_kunlik_nam")
batton43 = types.InlineKeyboardButton(text="Uch kunlikni kun davomidagi obhavo", callback_data="uch_kun_davomi_nam")
keybort_nam = types.InlineKeyboardMarkup().add(batton41, batton42, batton43)






@bot.message_handler(commands=['menu'])
def send_welcome_menu(message):
    try:
        id = message.from_user.id
        
        murkup = types.InlineKeyboardMarkup(row_width=2)

        ob_havo = types.InlineKeyboardButton("Ob-havo🌄", callback_data="answer_ob_havo")
        ramazon_kalindar = types.InlineKeyboardButton("Ramazon kalendar📆", callback_data="answer_ramazon_kalindar")
        tarjimon = types.InlineKeyboardButton("Tarjimon📖", callback_data="answer_tarjimon")
        musiqa_topish = types.InlineKeyboardButton("Musiqani topish🎜", callback_data="answer_musiqa_topish")
        video_topish = types.InlineKeyboardButton("Video topish🎥", callback_data="answer_video_topish")

        murkup.add(ob_havo, ramazon_kalindar, tarjimon, musiqa_topish, video_topish)
        bot.send_message(id,"Kerakli bo'limni tanlang.", reply_markup=murkup)
    except:
        bot.send_message(chat_id = message.from_user.id, text="Tizimda xatolik chiqdi kiyinroq urinib ko'ring!")
@bot.message_handler(commands=['tarjimon'])
def send_welcome(message):
    try:
        id = message.from_user.id
        
        murkup = types.InlineKeyboardMarkup(row_width=2)

        uz_rus = types.InlineKeyboardButton("Uzb🇺🇿 - Rus🇷🇺", callback_data="uzb_rus")
        rus_uz = types.InlineKeyboardButton("Rus🇷🇺 - Uzb🇺🇿", callback_data="rus_uz")
        uz_eng = types.InlineKeyboardButton("Uzb🇺🇿 - Eng🇺🇸", callback_data="uz_eng")
        eng_uz = types.InlineKeyboardButton("Eng🇺🇸 - Uzb🇺🇿", callback_data="eng_uz")
        uz_arb = types.InlineKeyboardButton("Uzb🇺🇿 - Arb🇸🇦", callback_data="uz_arb")
        arb_uz = types.InlineKeyboardButton("Arb🇸🇦 - Uzb🇺🇿", callback_data="arb_uz")
        orqaga = types.InlineKeyboardButton(text="orqaga", callback_data="orqaga")

        murkup.add(uz_rus, rus_uz, uz_eng,eng_uz, uz_arb,arb_uz ,orqaga)
        bot.send_message(id,"Siz hoxlagan tildagi so'zlarni\n<'Uzb','Rus','Eng','Arb'> tiliga o'giradi\nFoydalanish uchun /help bosing!🌐", reply_markup=murkup)
        bot.send_message(id,"uz> text -O'zbek tiliga tarjima qilish uchun!\nru> text -Rus tiliga tarjima qilish uchun!\nen> text -Ingilz tiliga tarjima qilish uchun!\nar> text -Arab tiliga tarjima qilish uchun!\nMisol: uz>Hello, Natija: Salom\nAniq to'g'ri bo'lmasligi mumkun.\nKamchiliklar uchun uzur!")
    except:
        bot.send_message(chat_id = message.from_user.id, text="Tizimda xatolik chiqdi kiyinroq urinib ko'ring!")
@bot.message_handler(commands=["obhavo"])
def battom(message):
    try:
        markup2 = types.InlineKeyboardMarkup()
        markup2.row_width = 3

        qashqadaryo = types.InlineKeyboardButton(text="Qashqadaryo", callback_data="test1")
        surxandaryo = types.InlineKeyboardButton(text="Surxondaryo", callback_data="test2")
        xorazim = types.InlineKeyboardButton(text="Xorazim", callback_data="test3")
        qoraqalpoq = types.InlineKeyboardButton(text="Qoraqalpog'iston", callback_data="test4")
        navoiy = types.InlineKeyboardButton(text="Navoiy",callback_data="test5")
        buxoro = types.InlineKeyboardButton(text="Buxoro",callback_data="test6")
        samarqand = types.InlineKeyboardButton(text="Samarqand", callback_data="test7")
        jizzax = types.InlineKeyboardButton(text="Jizzax", callback_data="test8")
        sirdaryo = types.InlineKeyboardButton(text="Sirdaryo", callback_data="test9")
        toshkent = types.InlineKeyboardButton(text="Toshkent", callback_data="test10")
        andijon = types.InlineKeyboardButton(text="Andijon", callback_data="test11")
        fargona = types.InlineKeyboardButton(text="Farg'ona", callback_data="test12")
        namangan = types.InlineKeyboardButton(text="Namangan", callback_data="test13")
        orqaga = types.InlineKeyboardButton(text="orqaga", callback_data="orqaga")
        
        markup2.add(qashqadaryo, surxandaryo, xorazim, qoraqalpoq,navoiy,buxoro,samarqand,jizzax,sirdaryo, toshkent,andijon,fargona,namangan,orqaga)
        bot.send_message(message.from_user.id, "Viloyatlarimiz!", reply_markup=markup2)
    except:
        bot.send_message(chat_id = message.from_user.id, text="Tizimda xatolik chiqdi kiyinroq urinib ko'ring!")
@bot.message_handler(commands=["ramazont"])
def battom_taqvim(message):
  
    try:
        markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True,selective=True)
        markup2.row_width = 3

        qashqadaryo = types.InlineKeyboardButton(text="Qashadaryo_taqvimi🗓", callback_data="test1")
        surxandaryo = types.InlineKeyboardButton(text="Surxondaryo_taqvimi🗓", callback_data="test2")
        xorazim = types.InlineKeyboardButton(text="Xorazim_taqvimi🗓", callback_data="test3")
        qoraqalpoq = types.InlineKeyboardButton(text="Qoraqalpog'iston_taqvimi🗓", callback_data="test4")
        navoiy = types.InlineKeyboardButton(text="Navoiy_taqvimi🗓",callback_data="test5")
        buxoro = types.InlineKeyboardButton(text="Buxoro_taqvimi🗓",callback_data="test6")
        samarqand = types.InlineKeyboardButton(text="Samarqand_taqvimi🗓", callback_data="test7")
        jizzax = types.InlineKeyboardButton(text="Jizzax_taqvimi🗓", callback_data="test8")
        sirdaryo = types.InlineKeyboardButton(text="Sirdaryo_taqvimi🗓", callback_data="test9")
        toshkent = types.InlineKeyboardButton(text="Toshkent_taqvimi🗓", callback_data="test10")
        andijon = types.InlineKeyboardButton(text="Andijon_taqvimi🗓", callback_data="test11")
        fargona = types.InlineKeyboardButton(text="Farg'ona_taqvimi🗓", callback_data="test12")
        namangan = types.InlineKeyboardButton(text="Namangan_taqvimi🗓", callback_data="test13")
        markup2.add(qashqadaryo, surxandaryo, xorazim, qoraqalpoq,navoiy,buxoro,samarqand,jizzax,sirdaryo, toshkent,andijon,fargona,namangan)
        bot.send_message(message.from_user.id, "Viloyatlar taqvimlari!", reply_markup=markup2)
    except:
        bot.send_message(chat_id = message.from_user.id, text="Tizimda xatolik chiqdi kiyinroq urinib ko'ring!")
def download(urli):
    try:
        if "https://instagram.com" in urli or "https://www.instagram.com" in urli:
            url = "https://social-media-video-downloader.p.rapidapi.com/smvd/get/all"

            querystring = {"url":urli,"filename":"Test video"}

            headers = {
                "X-RapidAPI-Key": "8a22ef3d9fmsh270fd82095a906fp1f8bc7jsn3c01f1038443",
                "X-RapidAPI-Host": "social-media-video-downloader.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            try:
                link = response.json()
                fotos = link["picture"]
                videos = link["links"][0]["link"]
                return fotos, videos
            except:
                return None   
        elif "https://tiktok.com" in urli or "https://www.tiktok.com" in urli:
            url = "https://tiktok89.p.rapidapi.com/tiktok"

            querystring = {"link":urli}

            headers = {
                "X-RapidAPI-Key": "8a22ef3d9fmsh270fd82095a906fp1f8bc7jsn3c01f1038443",
                "X-RapidAPI-Host": "tiktok89.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)

            kar = response.json()
            video = kar["video"]["download_addr"]["url_list"][1]
            name = kar["author"]["nickname"]
            comnt = kar["desc"]
            segnatur = kar["author"]["signature"]
            return video, name, comnt, segnatur
            
    except:
        return "Uzur tizimda xatolik chiqdi😱"
# def downloads(url, name = "video.mp4"):
#      r = requests.get(url, stream=True)
#      with open(name, "wb") as f:
#           for chunk in r.iter_content(chunk_size=1024):
#                if chunk:
#                     f.write(chunk)
def hozir(loc):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q":loc,"days":"3"}

    headers = {
        "X-RapidAPI-Key": "8a22ef3d9fmsh270fd82095a906fp1f8bc7jsn3c01f1038443",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    jsone = response.json()

   
    viloyat = jsone["location"]["region"]
    davlat = jsone["location"]["country"]

    hozrgi_obhavo = jsone["current"]["temp_c"]
    hozrgi_vaqt = jsone["current"]["last_updated"]
    hozirgi_obhavo_icon = jsone["current"]["condition"]["icon"]

    bugun_kun_sana_0 = jsone["forecast"]["forecastday"][0]["hour"][0]["time"]
    bugun_kun_harorat_0h = jsone["forecast"]["forecastday"][0]["hour"][0]["temp_c"]
    bugun_kun_icon_0h = jsone["forecast"]["forecastday"][0]["hour"][0]["condition"]["icon"]

    bugun_kun_sana_3 = jsone["forecast"]["forecastday"][0]["hour"][3]["time"]
    bugun_kun_harorat_3h = jsone["forecast"]["forecastday"][0]["hour"][3]["temp_c"]
    bugun_kun_icon_3h = jsone["forecast"]["forecastday"][0]["hour"][3]["condition"]["icon"]

    bugun_kun_sana_6 = jsone["forecast"]["forecastday"][0]["hour"][6]["time"]
    bugun_kun_harorat_6h = jsone["forecast"]["forecastday"][0]["hour"][6]["temp_c"]
    bugun_kun_icon_6h = jsone["forecast"]["forecastday"][0]["hour"][6]["condition"]["icon"]

    bugun_kun_sana_9 = jsone["forecast"]["forecastday"][0]["hour"][9]["time"]
    bugun_kun_harorat_9h = jsone["forecast"]["forecastday"][0]["hour"][9]["temp_c"]
    bugun_kun_icon_9h = jsone["forecast"]["forecastday"][0]["hour"][9]["condition"]["icon"]

    bugun_kun_sana_13 = jsone["forecast"]["forecastday"][0]["hour"][13]["time"]
    bugun_kun_harorat_13h = jsone["forecast"]["forecastday"][0]["hour"][13]["temp_c"]
    bugun_kun_icon_13h = jsone["forecast"]["forecastday"][0]["hour"][13]["condition"]["icon"]


    bugun_kun_sana_17 = jsone["forecast"]["forecastday"][0]["hour"][17]["time"]
    bugun_kun_harorat_17h = jsone["forecast"]["forecastday"][0]["hour"][17]["temp_c"]
    bugun_kun_icon_17h = jsone["forecast"]["forecastday"][0]["hour"][17]["condition"]["icon"]

    bugun_kun_sana_20 = jsone["forecast"]["forecastday"][0]["hour"][20]["time"]
    bugun_kun_harorat_20h = jsone["forecast"]["forecastday"][0]["hour"][20]["temp_c"]
    bugun_kun_icon_20h = jsone["forecast"]["forecastday"][0]["hour"][20]["condition"]["icon"]

    bugun_kun_sana_23 = jsone["forecast"]["forecastday"][0]["hour"][23]["time"]
    bugun_kun_harorat_23h = jsone["forecast"]["forecastday"][0]["hour"][23]["temp_c"]
    bugun_kun_icon_23h = jsone["forecast"]["forecastday"][0]["hour"][23]["condition"]["icon"]
    kun_buy_icon = jsone["forecast"]["forecastday"][0]["day"]["condition"]["icon"] 

    return [davlat,viloyat,hozrgi_obhavo,hozrgi_vaqt,hozirgi_obhavo_icon,bugun_kun_sana_0,bugun_kun_harorat_0h,
            bugun_kun_icon_0h, bugun_kun_sana_3,bugun_kun_harorat_3h,bugun_kun_icon_3h, bugun_kun_sana_6,bugun_kun_harorat_6h,bugun_kun_icon_6h,
            bugun_kun_sana_9,bugun_kun_harorat_9h,bugun_kun_icon_9h,bugun_kun_sana_13,bugun_kun_harorat_13h,bugun_kun_icon_13h,bugun_kun_sana_17,bugun_kun_harorat_17h,bugun_kun_icon_17h,
            bugun_kun_sana_20,bugun_kun_harorat_20h,bugun_kun_icon_20h,bugun_kun_sana_23,bugun_kun_harorat_23h,bugun_kun_icon_23h,kun_buy_icon]


def kunlar(loc):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q":loc,"days":"3"}

    headers = {
        "X-RapidAPI-Key": "8a22ef3d9fmsh270fd82095a906fp1f8bc7jsn3c01f1038443",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    jsone = response.json()
    bugun_kun_sana = jsone["forecast"]["forecastday"][0]["date"]
    kun_buy_max = jsone["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
    kun_buy_min = jsone["forecast"]["forecastday"][0]["day"]["mintemp_c"]
    kun_buy_icon = jsone["forecast"]["forecastday"][0]["day"]["condition"]["icon"]

    erta_kun_sana = jsone["forecast"]["forecastday"][1]["date"]
    erta_buy_max = jsone["forecast"]["forecastday"][1]["day"]["maxtemp_c"]
    erta_buy_min = jsone["forecast"]["forecastday"][1]["day"]["mintemp_c"]
    erta_buy_icon = jsone["forecast"]["forecastday"][1]["day"]["condition"]["icon"]

    inde_kun_sana = jsone["forecast"]["forecastday"][2]["date"]
    inde_buy_max = jsone["forecast"]["forecastday"][2]["day"]["maxtemp_c"]
    inde_buy_min = jsone["forecast"]["forecastday"][2]["day"]["mintemp_c"]
    inde_buy_icon = jsone["forecast"]["forecastday"][2]["day"]["condition"]["icon"]
    viloyat = jsone["location"]["region"]
    davlat = jsone["location"]["country"]

    return [bugun_kun_sana,kun_buy_max,kun_buy_min, kun_buy_icon,erta_kun_sana,erta_buy_max,erta_buy_min,erta_buy_icon,
            inde_kun_sana,inde_buy_max,inde_buy_min,inde_buy_icon, viloyat,davlat]

def kunlar_davomi(loc):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q":loc,"days":"3"}

    headers = {
        "X-RapidAPI-Key": "8a22ef3d9fmsh270fd82095a906fp1f8bc7jsn3c01f1038443",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    jsone = response.json()

   
    viloyat = jsone["location"]["region"]
    davlat = jsone["location"]["country"]



    bugun_kun_sana_0 = jsone["forecast"]["forecastday"][0]["hour"][0]["time"]
    bugun_kun_harorat_0h = jsone["forecast"]["forecastday"][0]["hour"][0]["temp_c"]

    bugun_kun_sana_3 = jsone["forecast"]["forecastday"][0]["hour"][3]["time"]
    bugun_kun_harorat_3h = jsone["forecast"]["forecastday"][0]["hour"][3]["temp_c"]

    bugun_kun_sana_6 = jsone["forecast"]["forecastday"][0]["hour"][6]["time"]
    bugun_kun_harorat_6h = jsone["forecast"]["forecastday"][0]["hour"][6]["temp_c"]

    bugun_kun_sana_9 = jsone["forecast"]["forecastday"][0]["hour"][9]["time"]
    bugun_kun_harorat_9h = jsone["forecast"]["forecastday"][0]["hour"][9]["temp_c"]


    bugun_kun_sana_13 = jsone["forecast"]["forecastday"][0]["hour"][13]["time"]
    bugun_kun_harorat_13h = jsone["forecast"]["forecastday"][0]["hour"][13]["temp_c"]



    bugun_kun_sana_17 = jsone["forecast"]["forecastday"][0]["hour"][17]["time"]
    bugun_kun_harorat_17h = jsone["forecast"]["forecastday"][0]["hour"][17]["temp_c"]


    bugun_kun_sana_20 = jsone["forecast"]["forecastday"][0]["hour"][20]["time"]
    bugun_kun_harorat_20h = jsone["forecast"]["forecastday"][0]["hour"][20]["temp_c"]
 

    bugun_kun_sana_23 = jsone["forecast"]["forecastday"][0]["hour"][23]["time"]
    bugun_kun_harorat_23h = jsone["forecast"]["forecastday"][0]["hour"][23]["temp_c"]
    kun_buy_icon = jsone["forecast"]["forecastday"][0]["day"]["condition"]["icon"] 

# erta
    erta_kun_sana_0 = jsone["forecast"]["forecastday"][1]["hour"][0]["time"]
    erta_kun_harorat_0h = jsone["forecast"]["forecastday"][1]["hour"][0]["temp_c"]




    erta_kun_sana_3 = jsone["forecast"]["forecastday"][1]["hour"][3]["time"]
    erta_kun_harorat_3h = jsone["forecast"]["forecastday"][1]["hour"][3]["temp_c"]


    erta_kun_sana_6 = jsone["forecast"]["forecastday"][1]["hour"][6]["time"]
    erta_kun_harorat_6h = jsone["forecast"]["forecastday"][0]["hour"][6]["temp_c"]


    erta_kun_sana_9 = jsone["forecast"]["forecastday"][1]["hour"][9]["time"]
    erta_kun_harorat_9h = jsone["forecast"]["forecastday"][1]["hour"][9]["temp_c"]


    erta_kun_sana_13 = jsone["forecast"]["forecastday"][1]["hour"][13]["time"]
    erta_kun_harorat_13h = jsone["forecast"]["forecastday"][1]["hour"][13]["temp_c"]



    erta_kun_sana_17 = jsone["forecast"]["forecastday"][1]["hour"][17]["time"]
    erta_kun_harorat_17h = jsone["forecast"]["forecastday"][1]["hour"][17]["temp_c"]


    erta_kun_sana_20 = jsone["forecast"]["forecastday"][1]["hour"][20]["time"]
    erta_kun_harorat_20h = jsone["forecast"]["forecastday"][1]["hour"][20]["temp_c"]


    erta_kun_sana_23 = jsone["forecast"]["forecastday"][1]["hour"][23]["time"]
    erta_kun_harorat_23h = jsone["forecast"]["forecastday"][1]["hour"][23]["temp_c"]
    erta_buy_icon = jsone["forecast"]["forecastday"][1]["day"]["condition"]["icon"] 

# kiyin


    kiyin_kun_sana_0 = jsone["forecast"]["forecastday"][0]["hour"][0]["time"]
    kiyin_kun_harorat_0h = jsone["forecast"]["forecastday"][0]["hour"][0]["temp_c"]

    kiyin_kun_sana_3 = jsone["forecast"]["forecastday"][0]["hour"][3]["time"]
    kiyin_kun_harorat_3h = jsone["forecast"]["forecastday"][0]["hour"][3]["temp_c"]

    kiyin_kun_sana_6 = jsone["forecast"]["forecastday"][0]["hour"][6]["time"]
    kiyin_kun_harorat_6h = jsone["forecast"]["forecastday"][0]["hour"][6]["temp_c"]

    kiyin_kun_sana_9 = jsone["forecast"]["forecastday"][0]["hour"][9]["time"]
    kiyin_kun_harorat_9h = jsone["forecast"]["forecastday"][0]["hour"][9]["temp_c"]

    kiyin_kun_sana_13 = jsone["forecast"]["forecastday"][0]["hour"][13]["time"]
    kiyin_kun_harorat_13h = jsone["forecast"]["forecastday"][0]["hour"][13]["temp_c"]


    kiyin_kun_sana_17 = jsone["forecast"]["forecastday"][0]["hour"][17]["time"]
    kiyin_kun_harorat_17h = jsone["forecast"]["forecastday"][0]["hour"][17]["temp_c"]

    kiyin_kun_sana_20 = jsone["forecast"]["forecastday"][0]["hour"][20]["time"]
    kiyin_kun_harorat_20h = jsone["forecast"]["forecastday"][0]["hour"][20]["temp_c"]

    kiyin_kun_sana_23 = jsone["forecast"]["forecastday"][0]["hour"][23]["time"]
    kiyin_kun_harorat_23h = jsone["forecast"]["forecastday"][0]["hour"][23]["temp_c"]
    kiyin_buy_icon = jsone["forecast"]["forecastday"][0]["day"]["condition"]["icon"]  

    return [davlat,viloyat,bugun_kun_sana_0,bugun_kun_harorat_0h,
             bugun_kun_sana_3,bugun_kun_harorat_3h, bugun_kun_sana_6,bugun_kun_harorat_6h,
            bugun_kun_sana_9,bugun_kun_harorat_9h,bugun_kun_sana_13,bugun_kun_harorat_13h,bugun_kun_sana_17,bugun_kun_harorat_17h,
            bugun_kun_sana_20,bugun_kun_harorat_20h,bugun_kun_sana_23,bugun_kun_harorat_23h,kun_buy_icon,

            erta_kun_sana_0,erta_kun_harorat_0h,erta_kun_sana_3,erta_kun_harorat_3h, erta_kun_sana_6,erta_kun_harorat_6h,
            erta_kun_sana_9,erta_kun_harorat_9h,erta_kun_sana_13,erta_kun_harorat_13h,erta_kun_sana_17,erta_kun_harorat_17h,
            erta_kun_sana_20,erta_kun_harorat_20h,erta_kun_sana_23,erta_kun_harorat_23h,erta_buy_icon,
            
            kiyin_kun_sana_0,kiyin_kun_harorat_0h,kiyin_kun_sana_3,kiyin_kun_harorat_3h, kiyin_kun_sana_6,kiyin_kun_harorat_6h,
            kiyin_kun_sana_9,kiyin_kun_harorat_9h,kiyin_kun_sana_13,kiyin_kun_harorat_13h,kiyin_kun_sana_17,kiyin_kun_harorat_17h,
            kiyin_kun_sana_20,kiyin_kun_harorat_20h,kiyin_kun_sana_23,kiyin_kun_harorat_23h,kiyin_buy_icon]



def taqvim():
    try:
        markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True,selective=True)
        markup2.row_width = 2

        saharlik_duosi = types.InlineKeyboardButton(text="Saharlik_duosi🌅", callback_data="test2")
        iftorlik_duosi = types.InlineKeyboardButton(text="Iftorlik_duosi🌄", callback_data="test3")
        return markup2.add(saharlik_duosi,iftorlik_duosi)
    except:
        return "Tizimda xato chiqdi!"

@bot.callback_query_handler(func=lambda call : True)
def answer(callback):
    try:
        if callback.message:

            if callback.data == "hozirgi_kun_q":
                iqlim = hozir("38.7685564,64.6887304")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Viloyat: {iqlim[1]}\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_q":
                kundalik = kunlar("38.7685564,64.6887304")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: {kundalik[12]}\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_q":
                kun_davomi = kunlar_davomi("38.7685564,64.6887304")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: {kun_davomi[1]}da 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")



            if callback.data == "hozirgi_kun_s":
                iqlim = hozir("37.2470911,67.2325474")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Viloyat: {iqlim[1]}\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_s":
                kundalik = kunlar("37.2470911,67.2325474")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: {kundalik[12]}\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_s":
                kun_davomi = kunlar_davomi("37.2470911,67.2325474")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: {kun_davomi[1]}da 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")


            if callback.data == "hozirgi_kun_x":
                iqlim = hozir("41.5524802,60.5406723")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Viloyat: {iqlim[1]}\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_x":
                kundalik = kunlar("41.5524802,60.5406723")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: {kundalik[12]}\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_x":
                kun_davomi = kunlar_davomi("41.5524802,60.5406723")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: {kun_davomi[1]}da 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")


            if callback.data == "hozirgi_kun_qor":
                iqlim = hozir("43.2655861,56.5446695")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Respublika: {iqlim[1]}\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_qor":
                kundalik = kunlar("43.2655861,56.5446695")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: {kundalik[12]}\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_qor":
                kun_davomi = kunlar_davomi("43.2655861,56.5446695")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: {kun_davomi[1]}da 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")


            if callback.data == "hozirgi_kun_na":
                iqlim = hozir("40.5646517,65.6800887")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Viloyat: {iqlim[1]}\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_na":
                kundalik = kunlar("40.5646517,65.6800887")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: {kundalik[12]}\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_na":
                kun_davomi = kunlar_davomi("40.5646517,65.6800887")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: {kun_davomi[1]}da 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")


            if callback.data == "hozirgi_kun_bu":
                iqlim = hozir("39.7776391,64.3403967")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Viloyat: {iqlim[1]}\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_bu":
                kundalik = kunlar("39.7776391,64.3403967")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: {kundalik[12]}\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_bu":
                kun_davomi = kunlar_davomi("39.7776391,64.3403967")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: {kun_davomi[1]}da 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")


            if callback.data == "hozirgi_kun_sa":
                iqlim = hozir("39.6408363,66.8030762")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Viloyat: {iqlim[1]}\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_sa":
                kundalik = kunlar("39.6408363,66.8030762")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: {kundalik[12]}\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_sa":
                kun_davomi = kunlar_davomi("39.6408363,66.8030762")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: {kun_davomi[1]}da 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")


            if callback.data == "hozirgi_kun_ji":
                iqlim = hozir("40.3720098,67.8001639")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Viloyat: Jizzakh\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_ji":
                kundalik = kunlar("40.3720098,67.8001639")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: Jizzakh\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_ji":
                kun_davomi = kunlar_davomi("40.3720098,67.8001639")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: Jizzakhda 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")


            if callback.data == "hozirgi_kun_sir":
                iqlim = hozir("40.4977982,68.7429561")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Viloyat: Sirdaryo\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_sir":
                kundalik = kunlar("40.4977982,68.7429561")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: Sirdaryo\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_sir":
                kun_davomi = kunlar_davomi("40.4977982,68.7429561")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: Sirdaryoda 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")


            if callback.data == "hozirgi_kun_to":
                iqlim = hozir("41.2827379,69.1145562")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Poytaxt: {iqlim[1]}\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_to":
                kundalik = kunlar("41.2827379,69.1145562")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: {kundalik[12]}\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_to":
                kun_davomi = kunlar_davomi("41.2827379,69.1145562")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: {kun_davomi[1]}da 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")


            if callback.data == "hozirgi_kun_an":
                iqlim = hozir("40.7795071,72.1548348")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Viloyat: {iqlim[1]}\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_an":
                kundalik = kunlar("40.7795071,72.1548348")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: {kundalik[12]}\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_an":
                kun_davomi = kunlar_davomi("40.7795071,72.1548348")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: {kun_davomi[1]}da 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")


            if callback.data == "hozirgi_kun_fa":
                iqlim = hozir("40.3798763,71.7080601")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Viloyat: {iqlim[1]}\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_fa":
                kundalik = kunlar("40.3798763,71.7080601")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: {kundalik[12]}\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_fa":
                kun_davomi = kunlar_davomi("40.3798763,71.7080601")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: {kun_davomi[1]}da 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")


            if callback.data == "hozirgi_kun_nam":
                iqlim = hozir("40.9998388,71.6222582")
                bot.send_message(callback.message.chat.id, f"Respublika: {iqlim[0]}, Viloyat: {iqlim[1]}\nHozirda: {iqlim[3]}\nHarorat: {iqlim[2]} C")
                bot.send_message(callback.message.chat.id, f"Kun davomida:\n{iqlim[5]} Harorat: {iqlim[6]} C\n{iqlim[8]} Harorat: {iqlim[9]} C \n{iqlim[11]} Harorat: {iqlim[12]} C\n{iqlim[14]} Harorat: {iqlim[15]} C\n{iqlim[17]} Harorat: {iqlim[18]} C\n{iqlim[20]} Harorat: {iqlim[21]} C\n{iqlim[23]} Harorat: {iqlim[24]} C\n{iqlim[26]} Harorat: {iqlim[27]} C {iqlim[29]}")
            elif callback.data == "uch_kunlik_nam":
                kundalik = kunlar("40.9998388,71.6222582")
                bot.send_message(callback.message.chat.id, f"Respublika: {kundalik[13]}, Viloyat: {kundalik[12]}\nBugun: {kundalik[0]}\nHarorat:  {kundalik[1]} / {kundalik[2]} C \n{kundalik[3]}")
                bot.send_message(callback.message.chat.id, f"Ertaga: {kundalik[4]}\nHarorat:  {kundalik[5]} / {kundalik[6]} C \n{kundalik[7]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun: {kundalik[8]}\nHarorat:  {kundalik[9]} / {kundalik[10]} C \n{kundalik[11]}")
            elif callback.data == "uch_kun_davomi_nam":
                kun_davomi = kunlar_davomi("40.7944231,71.8123552")
                bot.send_message(callback.message.chat.id, f"Respublika: {kun_davomi[0]}, Viloyat: {kun_davomi[1]}da 3 kunlikni kun davomidagi haroratlar!")
                bot.send_message(callback.message.chat.id, f"Bugun kun davomida:\n{kun_davomi[2]} Harorat: {kun_davomi[3]} C\n{kun_davomi[4]} Harorat: {kun_davomi[5]} C \n{kun_davomi[6]} Harorat: {kun_davomi[7]} C\n{kun_davomi[8]} Harorat: {kun_davomi[9]} C\n{kun_davomi[10]} Harorat: {kun_davomi[11]} C\n{kun_davomi[12]} Harorat: {kun_davomi[13]} C\n{kun_davomi[14]} Harorat: {kun_davomi[15]} C\n{kun_davomi[16]} Harorat: {kun_davomi[17]} C {kun_davomi[18]}")
                bot.send_message(callback.message.chat.id, f"Ertangi kun davomida:\n{kun_davomi[19]} Harorat: {kun_davomi[20]} C\n{kun_davomi[21]} Harorat: {kun_davomi[22]} C \n{kun_davomi[23]} Harorat: {kun_davomi[24]} C\n{kun_davomi[25]} Harorat: {kun_davomi[26]} C\n{kun_davomi[27]} Harorat: {kun_davomi[28]} C\n{kun_davomi[29]} Harorat: {kun_davomi[30]} C\n{kun_davomi[31]} Harorat: {kun_davomi[32]} C\n{kun_davomi[33]} Harorat: {kun_davomi[34]} C {kun_davomi[35]}")
                bot.send_message(callback.message.chat.id, f"Kiyingi kun davomida:\n{kun_davomi[36]} Harorat: {kun_davomi[37]} C\n{kun_davomi[38]} Harorat: {kun_davomi[39]} C \n{kun_davomi[40]} Harorat: {kun_davomi[41]} C\n{kun_davomi[42]} Harorat: {kun_davomi[43]} C\n{kun_davomi[44]} Harorat: {kun_davomi[45]} C\n{kun_davomi[46]} Harorat: {kun_davomi[47]} C\n{kun_davomi[48]} Harorat: {kun_davomi[49]} C\n{kun_davomi[50]} Harorat: {kun_davomi[51]} C {kun_davomi[52]}")

            if callback.data == "test10":
                bot.send_message(callback.message.chat.id, f"Toshkentda kunlik ob havo☀️", reply_markup=keybort_to)
            elif callback.data == "test1":
                bot.send_message(callback.message.chat.id, f"Qashqadaryoda kunlik ob havo☀️", reply_markup=keybort_qa)
            elif callback.data == "test2":
                bot.send_message(callback.message.chat.id, f"Surxondaryoda kunlik ob havo☀️", reply_markup=keybort_su)
            elif callback.data == "test3":
                bot.send_message(callback.message.chat.id, f"Xorazimda kunlik ob havo☀️", reply_markup=keybort_xo)
            elif callback.data == "test4":
                bot.send_message(callback.message.chat.id, f"Qoraqalpog'stonda kunlik ob havo☀️", reply_markup=keybort_qor)
            elif callback.data == "test6":
                bot.send_message(callback.message.chat.id, f"Buxoroda kunlik ob havo☀️", reply_markup=keybort_bu)
            elif callback.data == "test5":
                bot.send_message(callback.message.chat.id, f"Navoiyda kunlik ob havo☀️", reply_markup=keybort_na)
            elif callback.data == "test7":
                bot.send_message(callback.message.chat.id, f"Samarqandda kunlik ob havo☀️", reply_markup=keybort_sa)
            elif callback.data == "test8":
                bot.send_message(callback.message.chat.id, f"Jizzaxda kunlik ob havo☀️", reply_markup=keybort_ji)
            elif callback.data == "test9":
                bot.send_message(callback.message.chat.id, f"Sirdaryoda kunlik ob havo☀️", reply_markup=keybort_sir)
            elif callback.data == "test11":
                bot.send_message(callback.message.chat.id, f"Andijonda kunlik ob havo☀️", reply_markup=keybort_an)
            elif callback.data == "test12":
                bot.send_message(callback.message.chat.id, f"Farg'onada kunlik ob havo☀️", reply_markup=keybort_fa)
            elif callback.data == "test13":
                bot.send_message(callback.message.chat.id, f"Namanganda kunlik ob havo☀️",reply_markup=keybort_nam)

            if callback.data == "ins":
                bot.send_message(callback.message.chat.id,"Instagram video linkini tashlang!: ", )
            if callback.data == "tik":
                bot.send_message(callback.message.chat.id,"Tik Tok video linkini tashlang!: ", )
            if callback.data == "yut":
                bot.send_message(callback.message.chat.id,"You Tube video linkini tashlang!: ", )
                


            if callback.data == "orqaga":
                bot.send_message(callback.message.chat.id,"Bo'limlar haqida malumot olish: /help", reply_markup=send_welcome_menu(callback))
            if callback.data == "menu":
                bot.send_message(callback.message.chat.id,"Bo'limlar haqida malumot olish: /help", reply_markup=send_welcome_menu(callback))
            elif callback.data == "about":
                bot.send_message(callback.message.chat.id,"Bo'limlar haqida malumot olish: /help", reply_markup=send_welcome_about(callback))
            if callback.data == "answer_ob_havo": 
                xabar = battom(callback)
                bot.send_message(callback.message.chat.id,"Sizga qaysi viloyat ob havosi kerak ?", reply_markup=xabar)

            elif callback.data == "answer_ramazon_kalindar":
                taqvim = battom_taqvim(callback)
                bot.send_message(callback.message.chat.id, "Sizga qaysi viloyat, ramazon taqvim kerak?",reply_markup=taqvim)
            elif callback.data == "answer_tarjimon":
                bot.send_message(callback.message.chat.id,"Boshlanish kalitni kiritib izdan tarjima qilmoqchi bo'lgan hoxlagan tildagi so'zlarni kiritib yuboring!",reply_markup=send_welcome(callback))
            elif callback.data == "answer_musiqa_topish":
                bot.send_message(callback.message.chat.id, "Iashlamaydi❌", reply_markup=send_welcome_music(callback))
            elif callback.data == "answer_video_topish":
                bot.send_message(callback.message.chat.id, "Men faqat, 3ta ilovadagi videolarni topa olaman, shu ilovalar video linkini tashlang!!",reply_markup=send_welcome_video(callback) )

    except:
        bot.send_message(chat_id = callback.from_user.id, text="Tizimda xatolik chiqdi kiyinroq urinib ko'ring!")


def tarjima(message):
    try:
        k = message
        lug = k.split(">")
        if lug[0].upper() == "UZ" or lug[0].upper() == "RU" or lug[0].upper() == "EN" or lug[0].upper()=="AR":
            try:
                if lug[0].lower() == "en":
                    reg = re.search(f">.*",k)
                    suz =str(reg.group(0))
                    message = translator.translate(suz, lug[0])
                    x = str(message.text)
                    if x.upper() == suz.upper():
                        return f"Tarjima qilinamaydigan so'z!{x}"
                    else:
                      return x
                elif lug[0].lower() == "uz":
                    reg = re.search(f">.*",k)
                    suz =str(reg.group(0))
                    message = translator.translate(suz, lug[0])
                    x = str(message.text)
                    if x.upper() == suz.upper():
                        return f"Tarjima qilinamaydigan so'z!{x}"
                    else:
                      return x
                elif lug[0].lower() == "ru":
                    reg = re.search(f">.*",k)
                    suz =str(reg.group(0))
                    message = translator.translate(suz, lug[0])
                    x = str(message.text)
                    if x.upper() == suz.upper():
                        return f"Tarjima qilinamaydigan so'z!{x}"
                    else:
                      return x
                elif lug[0].lower() == "ar":
                    reg = re.search(f">.*",k)
                    suz =str(reg.group(0))
                    message = translator.translate(suz, lug[0])
                    x = str(message.text)
                    if x.upper() == suz.upper():
                        return f"Tarjima qilinamaydigan so'z!{x}"
                    else:
                       return x
            except:
                return "Bu so'zni tarjma qilolmadim uzur😫\nBoshqa so'z tashlab ko'ring🙃"
            
    except:
        return "Tizimda xato chiqdi!"





@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # print(message)

    try:
        if message.text == 'Qashadaryo_taqvimi🗓':
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Qashqadaryo.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())
        
        elif message.text == 'Surxondaryo_taqvimi🗓':
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Surxondaryo.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == 'Xorazim_taqvimi🗓':
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Xorazim.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())
        

        elif message.text == "Qoraqalpog'iston_taqvimi🗓":
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Nukus.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == 'Navoiy_taqvimi🗓':
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Navoiy.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())


        elif message.text == 'Buxoro_taqvimi🗓':
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Buxoro.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == 'Samarqand_taqvimi🗓':
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Samarqand.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == 'Jizzax_taqvimi🗓':
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Jizzax.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())
        

        elif message.text == 'Sirdaryo_taqvimi🗓':
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Sirdaryo.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == 'Toshkent_taqvimi🗓':
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Toshkent.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == 'Andijon_taqvimi🗓':
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Andijon.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == "Farg'ona_taqvimiq🗓":
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Farg'ona.png?raw=true?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())
            
        elif message.text == "Namangan_taqvimi🗓":
            requests.get("https://api.telegram.org/bot<token>/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Namangan.png?raw=true?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())
        
        if message.text == 'Saharlik_duosi🌅':   
            bot.send_message(message.chat.id, f"Saharlik duosi — Navaytu an asuma sovma shahri ramazona minal fajri ilal mag'ribi, xolisan lillahi ta'ala. Allohu akbar.")   
        elif message.text == "Iftorlik_duosi🌄":
            bot.send_message(message.chat.id, f"Iftorlik duosi — Allohumma laka sumtu va bika amantu va a'layka tavakkaltu va a'la rizqika aftartu, fag'firli ya g'offaru ma qoddamtu va ma axxortu.")
        k = message.text 
    
        trj = tarjima(message.text)
        if trj:
            yub = trj
        else:
            yub = message.text
        
        # yub = message.text
        tek = yub.split("/")
        if len(tek) > 3:
            id = message.from_user.id
            if "instagram.com" in yub or "tiktok.com" in yub:
                link = download(yub)
                bot.send_message(chat_id=id, text="Qidrilmoqad....📲")
                if link :
                    if "instagram.com" in yub:
                        try:
                            
                            bot.send_video(chat_id=id, video=link[1])
                            bot.send_message(chat_id=id, text="Instagram vidiosi!")
                            bot.send_message(chat_id=id, text="Instagram vidiosi boshlanish rasmi🏙!")
                            bot.send_photo(chat_id=id, photo=link[0], caption="Yordamimiz tekanidan xursandman😉")
                        except:
                            bot.send_message(chat_id=id, text="Bu Instagram linki xato qarab tashlang tashlang!")
                    
                    elif "tiktok.com" in yub:
                                            
                        try:
                            bot.send_video(chat_id=id, video=link[0])
                            bot.send_message(chat_id=id, text="Tiktok vidiosi!")
                            bot.send_message(chat_id=id, text=f"Video profil nicki: {link[1]}!")
                            bot.send_message(chat_id=id, text=f"Vidiosi haqida: {link[2]}!")
                            bot.send_message(chat_id=id, text=f"Video signaturesi: {link[1]} \nYordamimiz tekanidan xursandman😉")
                        except:
                            bot.send_message(chat_id=id, text="Bu Tiktok linki xato qarab tashlang tashlang!")
                    
                else:
                    bot.send_message(chat_id=id, text="Bu link xato!") 
                
                
            elif "https://youtu" in yub or "https://www.youtu" in yub:
                    bot.send_message(chat_id=id, text="Qidirilmoqda!📲")
                    try:
                        url = "https://social-media-video-downloader.p.rapidapi.com/smvd/get/all"

                        querystring = {"url":yub,"filename":"Test video"}

                        headers = {
                            "X-RapidAPI-Key": "8a22ef3d9fmsh270fd82095a906fp1f8bc7jsn3c01f1038443",
                            "X-RapidAPI-Host": "social-media-video-downloader.p.rapidapi.com"
                                    }

                        response = requests.get(url, headers=headers, params=querystring)

                        link = response.json()
                        fotos = link["picture"]
                        videos = link["links"][0]["link"]
                        try:
                            bot.send_photo(chat_id=id, photo=fotos, caption="Video fotosi!")
                            bot.send_video(chat_id=id, video=videos, caption="Siz so'ragan video\n Yordamimiz tekanidan xo'rsandman😉!")
                        except:
                            bot.send_message(chat_id=id, text="Afsus videoni topolmadim😭")
                    except:
                        bot.send_message(chat_id=id, text="Uzur tizimda muamo chiqdi🥶")
                        
            else:
            
                bot.send_message(chat_id=id, text="Link xato yuborilgam qarab qayta yuboring!")
        else:
           pass
    except:
        bot.send_message(chat_id = message.from_user.id, text="Tizimda xatolik chiqdi kiyinroq urinib ko'ring!")
    bot.reply_to(message, yub)

bot.polling()
	


import telebot,re
from telebot import types
import requests
from bs4 import BeautifulSoup as bs
from googletrans import Translator
translator = Translator()

viloyatlar = ["карши", "ташкент", "термез", "ургенч", "нукус", "бухара", "навои", "самарканд", "джизак", "сырдарья", "андижан", "фергана", "наманган"]
javob = []
for viloyat in viloyatlar:
    url =requests.get("https://sinoptik.ua/погода-"+viloyat)
    htm_url = bs(url.content, 'html.parser')
    for name in htm_url.select("#content"):

        data = name.select(".date")[0].text
        month = name.select(".month")[0].text

        data2 = name.select(".date")[1].text
        month2 = name.select(".month")[1].text

        data3 = name.select(".date")[2].text
        month3 = name.select(".month")[2].text

        data4 = name.select(".date")[3].text
        month4 = name.select(".month")[3].text

        data5 = name.select(".date")[4].text
        month5 = name.select(".month")[4].text

        min = name.select(".temperature .min")[0].text
        max = name.select(".temperature .max")[0].text

        min2 = name.select(".temperature .min")[1].text
        max2 = name.select(".temperature .max")[1].text

        min3 = name.select(".temperature .min")[2].text
        max3 = name.select(".temperature .max")[2].text

        min4 = name.select(".temperature .min")[3].text
        max4 = name.select(".temperature .max")[3].text

        min5 = name.select(".temperature .min")[4].text
        max5 = name.select(".temperature .max")[4].text
        javob.append(data + "-" + month + " "+min[4:]+" : "+ max[5:]+";     "+data2 + "-" + month2 + " "+ min2[4:] + " : "+ max2[5:]+";      "+data3 + "-" + month3 + " "+ min3[4:]+" : "+ max3[5:]+";        "+data4 + "-" + month4 + " "+ min4[4:]+" : "+ max4[5:]+";      "+data5 + "-" + month5 + " "+ min5[4:]+" : "+max5[5:])
       
TOKEN = "7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0"

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
            if callback.data == "test10":
                bot.send_message(callback.message.chat.id, f"Toshkentda 5 kunlik ob havo☀️\n{javob[1]} daraja")
            elif callback.data == "test1":
                bot.send_message(callback.message.chat.id, f"Qahqadaryoda 5 kunlik ob havo☀️\n{javob[0]} daraja")
            elif callback.data == "test2":
                bot.send_message(callback.message.chat.id, f"Surxondaryoda 5 kunlik ob havo☀️\n{javob[2]} daraja")
            elif callback.data == "test3":
                bot.send_message(callback.message.chat.id, f"Xorazimda 5 kunlik ob havo☀️\n{javob[3]} daraja")
            elif callback.data == "test4":
                bot.send_message(callback.message.chat.id, f"Qoraqalpog'stonda 5 kunlik ob havo☀️\n{javob[4]} daraja")
            elif callback.data == "test6":
                bot.send_message(callback.message.chat.id, f"Buxoroda 5 kunlik ob havo☀️\n{javob[5]} daraja")
            elif callback.data == "test5":
                bot.send_message(callback.message.chat.id, f"Navoiyda 5 kunlik ob havo☀️\n{javob[6]} daraja")
            elif callback.data == "test7":
                bot.send_message(callback.message.chat.id, f"Samarqandda 5 kunlik ob havo☀️\n{javob[7]} daraja")
            elif callback.data == "test8":
                bot.send_message(callback.message.chat.id, f"Jizzaxda 5 kunlik ob havo☀️\n{javob[8]} daraja")
            elif callback.data == "test9":
                bot.send_message(callback.message.chat.id, f"Sirdaryoda 5 kunlik ob havo☀️\n{javob[9]} daraja")
            elif callback.data == "test11":
                bot.send_message(callback.message.chat.id, f"Andijonda 5 kunlik ob havo☀️\n{javob[10]} daraja")
            elif callback.data == "test12":
                bot.send_message(callback.message.chat.id, f"Farg'onada 5 kunlik ob havo☀️\n{javob[11]} daraja")
            elif callback.data == "test13":
                bot.send_message(callback.message.chat.id, f"Namanganda 5 kunlik ob havo☀️\n{javob[12]} daraja")

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
    print(message)

    try:
        if message.text == 'Qashadaryo_taqvimi🗓':
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Qashqadaryo.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())
        
        elif message.text == 'Surxondaryo_taqvimi🗓':
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Surxondaryo.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == 'Xorazim_taqvimi🗓':
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Xorazim.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())
        

        elif message.text == "Qoraqalpog'iston_taqvimi🗓":
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Nukus.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == 'Navoiy_taqvimi🗓':
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Navoiy.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())


        elif message.text == 'Buxoro_taqvimi🗓':
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Buxoro.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == 'Samarqand_taqvimi🗓':
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Samarqand.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == 'Jizzax_taqvimi🗓':
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Jizzax.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())
        

        elif message.text == 'Sirdaryo_taqvimi🗓':
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Sirdaryo.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == 'Toshkent_taqvimi🗓':
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Toshkent.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == 'Andijon_taqvimi🗓':
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Andijon.png?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())

        elif message.text == "Farg'ona_taqvimiq🗓":
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Farg'ona.png?raw=true?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
            bot.send_message(message.chat.id, f"Qaysi duo kerak bo'lsa bosing!", reply_markup=taqvim())
            
        elif message.text == "Namangan_taqvimi🗓":
            requests.get("https://api.telegram.org/bot7070553394:AAHSe2NY4dzPPhxSSvXKu0n2_BCsnoAJiV0/sendPhoto?chat_id=6631020188&photo=https://github.com/NwBornoy/Picture-of-the-Ramadan-calendar-2024/blob/main/foto/Namangan.png?raw=true?raw=true&caption=Ro'zadorlarimiz uchun taqvim")
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
	


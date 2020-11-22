class Translation(object):
    START_TEXT = """Merhaba!
Bu bir Telegram'a URL yükleme botudur.

<b>Bana Telegram'a Dosya/Video olarak yükleyebileceğim bir link gönderin.</b>

Daha fazla detay için /help komutunu kullanabilirsiniz.

Depo Botu : @thunderdepo_Bot"""
    RENAME_403_ERR = "Üzgünüm. Bu dosyayı yeniden adlandırmak için yetkilendirilmediniz."
    ABS_TEXT = " Lütfen bencil olma."
    UPGRADE_TEXT = ""
    FORMAT_SELECTION = "İstenen formatı seçin: <a href='{}'> (Dosya boyutu yaklaşık olabilir.)</a> \nÖzel küçük resim ayarlamak istiyorsanız, aşağıdaki düğmelerden herhangi birine dokunmadan önce veya hızlıca fotoğraf gönderin.\nOtomatik oluşturulan küçük resmi silmek isterseniz /deletethumbnail komutunu kullanabilirsiniz."
    SET_CUSTOM_USERNAME_PASSWORD = """Premium videolar indirmek istiyorsanız, bu formatı uygulayın: URL | Dosya Adı | Kullanıcı Adı | Şifre"""
    NOYES_URL = "@robot URL tespit edildi. Lütfen <a href='http://thunderleech.xyz/'>bu siteyi</a> kullanın ve diğer kullanıcılar için yavaşlamadan Telegram'a yükleyebilmem için bana hızlı bir URL alın."
    DOWNLOAD_START = "İndiriliyor..."
    UPLOAD_START = "Yükleniyor..."
    RCHD_BOT_API_LIMIT = "İzin verilen maksimum boyuttan (50MB) büyük boyut. Yine de yüklemeye çalışıyorum."
    RCHD_TG_API_LIMIT = "{} Saniyede indirildi.\nAlgılanan Dosya Boyutu: {}\nÜzgünüm. Ancak Telegram API sınırlamaları nedeniyle 1.5 GB'tan büyük dosyaları yükleyemiyorum."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Lütfen beni faydalı bulursan derecelendir. Şuraya katılmaya ne dersin : @thunderBots0"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "{} Saniyede indirildi. \n{} Saniyede yüklendi."
    NOT_AUTH_USER_TEXT = ""
    NOT_AUTH_USER_TEXT_FILE_SIZE = ""
    SAVED_CUSTOM_THUMB_NAIL = "Özel video/dosya küçük resmi kaydedildi. Bu resim video/dosyada kullanılacaktır."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Özel küçük resim başarıyla silindi."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Medya başarıyla silindi."
    SAVED_RECVD_DOC_FILE = "Belge Başarıyla İndirildi."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Özel Küçük Resim bulunamadı."
    NO_VOID_FORMAT_FOUND = "HATA!!! \n<b>YouTubeDL</b> diyor ki: {}"
    USER_ADDED_TO_DB = ""
    CURENT_PLAN_DETAILS = """"""
    HELP_USER = """Merhaba! Bu bir URL yükleme botu.
    
1. Link gönder (Link|Uzantıyla birlikte yeni isim).
2. Özel Küçük Resim Gönder (İsteğe bağlı).
3. Butonu Seç
   SVideo - Ekran Görüntüleriyle Dosyayı Video Olarak Gönderir
   DFile  - Ekran Görüntüleriyle Dosya Gönderir
   Video  - Dosyayı Ekran Görüntüleri Olmadan Video Olarak Gönderir
   DFile  - Ekran Görüntüleri Olmadan Dosya Gönderir
   
<a href="https://t.me/thunderBots0">Kanalıma Katıl!</a>

--------

Destek:  @thunderBots0"""
    REPLY_TO_DOC_GET_LINK = "Yüksek Hızlı Doğrudan İndirme Bağlantısı almak için bir Telegram medyasına yanıt verin"
    REPLY_TO_DOC_FOR_C2V = "Dönüştürmek için bir Telegram medyasına yanıt verin"
    REPLY_TO_DOC_FOR_SCSS = "Ekran görüntüsü almak için bir Telegram medyasına yanıt verin"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Bir Telegram medyasını yeniden adlandırmak için ona /rename ile yanıt verin"
    AFTER_GET_DL_LINK = "Doğrudan Bağlantı <a href='{}'> oluşturuldu </a>, {} gün boyunca geçerlidir.\n@thunderBots0"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Kullanım: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "Depolama alanıma medyayı indirmek için ona /downloadmedia ile yanıt verin. \nİndirilen dosya hakkında bilgi almak için /storageinfo komutunu kullanın."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Süresi: {}\nBu medyayı depolama alanımdan silmek için ona /clearffmpegmedia ile yanıt verin.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/BotProjects0'>@thunderBots0</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> http://rapidleech.gq and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

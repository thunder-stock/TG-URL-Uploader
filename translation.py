class Translation(object):
    START_TEXT = """Merhaba! Ben bir telegram URL Yükleme Botuyum.
<b>Lütfen bana bir direkt indirme linki gönderin, telegrama video/dosya şeklinde gönderebilirim.</b>
Daha fazla detay için /help yazın.
Support : @whitedoton """
    RENAME_403_ERR = "Üzgünüm, bu dosyayı yeniden adlandırma izniniz yok."
    ABS_TEXT = " Lütfen bencil olma."
    UPGRADE_TEXT = ""
    FORMAT_SELECTION = "İstediğiniz formatı seçin: <a href='{}'>Dosya boyutu yaklaşık olabilir.</a> \nÖzel küçük resim ayarlamak istiyorsanız, aşağıdaki düğmelerden birine dokunmadan önce veya hızlı bir şekilde fotoğraf gönderin.\nOtomatik oluşturulmuş küçük resmi silmek için /deletethumbnail komutunu kullanabilirsiniz."
    SET_CUSTOM_USERNAME_PASSWORD = """Eğer premium videolar indirmek istiyorsanız aşağıdaki formatı uygulayın:
URL | Dosya adı | Kullanıcı Adı | Şifre"""
    NOYES_URL = "@robot URL tespit edildi. Lütfen https://shrtz.me/PtsVnf6 linkini kullanın ve diğer kullanıcılar için yavaşlamadan Telegram'a yükleyebilmem için hızlı bir URL alın."
    DOWNLOAD_START = "İndiriliyor..."
    UPLOAD_START = "Telegrama yükleniyor..."
    RCHD_BOT_API_LIMIT = "İzin verilen maksimum boyuttan daha büyük boyut (50 MB). Yine de yüklemeye çalışılıyor."
    RCHD_TG_API_LIMIT = "{} Saniyede indirildi. \nTespit edilen dosya boyutu: {}\nÜzgünüm ama Telegram API limiti sebebiyle 1.5 GB dan büyük dosyalar yükleyem."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Eğer beni kullanışlı bulduysan değerlendirmeyi unutma: @thebotmaker0"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "{} Saniyede indirildi. \n{} Saniyede yüklendi."
    NOT_AUTH_USER_TEXT = "Lütfen aboneliğinizi yükseltmek için /upgrade komutunu kullanın."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Tespit Edilen Dosya Boyutu: {}. Aboneliği olmayan kullanıcıların yükleyebildiği boyut: {}\nLütfen aboneliğinizi arttırmak için /upgrade komutunu kullanın.\nBunun bir hata olduğunu düşünüyorsanız, lütfen <a href='https://t.me/thebotmaker0'>@thebotmaker0</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Özel video/dosya küçük resmi kaydedildi. Bu resim yüklenen videolarda/dosyalarda kullanılacak."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Özel küçük resim başarıyla silindi."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Medya başarıyla silindi."
    SAVED_RECVD_DOC_FILE = "Dosya Başarıyla İndirildi."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Özel Küçük Resim Bulunamadı."
    NO_VOID_FORMAT_FOUND = "HATA...\n<b>YouTubeDL</b> diyor ki: {}"
    USER_ADDED_TO_DB = "Kullanıcı <a href='tg://user?id={}'>{}</a> eklendi {}."
    CURENT_PLAN_DETAILS = """Şuanki plan detayları
--------
Telegram ID: <code>{}</code>
Plan name: Free Cloned User
Expires on: 31/12/2020"""
    HELP_USER = """Merhaba, ben URL Yükleme Botuyum.
    
1. Link Gönderin. (Link|Uzantı ve Yeni Dosya Adı).
2. Özel Küçük Resim Gönderin. (İsteğe Bağlı).
3. Buton Seçin.
   SVideo - Videoyu Ekran Görüntüleri ile Gönderir.
   DFile  - Dosyayı Ekran Görüntüleri ile Gönderir.
   Video  - Videoları Ekran Görüntüleri Olmadan Gönderir
   DFile  - Dosyaları Ekran Görüntüleri Olmadan Gönderin.
   
<b>👉 Kendi Botunuzu Oluşturun :</b> 👉 <a href="#">Yakında!</a>
--------
Şuanki planınızı görüntülemek için /me komutunu gönderin.
Support Destek : @thebotmaker0
"""
    REPLY_TO_DOC_GET_LINK = "Yüksek Hızlı Doğrudan İndirme Bağlantısı almak için bir Telegram dosyasına yanıt verin."
    REPLY_TO_DOC_FOR_C2V = "Dönüştürmek istediğiniz bir Telegram dosyasına yanıt verin."
    REPLY_TO_DOC_FOR_SCSS = "Ekran görüntüsü almak istediğiniz telegram dosyasına yanıt verin."
    REPLY_TO_DOC_FOR_RENAME_FILE = "Dosyayı özel küçük resim desteğiyle göndermek için Telegram dosyasını /rename ile yanıtlayın."
    AFTER_GET_DL_LINK = "Direkt İndirme Linki <a href='{}'>Oluşturuldu</a> {} gün için geçerlidir.\n© @URLUploader0_Bot"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
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
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

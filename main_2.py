from flask import Flask, send_from_directory
import random
import os

IMAGE_FOLDER = "m2l1/images"

app = Flask(__name__)
facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
"Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
"2019'da yapılan bir araştırmaya göre, insanların %60 ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
"Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
"Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
"Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
"Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]
@app.route("/")
def home():
    return f'''
        <a href="/main_2">Rastgele bir gerçeği görüntüle!</a><br>
        <a href="/resim">Rastgele bir resim görüntüle!</a>
    '''
@app.route("/main_2")
def hello_world():
    return f'''
        <p>{random.choice(facts_list)}</p><br>
        <a href="/">Geri dön</a>
    '''
@app.route("/resim")
def resim():
    # Klasördeki tüm resimleri listele
    image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    if not image_files:
        return "<p>Resim bulunamadı!</p><br><a href='/'>Geri dön</a>"

    # Rastgele bir resim seç
    selected_image = random.choice(image_files)

    return f'''
        <img src="/get_image/{selected_image}" alt="Rastgele Resim"><br>
        <a href="/">Geri dön</a>
    '''

@app.route("/get_image/<filename>")
def get_image(filename):
    """Belirtilen dosyayı `m2l1/images` klasöründen getirir."""
    return send_from_directory(IMAGE_FOLDER, filename)
    
if __name__ == "__main__":
    app.run(debug=True)

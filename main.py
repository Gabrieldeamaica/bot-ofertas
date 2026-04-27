import requests
import random
import time
from flask import Flask

app = Flask(__name__)

TOKEN = "8776735092:AAEJn_AmUj3mxELsqi0scrYE0Gf-_58geFI"
CANAL = "@MegaOfertasMercadoLivre"

@app.route('/')
def home():
    return "Bot Online!"

@app.route('/disparar')
def disparar():
    termos = ["eletronicos", "ferramentas", "gamer"]
    busca = random.choice(termos)
    url_ml = f"https://api.mercadolibre.com/sites/MLB/search?q={busca}"
    
    try:
        res = requests.get(url_ml).json()
        produtos = res.get('results', [])
        
        for p in produtos[:10]:
            titulo = p['title']
            preco = p['price']
            link = p['permalink']
            msg = f"📦 {titulo}\n💰 R$ {preco}\n🛒 {link}"
            
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                          data={"chat_id": CANAL, "text": msg})
            time.sleep(1)
            
        return "Ofertas enviadas!", 200
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

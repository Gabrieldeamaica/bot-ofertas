
import requests
import random
import time
from flask import Flask

app = Flask(__name__)

# --- CONFIGURAÇÕES DO TELEGRAM ---
TOKEN_TELEGRAM = "8776735092:AAEJn_AmUj3mxELsqi0scrYE0Gf-_58geFI"
ID_CANAL = "@MegaOfertasMercadoLivre"

@app.route('/')
def home():
    return "Bot Online!"

@app.route('/disparar')
def disparar_ofertas():
    termos = ["eletronicos", "ferramentas", "casa", "gamer", "cozinha"]
    busca = random.choice(termos)
    url_ml = f"https://api.mercadolibre.com/sites/MLB/search?q={busca}&sort=relevance"
    
    try:
        res = requests.get(url_ml).json()
        produtos = res.get('results', [])
        random.shuffle(produtos)
        
        for p in produtos[:20]:
            titulo = p['title']
            preco = p['price']
            link = p['permalink']
            foto = p['thumbnail'].replace("-I.jpg", "-O.jpg")
            
            msg = f"🔥 **OFERTA ENCONTRADA**\n\n📦 {titulo}\n💰 **R$ {preco}**\n\n🛒 Link: {link}"
            url_tg = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendPhoto"
            requests.post(url_tg, data={"chat_id": ID_CANAL, "photo": foto, "caption": msg, "parse_mode": "Markdown"})
            time.sleep(2)
            
        return "Sucesso! 20 ofertas enviadas.", 200
    except Exception as e:
        return f"Erro: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

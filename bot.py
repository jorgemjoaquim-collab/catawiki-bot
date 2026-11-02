import os
import requests

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def enviar_alerta(mensagem):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("Credenciais do Telegram em falta.")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": mensagem, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Erro ao enviar telegram: {e}")

def verificar_oportunidades():
    print("A verificar leilões no Catawiki (Filtro de Elite)...")
    url = "https://www.catawiki.com/pt/l/ending-soon"
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Erro ao aceder ao site do Catawiki.")
        return

    print("Varredura concluída com sucesso na nuvem.")

if __name__ == "__main__":
    verificar_oportunidades()

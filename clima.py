import requests
import datetime

API_KEY = "b35945e4c343cbdc8c229c811d2ea74e"  

def buscar_temperatura_e_umidade():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=São Paulo,BR&appid={API_KEY}&units=metric&lang=pt_br"

    try:
        response = requests.get(url)
        response.raise_for_status()

        dados = response.json()

        temperatura = f"{round(dados['main']['temp'])}°C"
        umidade = f"{dados['main']['humidity']}%"

        agora = datetime.datetime.now()

        return {
            "data": agora.strftime("%d/%m/%Y"),
            "hora": agora.strftime("%H:%M:%S"),
            "temperatura": temperatura,
            "umidade": umidade
        }

    except Exception as e:
        print("Erro ao buscar dados:", e)
        return None

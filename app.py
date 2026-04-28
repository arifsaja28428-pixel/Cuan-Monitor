import google.generativeai as genai
import requests

# 1. Setting API (Ganti dengan API Key milikmu nanti)
GEMINI_KEY = "AIzaSyCiO_zKOyLUkBu_mkYTnEBCLhLRVtxXLJE"
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def ambil_harga_kripto():
    # Mengambil harga Bitcoin dari API gratis Binance
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    return data['price']

def analisis_gemini(harga):
    prompt = f"Harga Bitcoin saat ini {harga}. Berikan analisis teknikal singkat dan saran Jual atau Beli untuk pemula."
    response = model.generate_content(prompt)
    return response.text

# Tes jalankan di Notepad++
harga_sekarang = ambil_harga_kripto()
print(f"Harga BTC: {harga_sekarang}")
print(f"Analisis: {analisis_gemini(harga_sekarang)}")

import requests
import json

# Прямий запит до Google не рекомендується, але ось як це виглядає
site = 'https://www.google.com/search?q=anime'

# Виконання GET запиту
response = requests.get(site)

# Перевірка статусу запиту
if response.status_code == 200:
    print("Request was successful.")
    # Виведення перших 500 символів вмісту
    print(response.text[:500])  # Виведе частину HTML-коду
else:
    print(f"Request failed with status code: {response.status_code}")

# Відкриття та читання JSON-файлу
try:
    with open('info.json', 'w') as file:
        data = json.load(file)
        data = file.write(response.text[:500])
          # Завантаження даних з JSON
        print(data)  # Виведення вмісту файлу
except FileNotFoundError:
    print("The file 'info.json' does not exist.")
except json.JSONDecodeError:
    print("Error decoding JSON from the file.")

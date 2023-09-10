# Task 1
# Robots.txt
# Download and save to file robots.txt from wikipedia, twitter websites etc. 

import requests

'''wikipedia'''

# URL веб-сайта для отримання данних
website_url_1 = "https://en.wikipedia.org/wiki/Main_Page"

# отримання данних
response = requests.get(website_url_1)
data = response.text

# збереження данних в файл
file_path = r"C:\Users\Asus\Desktop\beetroot\homework_data\hw_33\robots.txt"
with open(file_path, "w", encoding = "utf-8") as file:
    file.write(data)

print(f"данні wikipedia збережено {file_path}")


'''twitter'''

website_url_2 = 'https://twitter.com/?lang=uk'

response = requests.get(website_url_2)
data_2 = response.text

file_path = r"C:\Users\Asus\Desktop\beetroot\homework_data\hw_33\robots.txt"
with open(file_path, "w", encoding = "utf-8") as file:
    file.write(data_2)

print(f"данні twitter збережено {file_path}")

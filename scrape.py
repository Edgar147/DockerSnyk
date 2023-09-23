import time
from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://hub.docker.com/search?q=&type=image&sort=updated_at&order=desc&page_size=1000&operating_system=linux"

headers = {
    "Authorization": "Bearer dckr_pat_X1-oiS81mMl8FsDhXk4NSe6Fjxk"
}

#web driver
driver = webdriver.Chrome()

# naviguer la page
driver.get(url)


for key, value in headers.items():
    driver.execute_script(f"window.localStorage.setItem('{key}', '{value}')")


time.sleep(5)

# recuperer source après l'execution de js
page_source = driver.page_source

# parser avec BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# chercher toutes les lignes contenant /
tags = soup.find_all('strong', text=lambda t: '/' in t and ' ' not in t)

# sauvegarde comme une ligne
with open('dockerImages.txt', 'w') as f:
    for tag in tags:
        f.write(tag.text.strip() + '\n')

#fermer web driver
driver.quit()


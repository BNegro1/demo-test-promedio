from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Ruta al directorio que contiene el controlador de Chrome
driver_dir = 'C:/Program Files/Google/Chrome/Application/'

# Agrega la ruta del directorio del controlador de Chrome al PATH
os.environ['PATH'] += ';' + driver_dir

# Configurar el navegador
driver = webdriver.Chrome()

# Abre la página web
driver.get("https://promedio.onrender.com/")

# Ingresa notas y porcentajes
notas = [10, 9, 8, 7]  # Cambia las notas según sea necesario
porcentajes = [30, 20, 20, 30]  # Cambia los porcentajes según sea necesario

for i in range(len(notas)):
    nota_id = "nota" + str(i + 1)
    porcentaje_id = "porcentaje" + str(i + 1)
    
    nota_element = driver.find_element(By.ID, nota_id)
    nota_element.clear()
    nota_element.send_keys(str(notas[i]))

    porcentaje_element = driver.find_element(By.ID, porcentaje_id)
    porcentaje_element.clear()
    porcentaje_element.send_keys(str(porcentajes[i]))

# Espera unos segundos para que se actualice el cálculo
time.sleep(2)

# Verifica el resultado
promedio = driver.find_element(By.ID, "total").get_attribute("value")
print("Promedio obtenido:", promedio)  # Imprime el valor real del promedio
assert promedio == "8.5"# Cambia el valor según sea necesario

# Cierra el navegador
driver.quit()

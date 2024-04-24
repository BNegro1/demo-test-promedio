from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Ruta al directorio que contiene el controlador de Chrome
driver_dir = 'C:/Program Files/Google/Chrome/Application/'

# Agrega la ruta del directorio del controlador de Chrome al PATH
os.environ['PATH'] += ';' + driver_dir

# Configurar el navegador
driver = webdriver.Chrome()

# Abrir la página web
driver.get("https://promedio.onrender.com/")

# Esperar hasta que el botón "Dar Examen" esté presente y sea clickeable
dar_examen_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "darExamen"))
)

# Dar clic en "Dar Examen"
dar_examen_btn.click()

# Esperar hasta que el elemento "nExamen" esté presente y sea interactuable
nota_examen = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='nExamen']"))
)

# Ingresa la nota del examen
nota_examen.clear()
nota_examen.send_keys("8")

# Esperar unos segundos para que se actualice el cálculo
time.sleep(2)

# Verifica el resultado final
promedio_final = driver.find_element(By.ID, "pFinal").get_attribute("value")
assert promedio_final == "6.5"

# Prueba los botones de agregar notas
boton_agregar_nota = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input.agregarNotas"))
)
boton_agregar_nota.click()

# Verifica que se haya agregado una nueva fila
nueva_fila = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "notaa5"))
)

# Prueba el botón de agregar notas parciales
boton_parciales = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input.notasParciales"))
)
boton_parciales.click()

# Verifica que se muestre la sección de notas parciales
seccion_parciales = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "promedioControles"))
)

# Cierra el navegador
driver.quit()

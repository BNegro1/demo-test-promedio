from selenium import webdriver
from selenium.webdriver.common.by import By

# Ruta al controlador de Chrome (reemplaza con la ruta correcta)
driver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'

# Inicializar el navegador
driver = webdriver.Chrome(executable_path=driver_path)

# Encontrar los campos de entrada para las notas y porcentajes
campos_notas = driver.find_elements(By.CLASS_NAME, "textNota")
campos_porcentajes = driver.find_elements(By.CLASS_NAME, "textPorcentaje")

# Ingresar notas y porcentajes
for i in range(len(campos_notas)):
    campo_nota = campos_notas[i]
    campo_porcentaje = campos_porcentajes[i]

    # Ingresar nota
    campo_nota.clear()  # Limpiar el campo antes de ingresar la nueva nota
    campo_nota.send_keys("10")  # Ingresar la nota deseada

    # Ingresar porcentaje
    campo_porcentaje.clear()  # Limpiar el campo antes de ingresar el nuevo porcentaje
    campo_porcentaje.send_keys("20")  # Ingresar el porcentaje deseado

# Encontrar el botón "Calcular"
boton_calcular = driver.find_element(By.ID, "calcular")

# Hacer clic en el botón "Calcular"
boton_calcular.click()

# Esperar un momento para que se actualice la página
driver.implicitly_wait(5)

# Encontrar el elemento que muestra el resultado
resultado = driver.find_element(By.ID, "total")

# Imprimir el resultado
print("El promedio es:", resultado.get_attribute("value"))

# Cerrar el navegador
driver.quit()

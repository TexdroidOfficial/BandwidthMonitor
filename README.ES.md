# Bandwidth Monitor 🖥️📶

Este es un script simple desarrollado como un proyecto personal para monitorear el uso del ancho de banda de la red (enviado, recibido y total) durante un período de tiempo específico.

## Descripción 📜

El script inicia una interfaz gráfica de usuario (GUI) construida con `customtkinter` al ejecutarse. Una vez que se cierra la ventana de la GUI, el script comienza a monitorear el tráfico de la red utilizando `psutil`. Después del período de monitoreo (el valor predeterminado es de 15 segundos), muestra datos en tiempo real sobre la cantidad de datos recibidos, enviados y el total de datos transferidos, junto con las tasas promedio en la terminal. El script realiza las siguientes operaciones:

1. **Inicio de la GUI:** Abre una ventana de GUI simple construida con `customtkinter`. Al cerrar esta ventana, comienza el proceso de monitoreo.
2. **Monitoreo de la Red:** Monitorea el tráfico de la red (enviado, recibido y total) durante un período de tiempo predefinido (el valor predeterminado es de 15 segundos) utilizando la biblioteca `psutil`.
3. **Visualización de Datos:** Después del período de monitoreo, muestra los datos recopilados en la terminal, incluyendo el total de datos recibidos, enviados y el total de datos transferidos, junto con las tasas promedio.

## Cómo usar 🚀

1. **Requisitos Previos:** Asegúrate de tener Python y las bibliotecas `customtkinter` y `psutil` instaladas en tu sistema. Si estas bibliotecas no están instaladas, instálalas usando pip:

   ```bash
   pip install customtkinter psutil
   ```
2. Navega al directorio del script: Abre la línea de comandos o la terminal y navega al directorio donde se encuentra el archivo del script. Puedes usar el comando `cd` (cambiar directorio) para esto. Por ejemplo, si el script está en la carpeta "MisScripts", usarías: `cd MisScripts`.
3. Ejecución del script: Una vez que estés en el directorio correcto, ejecuta el script desde la línea de comandos usando el siguiente comando:

   ```bash
   python bandwidthMonitor.py
   ```
5. Monitoreo: El script primero abrirá una ventana de GUI construida con `customtkinter`. Cierra la ventana de la GUI para iniciar el monitoreo de la red. El script monitoreará la red durante 15 segundos (o la duración especificada) usando `psutil` y luego mostrará los resultados en la terminal.

## Screenshots 📸

![2025-03-30 17-47-33 start=1 length=23 fps=30](https://github.com/user-attachments/assets/f6b4eff3-c93e-4771-ad1b-9fb49b3d47e7) 

## Licencia 📄

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

##
Hecho con ❤️ por Texdroid

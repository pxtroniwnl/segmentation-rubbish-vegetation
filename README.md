🛰️ Monitoreo de Residuos Sólidos en Canales Hídricos mediante Drones (YOLO11)
Este proyecto implementa un sistema de visión artificial basado en YOLO11 para la detección y clasificación automática de residuos sólidos (rubbish) y cobertura vegetal (vegetation) en canales hídricos. Utiliza imágenes capturadas por drones para facilitar la inspección ambiental en entornos de difícil acceso, como los canales de la ciudad de Cartagena, Colombia.

📌 Descripción del Proyecto
El objetivo principal es identificar simultáneamente múltiples objetos en imágenes de alta resolución. A diferencia de la clasificación simple, este modelo utiliza Detección de Objetos para localizar cada residuo y parche de vegetación mediante cuadros delimitadores (bounding boxes), permitiendo un análisis espacial preciso de la contaminación.

📊 Dataset
El conjunto de datos proviene de una curaduría de imágenes reales de drones y fuentes complementarias procesadas en Roboflow.

Clases:

rubbish: Residuos sólidos (plásticos, icopor, desechos urbanos).

vegetation: Cobertura vegetal y macrófitas acuáticas.

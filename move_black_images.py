import os
import cv2
import numpy as np
from shutil import move

# Directorios de entrada y salida
input_dir = r'C:\Users\Pc\Pictures\images'
output_dir = r'C:\Users\Pc\Pictures\images-back-blackg'

# Crear la carpeta de salida si no existe
os.makedirs(output_dir, exist_ok=True)

def calculate_black_percentage(image_path):
    """Calcula el porcentaje de píxeles negros en una imagen."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Leer en escala de grises
    if image is None:
        return 0

    total_pixels = image.size
    black_pixels = np.sum(image == 0)  # Contar píxeles negros
    return (black_pixels / total_pixels) * 100

# Iterar sobre las imágenes en el directorio de entrada
for filename in os.listdir(input_dir):
    file_path = os.path.join(input_dir, filename)

    # Verificar si es un archivo de imagen
    if not os.path.isfile(file_path):
        continue

    # Calcular el porcentaje de píxeles negros
    black_percentage = calculate_black_percentage(file_path)

    # Si el porcentaje de píxeles negros es >= 20%, mover la imagen
    if black_percentage >= 20:
        move(file_path, os.path.join(output_dir, filename))
        print(f"Movida: {filename} ({black_percentage:.2f}% negra)")
    else:
        print(f"Ignorada: {filename} ({black_percentage:.2f}% negra)")

print("Proceso completado.")
#!/usr/bin/env python3
"""
Script para rotar la imagen 4 a la derecha
"""
from PIL import Image
import os

def rotate_photo4():
    """Rota photo-4.jpg 90 grados a la derecha"""
    
    image_path = "images/photo-4.jpg"
    
    if not os.path.exists(image_path):
        print(f"❌ No se encontró {image_path}")
        return
    
    try:
        # Abrir imagen
        img = Image.open(image_path)
        print(f"📸 Imagen original: {img.size} - Rotación actual: {img.getexif().get(274, 'Normal')}")
        
        # Rotar 90 grados a la derecha (counterclockwise = -90)
        rotated_img = img.rotate(-90, expand=True)
        
        # Guardar
        rotated_img.save(
            image_path,
            'JPEG',
            quality=75,
            optimize=True,
            progressive=True
        )
        
        print(f"✅ Imagen rotada exitosamente a la derecha")
        print(f"📐 Nuevo tamaño: {rotated_img.size}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    rotate_photo4()

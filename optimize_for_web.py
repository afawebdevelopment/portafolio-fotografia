#!/usr/bin/env python3
"""
Script mejorado para optimizar imágenes para web
Comprime agresivamente manteniendo buena calidad visual
"""
from PIL import Image
import os
from pathlib import Path
import shutil

def optimize_images_for_web(folder_path="images"):
    """
    Optimiza imágenes para web:
    - Redimensiona a 1200px máximo
    - Comprime a 75% de calidad
    - Convierte a RGB si es necesario
    """
    
    image_files = list(Path(folder_path).glob("*.jpg")) + \
                  list(Path(folder_path).glob("*.JPG")) + \
                  list(Path(folder_path).glob("*.jpeg")) + \
                  list(Path(folder_path).glob("*.JPEG"))
    
    if not image_files:
        print("❌ No se encontraron imágenes JPG")
        return
    
    print(f"🖼️  Optimizando {len(image_files)} imágenes para web...\n")
    
    total_original = 0
    total_optimized = 0
    
    for image_path in sorted(image_files):
        try:
            filename = image_path.name
            
            # Obtener tamaño original
            original_size = image_path.stat().st_size / (1024 * 1024)
            total_original += original_size
            
            # Abrir imagen
            img = Image.open(image_path)
            original_width, original_height = img.size
            
            # Redimensionar si es muy grande
            max_dimension = 1200
            if original_width > max_dimension or original_height > max_dimension:
                img.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)
            
            # Convertir RGBA a RGB si es necesario
            if img.mode in ('RGBA', 'LA', 'P'):
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = rgb_img
            
            # Guardar optimizado
            img.save(
                image_path,
                'JPEG',
                quality=75,
                optimize=True,
                progressive=True  # Carga progresiva
            )
            
            # Obtener tamaño optimizado
            optimized_size = image_path.stat().st_size / (1024 * 1024)
            total_optimized += optimized_size
            
            reduction = ((original_size - optimized_size) / original_size * 100) if original_size > 0 else 0
            
            print(f"✅ {filename}")
            print(f"   Antes: {original_size:.2f} MB ({original_width}x{original_height}px)")
            print(f"   Ahora: {optimized_size:.2f} MB | Reducción: {reduction:.1f}%\n")
            
        except Exception as e:
            print(f"❌ Error procesando {image_path.name}: {e}\n")
    
    print("=" * 60)
    print(f"📊 RESUMEN FINAL:")
    print(f"Tamaño total original: {total_original:.2f} MB")
    print(f"Tamaño total optimizado: {total_optimized:.2f} MB")
    reduction_total = ((total_original - total_optimized) / total_original * 100) if total_original > 0 else 0
    print(f"Reducción total: {reduction_total:.1f}%")
    print("=" * 60)

if __name__ == "__main__":
    optimize_images_for_web("images")

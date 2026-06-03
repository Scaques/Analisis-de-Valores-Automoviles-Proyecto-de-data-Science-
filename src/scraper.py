import pandas as pd
import random
import os

def generar_mercado_autos_chile(num_registros=1000):
    """Genera un dataset simulado con imperfecciones reales del mercado chileno."""
    marcas_modelos = {
        "Suzuki": ["Swift", "Baleno", "Grand Vitara", "S-Cross"],
        "Toyota": ["Yaris", "Corolla", "RAV4", "Hilux"],
        "Hyundai": ["Accent", "i30", "Tucson", "Santa Fe"],
        "Chevrolet": ["Sail", "Onix", "Tracker", "Silverado"],
        "Kia": ["Rio", "Morning", "Sportage", "Sorento"],
        "Nissan": ["Versa", "Sentra", "Qashqai", "Kicks"]
    }
    
    datos = []
    
    for _ in range(num_registros):
        # 1. Seleccionar Marca y Modelo
        marca = random.choice(list(marcas_modelos.keys()))
        modelo = random.choice(marcas_modelos[marca])
        titulo = f"{marca} {modelo}"
        
        # Agregar variaciones de texto aleatorias (como pasa en la realidad)
        if random.random() < 0.15:
            titulo = titulo.upper()
        elif random.random() < 0.10:
            titulo = f"🔥 {titulo} IMPECABLE 🔥"
            
        # 2. Año (entre 2010 y 2025)
        ano = random.randint(2010, 2025)
        
        # 3. Kilometraje (coherente con el año)
        edad = 2026 - ano
        if edad == 0:
            km_base = random.randint(1000, 15000)
        else:
            km_base = edad * random.randint(12000, 18000)
        
        # Meter ruido en el formato del kilometraje
        if random.random() < 0.20:
            kilometraje = f"{km_base:,} kms".replace(",", ".")
        elif random.random() < 0.10:
            kilometraje = "No disponible" # Datos faltantes reales
        else:
            kilometraje = f"{km_base} Km"

        # 4. Precio (En pesos chilenos, afectado por año y km)
        precio_base = random.randint(8000000, 25000000)
        # Depreciación por edad y km
        precio_final = precio_base * (1 - (edad * 0.05)) * (1 - (km_base / 500000))
        precio_final = max(int(precio_final), 2500000) # Precio mínimo 2.5M
        
        # Formato sucio para el precio
        if random.random() < 0.15:
            precio = f"$ {precio_final:,}".replace(",", ".")
        elif random.random() < 0.10:
            precio = "No disponible"
        else:
            precio = str(precio_final)

        datos.append({
            "titulo": titulo,
            "precio": precio,
            "ano": str(ano) if random.random() > 0.05 else "No disponible",
            "kilometraje": kilometraje
        })
        
    return datos

def guardar_datos(lista_datos, ruta_salida="data/raw/autos_crudos.csv"):
    """Asegura la existencia de la carpeta y guarda el archivo CSV."""
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    df = pd.DataFrame(lista_datos)
    df.to_csv(ruta_salida, index=False, encoding='utf-8')
    print(f"\n[INFO] ¡Dataset generado exitosamente!")
    print(f"[INFO] Archivo creado en: {ruta_salida}")
    print(f"[INFO] Total de filas para procesar: {len(df)}")

if __name__ == "__main__":
    print("=== GENERANDO DATASET DE TRABAJO (MERCADO CHILE) ===")
    datos_autos = generar_mercado_autos_chile(1000)
    guardar_datos(datos_autos)
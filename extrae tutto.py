import os
import shutil

# Rutas de inicio y destino. PONER RUTA CORRECTA PARA QUITAR COMENTARIO Y EJECUTAR
#ruta_inicial = r"RUTA DE CARPETA CONTENEDORA"
#ruta_destino = r"RUTA NUEVA DE CARPETA"

# Crear la carpeta destino si no existe
os.makedirs(ruta_destino, exist_ok=True)

# Lista para guardar los archivos duplicados
archivos_duplicados = []

def mover_jpgs(ruta):
    for raiz, directorios, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.lower().endswith('.jpg'):
                ruta_completa = os.path.join(raiz, archivo)
                destino_completo = os.path.join(ruta_destino, archivo)

                # Verificar si el archivo ya existe en la carpeta de destino
                if os.path.exists(destino_completo):
                    archivos_duplicados.append((ruta_completa, destino_completo))
                else:
                    shutil.move(ruta_completa, destino_completo)

        # Imprimir mensaje después de procesar cada carpeta
        print(f"La carpeta {raiz} ha sido procesada.")

# Llamar a la función con la ruta inicial
mover_jpgs(ruta_inicial)

# Manejar archivos duplicados al final
if archivos_duplicados:
    print("Se encontraron archivos duplicados:")
    for i, (origen, destino) in enumerate(archivos_duplicados, 1):
        print(f"{i}. {os.path.basename(origen)}")

    respuesta = input("¿Deseas sobrescribir los archivos duplicados? (s/n): ").lower()
    if respuesta == 's':
        for origen, destino in archivos_duplicados:
            os.remove(destino)
            shutil.move(origen, destino)
        print("Los archivos duplicados han sido sobrescritos.")
    else:
        print("No se han sobrescrito los archivos duplicados.")
else:
    print("No se encontraron archivos duplicados.")

print("Todos los archivos JPG han sido procesados exitosamente.")


from pathlib import Path

# Nombre y apellido utilizados para renombrar los archivos
nombre_apellido = "daniela_agudelo"

# Obtener la ruta de la carpeta logs
carpeta_logs = Path(__file__).parent / "logs"

# Comprobar que la carpeta exista
if not carpeta_logs.is_dir():
    print("Error: no se encuentra la carpeta logs.")

else:

    # Filtrar los archivos con extension .log
    archivos_log = sorted(
        archivo
        for archivo in carpeta_logs.iterdir()
        if archivo.is_file()
        and archivo.suffix.lower() == ".log"
        and not archivo.stem.lower().startswith(f"{nombre_apellido}_")
    )



    # Preparar los nombres nuevos
    operaciones = [
        (archivo, carpeta_logs / f"{nombre_apellido}_{numero}.log")
        for numero, archivo in enumerate(archivos_log, start=1)
    ]

    # Comprobar que los nombres de destino no existan
    if any(destino.exists() for _, destino in operaciones):
        print("Error: ya existe uno de los nombres de destino.")

    elif not operaciones:
        print("No se encontraron archivos .log para renombrar.")

    else:
        # Mostrar los cambios que se realizaran
        for origen, destino in operaciones:
            print(f"{origen.name} -> {destino.name}")

        # Renombrar los archivos
        for origen, destino in operaciones:
            origen.rename(destino)

        print(f"\nProceso finalizado: {len(operaciones)} archivos renombrados.")

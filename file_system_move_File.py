import os

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print("Archivo renombrado correctamente.")
    except FileExistsError:
        print("El archivo nuevo ya existe.")
    except FileNotFoundError:
        print("El archivo a renombrar no existe.")

# Ruta y nombre del archivo original
old_file_path = "main.txt"

# Nuevo nombre del archivo
new_file_name = "hola.txt"

# Obtener la ruta del directorio del archivo original
directory = os.path.dirname(old_file_path)

# Obtener la ruta del nuevo archivo
new_file_path = os.path.join(directory, new_file_name)

# Renombrar el archivo
rename_file(old_file_path, new_file_path)
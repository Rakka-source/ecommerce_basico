# Dockerfile

# Usa una imagen base de Python Primero va nombre de la imagen : versión 3.13
FROM python:3.13-alpine

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de requisitos y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando para ejecutar Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]
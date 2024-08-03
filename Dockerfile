# Usa una imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el resto del código de la aplicación
COPY . /app

# Establece la variable de entorno PYTHONPATH
ENV PYTHONPATH=/app

# Expone el puerto de la aplicación
EXPOSE 5000

# Comando por defecto para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]

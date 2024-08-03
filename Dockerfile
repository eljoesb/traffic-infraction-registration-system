FROM python:3.10
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
ENV PYTHONPATH=/app
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

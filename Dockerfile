FROM python:3.9-slim

COPY u2net.onnx /root/.u2net/u2net.onnx

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5100

CMD ["python", "app.py"]

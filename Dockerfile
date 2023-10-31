FROM python:3.8.2

COPY product.py .

RUN pip install confluent-kafka

CMD ["python3", "product.py"]

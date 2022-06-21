#FROM arm64v8/python:3-alpine #для мака на м1
FROM python:3-alpine

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "mains.py" ]

EXPOSE 5001
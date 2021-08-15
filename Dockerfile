FROM python:3-slim
LABEL maintainer hamzaahmed12328@gmail.com
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python3"]
CMD ["bot.py"]

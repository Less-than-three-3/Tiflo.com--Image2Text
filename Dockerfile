FROM python:3.10-slim
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000
RUN echo "successfully installed"
CMD ["python", "server.py"]

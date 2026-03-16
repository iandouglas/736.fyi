FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN python build.py
CMD ["python", "-m", "http.server", "8000", "--directory", "public"]

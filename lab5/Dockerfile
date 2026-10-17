
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Run the application without root privileges
RUN useradd --no-create-home --uid 10001 appuser
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]

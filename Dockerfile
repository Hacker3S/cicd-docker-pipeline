# Use a slim, official Python base image to keep the image small
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file first (better layer caching - only reinstalls
# dependencies when requirements.txt actually changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Document the port the app listens on
EXPOSE 5000

# Default command to run when the container starts
CMD ["python", "app.py"]

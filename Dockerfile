# Use the official lightweight Python image.
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy local code to the container image.
COPY . /app

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Use uvicorn to run the app
# Listening on all network interfaces with port 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

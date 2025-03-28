# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variables
ENV TELEGRAM_BOT_TOKEN=7862392572:AAHOXE4hFk8qwNW-wyezk8H0W6d8LpmLXxo
ENV TELEGRAM_CHANNEL_ID=-1002527492866
ENV FILTER_MIN_PRICE=0
ENV FILTER_MAX_PRICE=15000000
ENV FILTER_DISTRICT='Praha 6'

# Run bot.py when the container launches
CMD ["python", "bot.py"]
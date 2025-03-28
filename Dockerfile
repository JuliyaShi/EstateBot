# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variables
ENV TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
ENV TELEGRAM_CHANNEL_ID=${TELEGRAM_CHANNEL_ID}
ENV FILTER_MIN_PRICE=${FILTER_MIN_PRICE}
ENV FILTER_MAX_PRICE=${FILTER_MAX_PRICE}
ENV FILTER_DISTRICT=${FILTER_DISTRICT}

# Run bot.py when the container launches
CMD ["python", "bot.py"]
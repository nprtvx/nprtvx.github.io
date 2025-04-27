# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application requirements to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port your application runs on
EXPOSE 1269

# Set the environment variable for production
ENV FLASK_ENV=production

# Command to run the application
# Replace 'app.py' with the entry point of your application
CMD ["python", "app.py"]

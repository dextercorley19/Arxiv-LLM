# Use the official Selenium standalone Chrome image
FROM selenium/standalone-chrome:4.0.0

# Switch to the root user to install packages
USER root

# Update package lists and install python3 and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev build-essential

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Switch back to the default Selenium user
USER seluser

# Copy your application files into the container
COPY . .

# Set environment variables for FastAPI
ENV PYTHONUNBUFFERED=1

# Expose the FastAPI port (default is 8000)
EXPOSE 8000

# Command to run your FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# Use Python 3.12 as the base image
FROM python:3.12.5-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Run Gunicorn as the WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "120", "mini_tweetapp.wsgi:application"]



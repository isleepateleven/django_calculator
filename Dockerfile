# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file first to leverage Docker caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY src/ /app/

# Expose the port the Django app will run on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Commands:
# docker build -t isleepateleven/django-calculator .
# docker run -p 8000:8000 isleepateleven/django-calculator
# test this in browser: http://localhost:8000

# docker push isleepateleven/django-calculator 
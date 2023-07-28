# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY app.py .
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Flask app will run (change it to your desired port)
EXPOSE 5000

# Set the environment variable for Flask (change "app.py" to the filename of your Flask app)
ENV FLASK_APP=app.py

# Run the Flask application inside the container
CMD ["flask", "run", "--host=0.0.0.0"]

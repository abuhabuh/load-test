FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY app.py .

# Install any necessary dependencies (if you have a requirements.txt, uncomment the next line)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
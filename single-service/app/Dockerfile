FROM python:3.12

# Create the /app directory and set it as the working directory
RUN mkdir -p /app
WORKDIR /app

# Copy the application code
COPY app-config /app/app-config
COPY app-source /app/app-source

# Install any necessary dependencies (if you have a requirements.txt, uncomment the next line)
RUN pip install --no-cache-dir -r app-config/requirements.txt

# Expose the port the app runs on
EXPOSE 5000
EXPOSE 9191

# Command to run the application
# - Moved command to docker-compose.yml so `--listen` option is next to OS
#   setting
# CMD ["uwsgi", \
#     "--http", ":5000", \
#     "--wsgi-file", "app.py", \
#     "--callable", "app", \
#     "--master", \
#     "--processes", "1", \
#     "--threads", "1", \
#     "--py-autoreload", "1", \
#     "--listen", "10", \
#     ]
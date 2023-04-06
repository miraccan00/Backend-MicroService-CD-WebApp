FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app
# Copy application code
COPY . .
RUN pip install --user --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver"]

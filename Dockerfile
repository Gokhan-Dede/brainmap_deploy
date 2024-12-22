# Use a specific base Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY brainmap_app /app/brainmap_app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "brainmap_app.api.fast:app", "--host", "0.0.0.0", "--port", "8000"]

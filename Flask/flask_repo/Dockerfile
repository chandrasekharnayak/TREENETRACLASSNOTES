# Step 1: Use an official Python runtime as a parent image
FROM python:3.-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY api_webapp /app

# Step 4: Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Make port 80 available to the world outside this container
EXPOSE 80

# Step 6: Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Step 7: Run the Flask application when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
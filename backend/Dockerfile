# Use a slim version of the Python image
FROM python:3.11.4-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Ensure Python output is sent directly to the terminal without buffering
ENV PYTHONBUFFERED 1

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Copy and install dependencies before copying the entire app to leverage Docker cache
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint script and grant execute permissions
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy the application files
COPY . /usr/src/app/

# Specify the default command to run on container startup
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

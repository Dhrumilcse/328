# Python docker image
FROM python:3.9.4-buster

# Work directory
WORKDIR /Users/dhrumil/Documents/Projects/shopify-challenge/shop

# Env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies 
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy entrypoint.sh
COPY ./entrypoint.sh .

# Copy project
COPY . .
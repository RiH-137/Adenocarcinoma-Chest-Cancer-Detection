## using a more recent slim image based on Debian Bookworm
FROM python:3.12-slim

# working directory
WORKDIR /app

## Installing system dependencies (awscli and updates)
RUN apt-get update -y && \
    apt-get install -y awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Coping project files
COPY . /app

# Installing Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default Streamlit port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
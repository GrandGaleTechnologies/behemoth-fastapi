FROM python:3.12

ENV PYTHONUNBUFFERED=1

# Install curl for downloading uv and bash for script
RUN apt-get update && apt-get install -y curl bash \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install uv (standalone binary)
RUN curl -LsSf https://astral.sh/uv/install.sh | bash

ENV PATH="/root/.cargo/bin:/root/.local/bin:$PATH"

WORKDIR /app

COPY . /app

# Use uv to install deps
RUN uv pip install -r requirements.txt

# Optional: Install uvloop only if on Linux (already here)
RUN uv pip install uvloop

# Entrypoint to shell script
CMD ["/bin/bash", "/app/start.sh"]

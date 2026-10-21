# Use an official Python image as the base, named by digest so the content cannot change under the tag
FROM python:3.11.17-slim@sha256:e88e9763f943ec1834f992a4b51e0f24500486803e8bc534e5767af9ea65f6ce

# uv installs exactly what uv.lock names, checking each file's hash
COPY --from=ghcr.io/astral-sh/uv:0.13.1@sha256:4a1f3666816dafadd20ceb71eac9a7d56d7ef30279f7d64048519ab901ada336 /uv /bin/uv

# Set working directory inside the container
WORKDIR /app

# Install system dependencies (optional: needed for pip or grpc)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Use the image's Python, never a downloaded one
ENV UV_PYTHON_DOWNLOADS=never

# Install Python dependencies from the lock. setuptools goes in first, because dlx is built
# from source with the locked setuptools rather than one fetched at build time.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache --no-install-package dlx \
    && uv sync --frozen --no-cache

# Copy the rest of the application
COPY . .

ENV PYTHONPATH=/app
ENV PATH="/app/.venv/bin:$PATH"

# Expose the gRPC server port (e.g., 50051)
EXPOSE 50051

# Define the default command to run your server
CMD ["python", "calendar_solver/server/grpc_server.py"]

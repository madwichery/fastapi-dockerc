# FROM ghcr.io/astral-sh/uv:debian

# WORKDIR /app

# COPY . .

# RUN uv sync

# EXPOSE 8000

# ENV PYTHONPATH=/app

# CMD ["sh", "-c", "uv run alembic upgrade head && PYTHONPATH=/app uv run uvicorn app.main:app --host 0.0.0.0 --port 8000"]

FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync

COPY . .

EXPOSE 8000

CMD ["./bin/start.sh"]
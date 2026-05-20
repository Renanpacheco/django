FROM python:3.12-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dependências para compilação
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    musl-dev

WORKDIR /app

# Copia requirements primeiro para cache
COPY django/src/requirements.txt .

# Instala dependências
RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt

# =========================
# STAGE 2 - RUNTIME
# =========================
FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Usuário não-root
RUN addgroup -S django && adduser -S django -G django

# Dependências mínimas
RUN apk add --no-cache \
    libffi \
    bash \
    wget

WORKDIR /app

# Copia libs instaladas
COPY --from=builder /install /usr/local

# Copia projeto
COPY django/src /app
COPY docker /app/docker

# Permissões
RUN chown -R django:django /app

USER django

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD sh /app/docker/healthcheck.sh

ENTRYPOINT ["sh", "/app/docker/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
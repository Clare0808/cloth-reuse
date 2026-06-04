FROM node:20-slim AS frontend-builder

WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM python:3.11-slim

WORKDIR /app
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

COPY --from=frontend-builder /app/backend ./backend
COPY --from=frontend-builder /app/upload ./upload

ENV PORT=10000
EXPOSE 10000

CMD ["sh", "-c", "gunicorn -w 1 --threads 100 --chdir backend app:app --bind 0.0.0.0:${PORT}"]

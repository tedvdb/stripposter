FROM python:3-alpine
COPY stripbot /app
CMD [ "python", "/app/update-continuous" ]

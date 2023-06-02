FROM python:3-alpine
COPY . /app
RUN pip install -r /app/requirements.txt --no-cache-dir
CMD [ "python", "/app/update-continuous" ]

FROM python:3-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt --no-cache-dir
VOLUME /app/states
CMD [ "python", "update-continuous" ]

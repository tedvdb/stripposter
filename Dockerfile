FROM python:3-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt --no-cache-dir
VOLUME /app/states
ENV PYTHONUNBUFFERED=1
CMD [ "python", "update-continuous" ]

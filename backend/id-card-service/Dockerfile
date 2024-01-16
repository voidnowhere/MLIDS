FROM python:3.7.9

RUN apt-get update \
    && apt-get install -y tesseract-ocr libgl1-mesa-glx

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:80", "api:app"]
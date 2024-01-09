FROM python:3.7.9

RUN apt-get update \
    && apt-get install -y tesseract-ocr libgl1-mesa-glx

ENTRYPOINT ["sh", "-c", "pip install -r requirements.txt && python -m flask --app api.py run --host=0.0.0.0"]
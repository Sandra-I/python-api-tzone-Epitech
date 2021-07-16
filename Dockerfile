FROM python:3.9.1
RUN apt-get update
RUN apt-get -y install tesseract-ocr
RUN apt-get install tesseract-ocr-eng
ADD . /tesseract-python
WORKDIR /tesseract-python
RUN pip install -r requirements.txt
EXPOSE 8080
FROM python:3.6-alpine
WORKDIR /app
ADD code.py .
ADD requirements .
RUN pip3 install -r requirements
CMD python code.py

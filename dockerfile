FROM python:2.7
WORKDIR /app
RUN apt-get update && apt-get install -y libgraphicsmagick++1-dev libboost-python-dev
ADD app/* ./
RUN pip install --upgrade -r requirements
CMD python code.py
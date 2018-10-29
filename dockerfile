FROM parkayun/ubuntu-11.04
WORKDIR /app
RUN apt-get -y update
#RUN apt-get install -y --fix-missing     build-essential     cmake     gfortran     git     wget     curl     graphicsmagick     libgraphicsmagick1-dev     libatlas-dev     libavcodec-dev     libavformat-dev     libgtk2.0-dev     libjpeg-dev     liblapack-dev     libswscale-dev     pkg-config     python3-dev     python3-numpy     software-properties-common     zip && apt-get clean && rm -rf /tmp/* /var/tmp/*
RUN apt-get install -y libgraphicsmagick++1-dev libboost-python-dev python-pip python python-pgmagick
ADD code.py .
ADD requirements .
# RUN pip3 install -r requirements
CMD python code.py

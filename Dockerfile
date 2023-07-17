FROM python:3.11

#non buffered mode
ENV PYTHONUNBUFFERED 1 

#copying all the code into docker directory
COPY ./ /clothstore/

#set workdir
WORKDIR /clothstore

RUN pip install -r requirements.txt

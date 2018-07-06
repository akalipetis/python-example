FROM python:3.6
# /code/requirements.txt -> requirements
ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
ADD . /code
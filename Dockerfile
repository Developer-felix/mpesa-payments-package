FROM python:3.9

RUN pip3 install --upgrade pip

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

RUN mkdir /app
WORKDIR /app

COPY . /app

WORKDIR /app
CMD python3 setup.py 
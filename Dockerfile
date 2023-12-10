FROM tiangolo/uvicorn-gunicorn:python3.11

RUN mkdir /crypto-bert

COPY requirements.txt /crypto-bert

WORKDIR /crypto-bert

RUN pip install -r requirements.txt
RUN rm -r /root/.cache
RUN apt-get -y clean
RUN apt-get -y autoremove

COPY . /crypto-bert

EXPOSE 8001

#uvicorn api:app --host 0.0.0.0 --port 8001
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8001"]

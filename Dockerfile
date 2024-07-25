FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "7000", "main:app"]

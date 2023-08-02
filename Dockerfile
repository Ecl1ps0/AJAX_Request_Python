FROM python:3

WORKDIR /main

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./main ./main

CMD ["python", "./main/main.py"]
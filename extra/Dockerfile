FROM Python:latest

COPY main.py bd.json requirements.txt /

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
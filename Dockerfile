FROM python:3.10-slim

WORKDIR /app

COPY . .

ENV TARGET_URL=https://amrita.edu/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python3","scrapper.py"]
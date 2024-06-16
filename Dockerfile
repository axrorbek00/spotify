FROM python:3.7


WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
# entrypoint.sh file dagi kamandalarni yurgizadi
FROM python:3.11

RUN mkdir /app
RUN groupadd app -g 10000
RUN useradd app -d /app -u 10000 -g 10000
RUN chown app:app /app
USER app
WORKDIR /app
COPY main.py /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3","/app/main.py"]

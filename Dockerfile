FROM python:3.11

RUN pip install gunicorn

RUN mkdir /app
RUN groupadd app -g 10000
RUN useradd app -d /app -u 10000 -g 10000
RUN chown app:app /app
USER app
WORKDIR /app
COPY configs/ /app/configs/
COPY main.py /app/
RUN ls -alh /app/
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--conf", "configs/gunicorn.py", "--bind", "0.0.0.0:5000", "main:_api"]

FROM python:3.9.6

WORKDIR /usr/src/app

COPY . .
RUN pip install -r requirements.txt
RUN pip install .

CMD ["gunicorn","cutiesound:app","-c","./gunicorn.conf.py"]
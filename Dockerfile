FROM python:3

WORKDIR /usr/src/app

COPY main_thread.py .
COPY sss.py .
ENTRYPOINT ["python3", "main_thread.py"] 

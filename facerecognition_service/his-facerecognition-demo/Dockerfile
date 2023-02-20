FROM tiangolo/uvicorn-gunicorn:python3.8
COPY requirements.txt /tmp/requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY ./server /app
CMD ["/start-reload.sh"]
# CMD uvicorn main:app --host 0.0.0.0 --port 80 --reload


FROM python:3.10-slim
WORKDIR /api
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
# CMD ["./entrypoint.sh"]
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
CMD uvicorn app:app --host 0.0.0.0 --port $PORT
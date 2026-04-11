#Build Application
FROM python:3.12
WORKDIR /app

#install backend depedencies
COPY requirements.txt .
RUN pip install  --no-cache-dir -r requirements.txt

#copy source code frontend + backend
COPY . .

ENV PYTHONBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
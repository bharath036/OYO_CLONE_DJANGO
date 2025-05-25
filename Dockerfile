FROM python:latest 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# 🛠 Install netcat (required for DB wait logic)
#RUN apt-get update && apt-get install -y netcat
# Install netcat correctly
RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

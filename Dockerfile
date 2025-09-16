FROM python:3.9


WORKDIR /code


COPY ./requirements.txt .


RUN pip install --no-cache-dir --upgrade -r ./requirements.txt


COPY ./core .


CMD ["fastapi", "run", "./main.py", "--port", "80"]
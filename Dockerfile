FROM python:3.9.0

#FROM python:3.9-alpine3.13

LABEL maintainer="BuildApp"
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
COPY . /app

WORKDIR /app
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # apk add --update --no-cache postgresql-client && \
    # apk add --update --no-cache --virtual .tmp-deps \
    #     build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    # apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app

ENV PATH="/py/bin:$PATH"

WORKDIR /app

RUN ls -ltr
# RUN PWD
# CMD [ "python manage.py runserver" ]

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]


# # set work directory
# WORKDIR /usr/src/app

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # install dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# # copy project
# COPY . .
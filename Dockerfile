# Base Image
FROM python:3.10

# create and set working directory
RUN mkdir /app
WORKDIR /app

# install environment dependencies
COPY ./requirements.txt /app/requirements.txt
COPY ./requirements-dev.txt /app/requirements-dev.txt
RUN pip install --upgrade pip
ARG REQUIREMENTS=requirements.txt
RUN pip install -r ${REQUIREMENTS}

# Add current directory code to working directory
ADD . /app

EXPOSE 28332
EXPOSE 28333

CMD ["python main.py"]

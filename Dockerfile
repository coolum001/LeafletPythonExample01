#  get python
FROM python:3.6-slim

# set working directory to /app
WORKDIR /app

# copy current directory to container at /app
COPY . /app

# install packages
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# make port 80 avaiable 
EXPOSE 80

# define env var
ENV NAME World

# run app.py inside container on launch
CMD ["python", "app.py"]
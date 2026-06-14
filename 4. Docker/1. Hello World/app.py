## flask app for hello world

from flask import Flask


app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World"


'''
    "0.0.0.0"---> can access your local address and your local host address both
    http://localhost:5000/
    http://localhost:5000/
    http://192.168.1.7:5000/

'''
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)

'''
# Use a Docker image that contains Python 3.7 on top of a Linux OS
FROM python:3.7

# Copy all files from the current directory on the host into /app in the container
COPY . /app

# Set /app as the working directory for subsequent commands
WORKDIR /app

# Install dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container starts
CMD ["python", "app.py"]

'''

### Docker file to install ubantu as bas os then install javA AND PYTHON
'''

FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip openjdk-17-jdk

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
'''
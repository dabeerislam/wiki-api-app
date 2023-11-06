FROM amazonlinux:latest
RUN yum -y update && yum -y install python3 python3-pip
ADD . /app
WORKDIR /app
RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip install Flask && pip install Flask requests
EXPOSE 80 443 5000
CMD ["python3", "grow-app.py"]

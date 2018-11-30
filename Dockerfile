# this is an official Python runtime, used as the parent image
FROM python:3.7.1-slim
# Responsible person
LABEL maintainer="dimakievua@gmail.com"
# Argument to control what script to install
ARG ENV
ARG BUILD_DATE
ARG VCS_REF
ARG BUILD_VERSION
# Set one or more individual labels
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.name="sysinfo"
LABEL org.label-schema.version=$BUILD_VERSION
LABEL org.label-schema.description="Python Flask API Example"
LABEL org.label-schema.vcs-url="https://github.com/dimakievua/python-sysinfo-api"
LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.docker.cmd="docker run -it -v htmlcov:/app/htmlcov --entrypoint 'bash -c' ${IMG} 'coverage run -m pytest && coverage html'"
# set the working directory in the container to /app
WORKDIR /app
# Set ENV variable
ENV ENV=$ENV
# add the current directory to the container as /app
ADD . /app
# execute everyone's favorite pip command, pip install -r
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/* \
    && python3 -m venv venv && . venv/bin/activate && pip install -e . \
    && pip install --trusted-host pypi.python.org -r requirment-${ENV}.txt
# expose port 80 for the Flask app to run on
EXPOSE 5000
# define entypoint
ENTRYPOINT ["bash"]
# execute the Flask app
CMD ["-c"]

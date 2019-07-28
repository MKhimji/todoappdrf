FROM python:3.6.6-alpine3.7

LABEL maintainer="Muhammad Khimji"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Path for COPY, RUN etc to be run
WORKDIR /app
#Copy files from current directory(where the dockerfile lives) into /app folder in container(running Alpine Linux)
COPY . /app

RUN addgroup -g 1000 -S m && adduser -u 1000 -S m -G m /bin/bash

RUN chown -R m /app
RUN chmod -R u+rX /app


RUN apk --no-cache add shadow \
                       build-base \
                       # dev dependencies
                       sudo \
                       bash \
                       vim \
                       git \
                       tmux 

RUN git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
RUN sh ~/.vim_runtime/install_awesome_vimrc.sh
 
CMD [ "bash" ] 












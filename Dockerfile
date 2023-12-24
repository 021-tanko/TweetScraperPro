FROM python:3.6-buster
LABEL maintainer="aisynclab@gmail.com"

WORKDIR /root

RUN git clone --depth=1 https://github.com/021-tanko/tweetscraperpro.git && \
	cd /root/tweetscraperpro && \
	pip3 install . -r requirements.txt

CMD /bin/bash

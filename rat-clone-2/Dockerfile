FROM debian:bookworm-slim AS base

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    socat

RUN mkdir /challenge && chmod 700 /challenge

COPY cheese_list.txt challenge.py setup-challenge.py /app/
COPY start.sh /opt/
RUN chmod +x /opt/start.sh

WORKDIR /app/
RUN tar czvf /challenge/artifacts.tar.gz challenge.py

FROM base AS challenge
ARG FLAG

RUN python3 setup-challenge.py

# The start.sh script starts a socat listener on port 5555, that connects to the
# python script.
EXPOSE 5555
# PUBLISH 5555 AS socat
CMD ["/opt/start.sh"]

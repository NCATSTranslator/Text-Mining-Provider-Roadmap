FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    jq \
    wget \
    curl

WORKDIR /home/dev
# install bash_unit
RUN wget -O - https://raw.githubusercontent.com/pgrange/bash_unit/master/install.sh | bash

COPY entrypoint.sh /home/dev/
RUN chmod 755 /home/dev/entrypoint.sh

COPY tests /home/dev/tests/

ENV TEXT_MINED_TRAPI_URL https://api.bte.ncats.io/v1/smartapi/978fe380a147a8641caf72320862697b/query/
ENV COOCCUR_TRAPI_URL https://api.bte.ncats.io/v1/smartapi/5be0f321a829792e934545998b9c6afe/query/

ENTRYPOINT [ "/home/dev/entrypoint.sh" ]



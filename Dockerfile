ARG BUILD_FROM
FROM ${BUILD_FROM}

LABEL \
    io.hass.type="addon" \
    io.hass.version="1.0.0" \
    io.hass.name="GeoServer"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

#--------------------------------------------------
# Install packages
#--------------------------------------------------

RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-setuptools \
    py3-wheel \
    bash

#--------------------------------------------------
# Working directory
#--------------------------------------------------

WORKDIR /app

#--------------------------------------------------
# Install Python packages
#--------------------------------------------------

COPY requirements.txt .

RUN pip3 install --no-cache-dir \
    -r requirements.txt

#--------------------------------------------------
# Copy application
#--------------------------------------------------

COPY app/ /app/

COPY run.sh /run.sh

RUN chmod +x /run.sh

EXPOSE 8099

CMD ["/run.sh"]
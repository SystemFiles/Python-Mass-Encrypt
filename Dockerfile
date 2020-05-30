FROM python:2.7-alpine3.11

LABEL author="Ben Sykes"
LABEL email="bensykes12@gmail.com"

WORKDIR /cryware2
COPY . .
RUN apk add --update --no-cache build-base
RUN pip install -r requirments.txt

# Execute the payload
CMD [ "python", "cryware2.py" ]
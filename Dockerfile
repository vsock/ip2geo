FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD ip2geo.py /
ENTRYPOINT  [ "python3", "ip2geo.py" ]

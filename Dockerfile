FROM python:3.9-alpine

WORKDIR /code
RUN pip install requests
COPY update_dns.py /code/

ENTRYPOINT ["python", "/code/update_dns.py"]
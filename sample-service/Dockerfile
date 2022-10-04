FROM python:3.10-alpine

WORKDIR /var/app

ENV ENABLE_METRICS=true

RUN adduser --system --no-create-home --uid 1001 lenny_kravitz

COPY ./requirements.txt /var/app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /var/app/requirements.txt

COPY ./app /var/app/app

USER lenny_kravitz

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

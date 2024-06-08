FROM python:3.11.6  AS build_stage_1

ENV PORT 8080

WORKDIR /dockerworkdir

COPY ./requirements.txt /dockerworkdir/requirements.txt

RUN pip install --no-cache-dir -r /dockerworkdir/requirements.txt

COPY . /dockerworkdir

ENV PYTHONPATH "$PYTHONPATH:/dockerworkdir/app"

CMD ["python", "run.py"]
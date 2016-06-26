FROM python:3.5
MAINTAINER Manu Phatak <bionikspoon@gmail.com>
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["/usr/bin/env", "python", "/code/manage.py"]
CMD ["runserver", "0.0.0.0:5000"]

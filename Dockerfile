FROM python:3.6.1
ADD main.py /
RUN pip3 install requests
CMD [ "python3", "./main.py" ]

FROM python:3.9
LABEL developed_by='@LeoAlecksey'
WORKDIR /usr/src/app
ENV TOKEN= # token
ENV OFFICE= # Group_id
ENV IT_ADM= # Group_id
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
RUN mkdir ./files
COPY ./main.py .
COPY ./button.py .
COPY ./LICENCE.md .
COPY ./blank/Blank.docx ./blank/Blank.docx
COPY ./.env .
COPY ./.gitignore .
CMD ["python", "./main.py"]
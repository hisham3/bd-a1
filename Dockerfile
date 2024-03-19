FROM ubuntu

RUN apt update -y
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy openpyxl

WORKDIR /home/doc-bd-a1/

COPY ./economic_freedom_index2019_data.xlsx ./
COPY ./load.py ./
COPY ./dpre.py ./
COPY ./eda.py ./
COPY ./vis.py ./
COPY ./model.py ./

CMD ["python3", "load.py", "./economic_freedom_index2019_data.xlsx"]
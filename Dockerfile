FROM jupyter/scipy-notebook


RUN pip install joblib

COPY requirements.txt ./requirements.txt
pip install -r requirements.txt

COPY ECG_ALL_Data.txt ./ECG_ALL_Data.txt
COPY train.py ./train.py
COPY test.py ./test.py

RUN python3 train.py

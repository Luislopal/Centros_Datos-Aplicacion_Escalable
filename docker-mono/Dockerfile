FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3-pip build-essential git
RUN git clone "https://github.com/CDPS-ETSIT/practica_creativa2.git"
ENV GROUP_NUMBER="17"
WORKDIR practica_creativa2
EXPOSE 9080
WORKDIR "./bookinfo/src/productpage"
RUN pip3 install -r ./requirements.txt
WORKDIR "./templates"
ADD groupNumber.py .
RUN python3 groupNumber.py
WORKDIR ".."
CMD ["python3", "productpage_monolith.py", "9080"]
#RUN python3 productpage_monolith.py 9080


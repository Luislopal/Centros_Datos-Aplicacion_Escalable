FROM node:12.18.1-slim
RUN apt-get update
RUN apt-get install -y git
RUN mkdir /opt/microservices
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
WORKDIR "practica_creativa2/bookinfo/src/ratings/"
RUN cp package.json /opt/microservices/
RUN cp ratings.js /opt/microservices/
EXPOSE 9080
WORKDIR "/opt/microservices"
RUN npm install
CMD ["node", "ratings.js", "9080"]
#RUN python3 productpage_monolith.py 9080

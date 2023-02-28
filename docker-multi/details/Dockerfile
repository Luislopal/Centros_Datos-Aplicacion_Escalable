FROM ruby:2.7.5
WORKDIR "/"
RUN apt-get install  git
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
RUN mkdir /opt/microservices
ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true
RUN cp practica_creativa2/bookinfo/src/details/details.rb /opt/microservices
EXPOSE 9080
WORKDIR "/opt/microservices"
CMD ["ruby", "details.rb", "9080"]

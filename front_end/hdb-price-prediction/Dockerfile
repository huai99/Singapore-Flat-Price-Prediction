# base image
FROM node:9.6.1 AS builder

# set working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /usr/src/app/package.json
RUN npm install 

COPY . /usr/src/app
RUN ng build --prod --aot --deployUrl=/hdb-flat-price-predictor/ --baseHref=/hdb-flat-price-predictor/


FROM nginx:alpine

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /usr/src/app/dist/* /usr/share/nginx/html/

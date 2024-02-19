FROM node:20.10.0-alpine

WORKDIR /functions

COPY ./functions .
COPY .firebaserc .
COPY firebase.json .

RUN apk update && \
    apk add --no-cache openjdk21

RUN npm ci

CMD npm run emu

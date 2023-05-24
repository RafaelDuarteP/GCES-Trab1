FROM node:latest

WORKDIR /front

COPY package.json .
COPY package-lock.json .

RUN npm install
RUN npm install react-scripts

COPY . .

CMD [ "npm", "start" ]
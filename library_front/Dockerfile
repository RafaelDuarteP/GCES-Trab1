FROM node:14.17.6

WORKDIR /app

COPY . .

RUN npm cache clean --force
RUN npm install
RUN npm install react-scripts

EXPOSE 3000

CMD [ "npm", "start" ]
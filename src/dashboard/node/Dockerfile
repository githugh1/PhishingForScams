FROM node:slim

WORKDIR /home/node/app

COPY client/package.json .
COPY client/package-lock.json .

RUN npm install

COPY . .

EXPOSE 80

CMD ["npm", "start"]
node:
    image: "node:slim"
    container_name: frontend
    user: "node"
    working_dir: /home/node/app
    environment:
      - NODE_ENV=production
    volumes:
      - ./src/dashboard/node/app:/home/node/app:ro  # read only!
    ports:
      - "80:8081"
    command: "npm start"
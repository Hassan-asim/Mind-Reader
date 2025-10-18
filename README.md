# Mind Reader Game

![Mind Reader Game](1.png)

A simple, fun, and interactive web-based game where the computer tries to read your mind! This project is containerized using Docker for easy setup and deployment.

## Features

- _Interactive Gameplay:_ Think of something, and the computer will make a guess.
- _Simple User Interface:_ A clean and minimalist UI built with Next.js and Tailwind CSS.
- _Containerized:_ The entire application is containerized using Docker, making it easy to run on any machine.
- _Scalable Backend:_ A simple Node.js and Express backend that can be easily extended.

## Tech Stack

- _Frontend:_
  - [Next.js](https://nextjs.org/) - A React framework for building user interfaces.
  - [React](https://reactjs.org/) - A JavaScript library for building user interfaces.
  - [Tailwind CSS](https://tailwindcss.com/) - A utility-first CSS framework.
- _Backend:_
  - [Node.js](https://nodejs.org/) - A JavaScript runtime built on Chrome's V8 JavaScript engine.
  - [Express](https://expressjs.com/) - A minimal and flexible Node.js web application framework.
- _Containerization:_
  - [Docker](https://www.docker.com/) - A platform for developing, shipping, and running applications in containers.
  - [Docker Compose](https://docs.docker.com/compose/) - A tool for defining and running multi-container Docker applications.

## Project Structure

mind-reader-game/
├── backend/
│ ├── Dockerfile
│ ├── package.json
│ └── server.js
├── frontend/
│ ├── Dockerfile
│ ├── next.config.js
│ ├── package.json
│ ├── src/
│ └── ...
├── docker-compose.yml
└── README.md

- **backend/**: Contains the Node.js and Express backend server.
- **frontend/**: Contains the Next.js and React frontend application.
- **docker-compose.yml**: The Docker Compose file for orchestrating the frontend and backend containers.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.

### Installation and Running the Application

1.  _Clone the repository:_

    bash
    git clone https://github.com/your-username/mind-reader-game.git
    cd mind-reader-game

2.  _Run the application using Docker Compose:_

    bash
    docker-compose up

    This command will build the Docker images for the frontend and backend and start the containers.

3.  _Access the application:_

    Open your web browser and navigate to [http://localhost:3000](http://localhost:3000).

## Docker Integration

This project is fully containerized using Docker, which simplifies the setup and deployment process.

### Backend Dockerfile

The backend/Dockerfile is responsible for creating the Docker image for the backend server.

dockerfile
FROM node:18

WORKDIR /app

COPY package\*.json ./

RUN npm install

COPY . .

EXPOSE 3001

CMD ["node", "server.js"]

- **FROM node:18**: Specifies the base image to be Node.js version 18.
- **WORKDIR /app**: Sets the working directory inside the container to /app.
- **COPY package\*.json ./**: Copies the package.json and package-lock.json files to the container.
- **RUN npm install**: Installs the backend dependencies.
- **COPY . .**: Copies the rest of the backend source code to the container.
- **EXPOSE 3001**: Exposes port 3001 from the container.
- **CMD ["node", "server.js"]**: The command to run when the container starts.

### Frontend Dockerfile

The frontend/Dockerfile is responsible for creating the Docker image for the frontend application.

dockerfile
FROM node:18

WORKDIR /app

COPY package\*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]

- **FROM node:18**: Specifies the base image to be Node.js version 18.
- **WORKDIR /app**: Sets the working directory inside the container to /app.
- **COPY package\*.json ./**: Copies the package.json and package-lock.json files to the container.
- **RUN npm install**: Installs the frontend dependencies.
- **COPY . .**: Copies the rest of the frontend source code to the container.
- **EXPOSE 3000**: Exposes port 3000 from the container.
- **CMD ["npm", "run", "dev"]**: The command to run when the container starts.

### Docker Compose

The docker-compose.yml file defines and orchestrates the multi-container application.

yaml
version: '3.8'
services:
backend:
build: ./backend
ports: - "3001:3001"
frontend:
build: ./frontend
ports: - "3000:3000"
depends_on: - backend

- **services**: Defines the services (containers) to be run.
- **backend**: The backend service.
  - **build: ./backend**: Specifies that the Docker image for this service should be built from the backend directory.
  - **ports: - "3001:3001"**: Maps port 3001 on the host to port 3001 in the container.
- **frontend**: The frontend service.
  - **build: ./frontend**: Specifies that the Docker image for this service should be built from the frontend directory.
  - **ports: - "3000:3000"**: Maps port 3000 on the host to port 3000 in the container.
  - **depends_on: - backend**: Specifies that the frontend service depends on the backend service. This ensures that the backend container starts before the frontend container.

## API Endpoints

### GET /api/guess

- _Description:_ Gets a random guess from the backend.
- _Response:_ A JSON object with a guess property.

  json
  {
  "guess": "a warm, sandy beach."
  }

## Workflow Diagram

mermaid
graph TD
A[User clicks "I'm ready! Guess!"] --> B{Frontend};
B --> C{Backend API};
C --> D[Generate random guess];
D --> C;
C --> B;
B --> E[Display guess to user];

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

1.  Fork the repository.
2.  Create a new branch (git checkout -b feature/your-feature).
3.  Make your changes.
4.  Commit your changes (git commit -m 'Add some feature').
5.  Push to the branch (git push origin feature/your-feature).
6.  Open a pull request.

## License

This project is licensed under the MIT License.

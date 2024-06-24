## Getting Started

These instructions will get your API up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

- [Docker Installation Guide](https://docs.docker.com/get-docker/)
- [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone git@github.com:obdul404/xmart.git
cd xmart
```

### Environment Variables

Create a `.env` file in the `app` directory. You can use the provided `.env.sample` file as a template.

```bash
cp app/.env.sample app/.env
```

Edit the `app/.env` file to match your environment settings.

### Running the Application

Use Docker Compose to build and run the application:

```bash
docker-compose up --build
```

This command will build the Docker images and start the services defined in the `docker-compose.yml` file.

### Accessing the Application

Once the application is running, you can access it at:

```
http://localhost:8000
```

### Stopping the Application

To stop the application, use:

```bash
docker-compose down
```

## Project Structure

Here is an overview of the project structure:

```
your-repo-name/
│
├── app/
│   ├── .env
│   ├── .env.sample
│   ├── Dockerfile
│   ├── app
│   └── ...
│
├── docker-compose.yml
├── README.md
└── ...
```

- `app/`: Contains the FastAPI application code and the Dockerfile.
- `docker-compose.yml`: Defines the services for the application, including the API and PostgreSQL database.
- `.env.sample`: Sample environment variables file.

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework for building APIs with Python 3.6+ based on standard Python type hints.
- [Uvicorn](https://www.uvicorn.org/) - A lightning-fast ASGI server implementation, using `uvloop` and `httptools`.
- [Docker](https://www.docker.com/) - Container platform for developing, shipping, and running applications.
- [Docker Compose](https://docs.docker.com/compose/) - A tool for defining and running multi-container Docker applications.

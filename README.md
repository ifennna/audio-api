# Audio file server

A REST API that emulates an audio file server

## Requirements

- Python 3
- Docker
- Docker compose
- GNUMake/BSDMake (Optional)


## Setting up

- Start the database: `make db`

- Run migrations: `make migration`

- Start the server: `make run`

The server should be running on `localhost:5000`.
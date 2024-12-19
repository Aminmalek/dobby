# Dobby Project
![a character in harry potter movie](https://domnardireviews.wordpress.com/wp-content/uploads/2015/05/1294516396126_f.jpg)
## Project Overview

This project consists of three services and kafka ui:

1. **Kafka Producer Daemon**: A service that fetches data from an external API (`https://fakerapi.it/api/v2/texts?_quantity=100&_locale=fa_IR`) every minute, processes the received data, and pushes it to a Kafka topic.
   
2. **Kafka Consumer Daemon**: A service that reads the data from the Kafka topic, processes it, and stores the data into an Elasticsearch index with the specified schema.

3. **FastAPI Service**: A web service that provides APIs for searching and tagging the content stored in Elasticsearch. The search allows users to filter content by any field, and the tagging feature allows tagging content with predefined static tags.
4. **Kafka UI** : a kafka ui for easy use of kafka

## Requirements

Before you begin, ensure you have the following installed:

- Docker
- Docker Compose
- Make (optional, for running Makefile commands)
## Overview
This project is a FastAPI-based service with Docker, Kafka, and other necessary configurations to run and test. This document outlines how to build, run, and interact with the project using the provided `Makefile`.

## Setup

Clone this repository to your local machine:

```bash
git clone <repository-url>
cd dobby
```

### Docker Setup
The project uses Docker for containerization. Ensure Docker is running on your system.

## Usage

### Build Docker Images
To build the Docker images for the project, run the following command:

```bash
make
```

This will build the Docker images specified in the `docker-compose.yml` file. It uses the `DOCKER_DEFAULT_PLATFORM=linux/amd64` environment variable to ensure compatibility across systems.

### Run Docker Containers
To start the application and related services, use:

```bash
make run
```

This command starts the Docker containers as defined in the `docker-compose.yml` file. The application will be accessible according to the settings in your Docker Compose file.

### Restart Containers
If you need to restart the containers, use:

```bash
make restart
```

This will restart the running containers.

### Bring Down Containers
To stop and remove all containers, networks, and volumes defined in your `docker-compose.yml` file:

```bash
make down
```

### View Logs
To view the logs of the application container, run:

```bash
make log
```

This will display the logs of the `app` container in real-time.

### Run Tests
To run tests inside the FastAPI service container, use:

```bash
make run-tests
```

This will execute the tests using `pytest` inside the FastAPI service container.

### Create Kafka Topic
To create a Kafka topic (`texts_topic`), use:

```bash
make create-kafka-topic
```

This command will create a Kafka topic named `texts_topic` with 1 partition and a replication factor of 1, if it doesn't already exist.

## Additional Commands
The following are the targets available in the `Makefile`:

- **docker**: Builds the Docker images for the project.
- **run**: Starts the Docker containers defined in `docker-compose.yml`.
- **restart**: Restarts the Docker containers.
- **down**: Stops and removes all containers, networks, and volumes.
- **log**: Shows real-time logs for the app container.
- **run-tests**: Runs tests inside the FastAPI service container.
- **create-kafka-topic**: Creates the Kafka topic `texts_topic`.

## Troubleshooting

If you encounter issues with Docker or the services, check the following:

- Ensure Docker is running and properly configured.
- Check logs with `make log` to diagnose issues with the application.
- If the containers are not starting, try `make down` and then `make run` to reset the environment.
# Dobby Project Architecture Overview

This project follows a **microservices** architecture with a focus on modularity, scalability, and maintainability. The key components of the system are as follows:

## 1. **Daemon Kafka Consumer**
- **Purpose**: Consumes data from a Kafka topic and stores it in Elasticsearch.
- **Components**:
  - `config.py`: Contains configuration settings, such as connection details for Kafka and Elasticsearch.
  - `consumer.py`: The core logic for consuming messages from Kafka and processing them.
  - `elastic_client.py`: Handles interactions with the Elasticsearch service.
  - `kafka_consumer.py`: Manages the Kafka consumer setup and connection.
  - `Dockerfile`: Containerizes the consumer service for deployment.
  - `requirements.txt`: Lists the Python dependencies needed for the consumer service (e.g., Kafka and Elasticsearch clients).

**How it helps the project**:
- Independent, scalable service that decouples data ingestion from processing.
- Ensures data is reliably consumed from Kafka and inserted into Elasticsearch.

## 2. **Daemon Kafka Producer**
- **Purpose**: Fetches data from an external API and sends it to a Kafka topic for consumption by the Kafka consumer.
- **Components**:
  - `api_client.py`: Fetches data from an external API.
  - `config.py`: Configuration for Kafka and external API connections.
  - `kafka_producer.py`: Sends data to Kafka topics.
  - `producer.py`: Orchestrates fetching data and publishing it to Kafka.
  - `Dockerfile`: Containerizes the producer service for deployment.
  - `requirements.txt`: Lists dependencies for the producer service (Kafka client and external API libraries).

**How it helps the project**:
- Decouples the data fetching and publishing logic from other services.
- Can be independently scaled to handle high-volume data production.

## 3. **FastAPI Service**
- **Purpose**: Provides RESTful APIs to interact with Elasticsearch, enabling search and tagging functionalities.
- **Components**:
  - `config/settings.py`: Stores configuration details for Elasticsearch and other settings.
  - `controllers/`:
    - `search_controller.py`: Handles search-related API requests.
    - `tag_controller.py`: Handles tagging functionality.
  - `main.py`: The FastAPI application entry point, initializing the app and routes.
  - `models/`:
    - `search_request_dto.py`: Defines the structure of search requests.
    - `tag_request_dto.py`: Defines the structure of tag-related requests.
  - `repositories/`:
    - `elastic_repository.py`: Interface for interacting with Elasticsearch.
  - `services/`:
    - `search_service.py`: Business logic for searching in Elasticsearch.
    - `tag_service.py`: Business logic for tagging content in Elasticsearch.
  - `Dockerfile`: Containerizes the FastAPI service.
  - `README.md`: Documentation for setting up and using the FastAPI service.
  - `requirements.txt`: Lists dependencies for the FastAPI service (FastAPI, Elasticsearch client, etc.).

**How it helps the project**:
- Provides a fast and flexible API layer to interact with Elasticsearch.
- The clean separation of concerns (service/repository pattern) ensures easy maintainability and testability.
- Scalable architecture with clear service boundaries.

## 4. **docker-compose.yml**
- **Purpose**: Orchestrates the deployment of multiple services (Kafka, Elasticsearch, and FastAPI) with a single command.
- **How it helps the project**:
  - **Single Command Setup**: With `docker-compose up`, the entire system can be started together.
  - **Isolation**: Each service runs in its own container, ensuring isolation of dependencies.
  - **Scalability**: Docker Compose makes it easy to scale services based on needs.

## 5. **requirements.txt**
- This file contains the list of Python dependencies needed for the entire project (e.g., Kafka client, Elasticsearch client, FastAPI, etc.).
- **How it helps the project**:
  - Centralized dependency management for the entire project.
  - Ensures consistent environments across different stages of development and deployment.

---

### **How the Architecture Helps the Project**

1. **Separation of Concerns**:
   - The project is divided into multiple services with clearly defined responsibilities:
     - **Producer** fetches data and sends it to Kafka.
     - **Consumer** processes Kafka messages and stores them in Elasticsearch.
     - **FastAPI service** provides an API layer to interact with Elasticsearch.
   - This modular structure makes it easy to develop, maintain, and scale individual components.

2. **Scalability**:
   - Each service is containerized using Docker, allowing for easy scaling and management.
   - Kafka itself is highly scalable and serves as a reliable messaging queue between the producer and consumer services.

3. **Fault Tolerance**:
   - Kafka acts as a buffer between the producer and consumer, ensuring that data is not lost if a service fails. The consumer can process messages at its own pace when it's back online.

4. **Ease of Deployment**:
   - The use of Docker and Docker Compose simplifies the deployment process. The entire system can be spun up with a single command (`docker-compose up`), ensuring consistency across environments.

5. **Extensibility**:
   - The system is designed with extensibility in mind, following principles such as Object-Oriented Programming (OOP) and clean architecture patterns. This makes it easy to add new features or integrate with other systems in the future.

By using a microservices architecture, this system is robust, scalable, and easy to maintain, making it well-suited for handling growing data volumes and user requests.

- **Apache Kafka**: Used as a message broker between the producer and the consumer services.
- **Elasticsearch**: A NoSQL database used for storing the data produced by the consumer service. It allows fast searches and filtering.
- **FastAPI**: Provides an HTTP API for interacting with Elasticsearch, including search and tagging features.

## Project Structure
Click [here](https://drive.google.com/file/d/1RN3_QBH1vO4Po8fx6ADT7v-PJM-30pPL/preview) to see the project structure.
## Services

### 1. Kafka Producer Daemon Service

This service fetches data from the FakerAPI every minute and produces it to a Kafka topic.

#### Features:
- Fetches records every minute from the FakerAPI.
- Formats the data to match the schema required by the consumer.
- Publishes the data to a Kafka topic.

#### Docker Setup:
- Dockerfile and requirements are specified in the `producer-service` directory.
- Kafka client libraries are required to connect and produce messages to the Kafka broker.

### 2. Kafka Consumer Daemon Service

This service reads data from the Kafka topic and stores it in an Elasticsearch index with a predefined schema.

#### Elasticsearch Index Schema:
| Kafka Field  | Elastic Field | Data Type   |
|--------------|---------------|-------------|
| Title        | Name          | text        |
| Author       | Username      | keyword     |
| Genre        | Category      | keyword     |
| Content      | Text          | text        |
| inserted_at* | timestamp     | timestamp   |

#### Features:100
- Consumes messages from Kafka and parses them.
- Stores the data in Elasticsearch with the necessary transformations and schema mapping.
- Adds an `inserted_at` field with the timestamp of when the document is stored.

#### Docker Setup:
- Dockerfile and requirements are specified in the `consumer-service` directory.
- Elasticsearch client libraries are required to connect and store documents in Elasticsearch.

### 3. FastAPI Service

This service exposes two main APIs:

#### a. Search API:
- **Endpoint**: `/api/search/`
- **Method**: `GET`
- **Query Parameters**: `field`, `value`
  - `field`: The field of the Elasticsearch document to filter by.
  - `value`: The value to filter for in the specified field.
  - Sample URL: GET http://localhost:8000/api/search/?field=title&value=some_value

#### b. Tagging API:
- **Endpoint**: `/api/tag/`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "doc_id": "string",
    "tag": 1
  }
Tags: Tags are predefined and fixed as 1, 2, or 3.
Updates the Tag field of a document in Elasticsearch.

#### Docker Setup:
- Dockerfile and requirements are specified in the `fastapi-service` directory.
- Elasticsearch client libraries are required to connect and store documents in Elasticsearch.

### How Verify the services are running?:

#### Kafka: Should be running on port 9093.
#### Elasticsearch: Should be accessible at http://localhost:9200.
#### FastAPI: Should be accessible at http://localhost:8000.
Access FastAPI APIs:

- **Search API: GET http://localhost:8000/api/search/?field=title&value=some_value**
- **Tagging API: POST http://localhost:8000/api/tag/**

Payload:
```json
{
  "doc_id": "document_id",
  "tag": 1
}

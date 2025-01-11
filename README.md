# Chat App

A simple Python-based chat application with FastAPI that integrates with a dummy AI assistant.

## Features

- RESTful endpoints for chat and chat history
- Dummy AI assistant for generating responses
- Containerized with Docker for both backend and frontend(using NGINX)
- Basic CI/CD pipeline with GitHub Actions
- Logging for observability

## Setup

### Prerequisites

- Docker (If using Docker for setting it up)
- Python 3.12 and pip (If setting up locally)

### Using Docker
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <repo-directory>
   ```
2. Build and start the application using Docker Compose:
    ```she
    docker-compose up --build
    ```
3. Access the frontend in your browser at `http://localhost:8085/frontend.html` .

### Run Locally

To run the application locally without Docker

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <repo-directory>
   ```
2. Navigate to the `backend` directory and install the dependencies:
   ```sh
   cd backend
   pip install -r requirements.txt
   ```
3. Start the backend server:
    ```sh
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```
4. Navigate to the `frontend` directory and start a simple HTTP server:
    ```sh
   cd ../frontend
   python -m http.server 8085
   ```
5. Access the frontend in your browser at `http://localhost:8085/frontend.html`

## Testing
Run the tests using `pytest`:
```sh
pytest
```

This will execute all the tests and provide a summary of the results.

## API Contract

This section defines the API contract for the backend implementation of the Chat App. The backend is built using FastAPI and exposes the following endpoints.

### Endpoints

#### 1. Get Chat History
- **Endpoint**: `/chat/history`
- **HTTP Method**: `GET`
- **Request Body**: None
- **Response Codes**:
  - `200 OK`: Successfully retrieved chat history.
  - `500 Internal Server Error`: Failed to retrieve chat history due to server issues.
- **Response Body**:
  - **Success**:
    ```json
    [
        {
          "user": "User message",
          "AI": "AI Assistant response"
        }
      
    ]
    ```
  - **Error**:
    ```json
    {
      "message": "Failed to fetch chat history."
    }
    ```

---

#### 2. Send New Message
- **Endpoint**: `/chat/message`
- **HTTP Method**: `POST`
- **Request Body**:
  The request body must be in JSON format:
  ```json
  {
    "message": "User's chat message"
  }
  ```
  **Example**:
  ```json
  {
    "message": "Hello, AI assistant!"
  }
  ```
- **Response Codes**:
  - `200 OK`: The message was successfully processed, and a response was received.
  - `400 Bad Request`: The request body is invalid or missing fields.
  - `500 Internal Server Error`: An error occurred on the backend while processing the message.
- **Response Body**:
  - **Success**:
    ```json
    {
      "status": "Success",
      "response": "AI Assistant's response"
    }
    ```
  - **Error (400) or (500)**:
    ```json
    {
      "status": "error",
      "message": "Internal Server Error"
    }
    ```

---

### Notes:
- Ensure valid JSON payloads are sent for POST requests to avoid `400 Bad Request` errors.
- Additional endpoints may be added as new features are developed.

## Deploying the container on Kubernetes cluster

To deploy the application to a Kubernetes cluster, follow these steps:

1. **Setup Kubernetes Cluster:**
   - Ensure you have a Kubernetes cluster set up. You can use managed services like GKE, EKS, or AKS, or a local solution like Minikube or Kind for development.

2. **Build and Push Docker Images:**
   If you haven't already pushed the Docker images to a container registry, ensure you do so by:
   ```sh
   docker build -t <your-registry>/<backend-image-name>:<tag> ./backend
   docker push <your-registry>/<backend-image-name>:<tag>
   docker build -t <your-registry>/<frontend-image-name>:<tag> ./frontend
   docker push <your-registry>/<frontend-image-name>:<tag>
   ```

3. **Create Kubernetes Manifests:**
   - Create `Deployment` and `Service` YAML files for both the backend and frontend. Ensure proper configuration for ports, environment variables, and image names.

   Example of a simple backend deployment file:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: backend-deployment
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: backend
     template:
       metadata:
         labels:
           app: backend
       spec:
         containers:
         - name: backend
           image: <your-registry>/<backend-image-name>:<tag>
           ports:
           - containerPort: 8000
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: backend-service
   spec:
     selector:
       app: backend
     ports:
     - protocol: TCP
       port: 8000
       targetPort: 8000
     type: ClusterIP
   ```

4. **Apply Kubernetes Objects:**
   Apply these manifests to your cluster:
   ```sh
   kubectl apply -f <manifest-file>.yaml
   ```

5. **Access the Application:**
   - If using NodePort or LoadBalancer, access the frontend via the external IP or node.
   - For example, for a LoadBalancer service, get its external IP:
     ```sh
     kubectl get service frontend-service
     ```
   - Open the browser at `http://<external-ip>:8085/frontend.html`.

### Notes:
- Review resources, scaling, and deployment policies based on production needs.
- Use tools like Helm or Kustomize for easier management of Kubernetes deployments.

---
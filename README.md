# Chat App

A simple Python-based chat application with FastAPI that integrates with a dummy AI assistant, featuring persistent storage using SQLite.

## Features

- RESTful endpoints for chat and chat history
- Dummy AI assistant for generating responses
- Containerized with Docker for both backend and frontend(using NGINX)
- Basic CI/CD pipeline with GitHub Actions
- Logging for observability

## **Design Considerations**

This section outlines the key design considerations and trade-offs made in the implementation of the chat application.

---

### **1. Technology Stack**

- **FastAPI**: Chosen for its simplicity, asynchronous capabilities, and automatic OpenAPI documentation generation.
- **Docker**: Used for containerization, ensuring consistency across development, testing, and production environments.
- **Python Logging**: Integrated for observability and debugging during runtime.
- **In-Memory Data Storage**: Used to store chat history for simplicity in this prototype.

---

### 2. Chat History Storage

**Current Implementation:**
- Chat history is now stored in a SQLite database for persistent storage. This ensures chat data remains available even after restarts, making it more suitable for practical use cases.

**Future Considerations:**
- Scale to larger databases like PostgreSQL or MongoDB for handling larger datasets or more complex queries.
- Add caching mechanisms such as Redis for faster querying of frequently accessed data.

---

### **3. Generative AI Integration**

- **Current Implementation**:
  - A dummy function is used to simulate responses from an AI/LLM model.
  - Designed with clear placeholders to integrate real LLM APIs (e.g., OpenAI, Hugging Face) in the future.
- **Future Considerations**:
  - Implement retries and rate-limiting for LLM API calls to handle quotas and ensure stability.
  - Use a caching layer for responses to reduce API call frequency for repeated questions.

---

### **4. Observability**

- **Current Implementation**:
  - Integrated Python logging for tracking user messages, errors, and AI responses.
  - Logs are written to stdout, making them suitable for redirection to centralized logging systems.
- **Future Considerations**:
  - Integrate monitoring and logging tools (e.g., Splunk, Datadog, ELK Stack) for production-grade observability.
  - Add support for distributed tracing (e.g., OpenTelemetry) to track request lifecycles.

---

### **5. Containerization and Portability**

- **Current Implementation**:
  - Docker is used to containerize the application, ensuring a consistent runtime environment.
  - Kubernetes manifests are provided for deployment in scalable environments.
- **Future Considerations**:
  - Add Helm charts for more advanced Kubernetes deployment options.
  - Integrate with CI/CD pipelines for automated deployment.

---

### **6. Scalability**

- **Current Implementation**:
  - Basic horizontal scaling is supported through Kubernetes/OpenShift configurations.
  - Stateless architecture ensures compatibility with multiple replicas.
- **Future Considerations**:
  - Add support for horizontal autoscaling based on CPU or memory usage.
  - Introduce sharding or partitioning for database scalability when transitioning to persistent storage.

---

### **7. Security**

- **Current Implementation**:
  - Sensitive information, such as API keys, can be stored as environment variables.
  - OpenShift-specific deployment leverages Kubernetes secrets.
- **Future Considerations**:
  - Implement authentication and authorization for API endpoints (e.g., OAuth2, API tokens).
  - Regularly scan dependencies and container images for vulnerabilities.

---

### **8. API Design**

- **Current Implementation**:
  - RESTful APIs are used for simplicity and broad compatibility.
  - APIs are documented with clear contracts and example payloads.
- **Future Considerations**:
  - Enhance APIs with pagination for large chat histories.
  - Explore GraphQL for more flexible query structures if needed.

---

### **9. Testing and CI/CD**

- **Current Implementation**:
  - Unit tests validate individual components like utility functions and API endpoints.
  - Integration tests ensure the end-to-end flow of the application works as expected.
  - A GitHub Actions workflow is provided for linting, testing, and building.
- **Future Considerations**:
  - Add performance testing for API endpoints under high concurrency.
  - Expand CI/CD to include staging and production deployments with rollback mechanisms.

---

### **10. Frontend Considerations**

- **Current Implementation**:
  - A simple HTML-based frontend is provided for user interaction.
  - Designed with modern CSS for usability and responsiveness.
- **Future Considerations**:
  - Replace the static frontend with a dynamic one using React or Vue.js.
  - Add WebSocket support for real-time communication.

---

This design ensures a balance between simplicity for prototyping and scalability for future enhancements.

## Setup

### Prerequisites

- Docker (If using Docker for setting it up)
- Python 3.12 and pip (If setting up locally)
- SQLite: Ensure SQLite is available, as it's required for chat history storage.

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

---

## Database Notes

- SQLite file `chat.db` will be created in the default backend working directory.

---

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
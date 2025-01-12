# FastAPI and React Chat App with AI Integration

A Python-based chat application built using **FastAPI** and **React**, featuring a dummy AI assistant, persistent **SQLite** storage, and containerization with Docker.

## **Solution Overview**

### **Backend**
- Provides **RESTful APIs** for chat and chat history management.
- Persistent chat history storage using **SQLite**.
- **Scalability** options: easy migration to databases like PostgreSQL or MongoDB.
  
### **AI Integration**
- Simulated AI responses using a dummy AI assistant.
- Placeholder for integrating real LLM APIs (e.g., **OpenAI**, **Hugging Face**) in the future.

### **Frontend**
- **React** based dynamic and user-friendly interface capable of communicating with the backend over REST APIs.

### **Containerization**
- **Dockerized** backend and frontend for environment consistency.
- Streamlined development and production orchestration using **Docker Compose** and **Kubernetes**.

### **CI/CD**
- A basic **GitHub Actions** pipeline for effective linting, testing, and deployment workflows.

### **Logging and Observability**
- Integrated **Python logging** to track interactions and ease debugging.

---

## **Design Considerations**

This section outlines the key design considerations and trade-offs made in the implementation of the chat application.

---

### **1. Technology Stack**

- **FastAPI**: Async capabilities and automatic OpenAPI generation.
- **React**: Modern frontend framework supporting reusable components and strong community support.
- **SQLite**: Lightweight, disk-based database catering to current project needs.
- **Docker**: Used for containerization to provide a consistent runtime environment across development, testing, and production.
- **Python Logging**: Incorporated for observability and debugging.

---

### 2. Chat History Storage

**Current Implementation:**
- Chat history is stored in a **SQLite database**, ensuring persistence even after application restarts.
- SQLite was chosen for its simplicity, zero-configuration setup, and capability to manage the required data volume for this application.

**Future Considerations:**
- Upgrade to a robust database like **PostgreSQL** or **MongoDB** for scalability and support for larger datasets.
- Introduce caching with **Redis** for faster access to frequently accessed chat data.

---

### **3. Generative AI Integration**

- **Current Implementation**:
  - A dummy function is used to simulate responses from an AI/LLM model.
  - Designed with clear placeholders to integrate real LLM APIs (e.g., OpenAI, Hugging Face) in the future.
- **Future Considerations**:
  - Implement retries and rate-limiting for LLM API calls to handle quotas and ensure stability.
  - Use a caching layer for responses to reduce API call frequency for repeated questions.

---

### **4. Frontend Design**

**Current Implementation:**
- Replaced the static HTML frontend with a **React-based** application

**Future Considerations:**
- Add themes and responsiveness improvements, leveraging libraries like **Material-UI** or **TailwindCSS**.

---

### **5. Observability**

- **Current Implementation**:
  - Python logging for tracking user messages, errors, and AI responses.
  - Designed with provisions for centralized logging via tools like **Datadog**, **Splunk**, or ELK Stack.
  
- **Future Considerations**:
  - Introduce **OpenTelemetry** or other distributed tracing tools.

---

### **6. Containerization and Portability**

- **Current Implementation**:
  - Backend and frontend containerized using Docker.
  - Kubernetes manifests are provided for deployment in scalable environments.
- **Future Considerations**:
  - Add Helm charts for more advanced Kubernetes deployment options.
  - Integrate with CI/CD pipelines for automated deployment.

---

### **7. Scalability**

- **Current Implementation**:
  - Basic horizontal scaling is supported through Kubernetes/OpenShift configurations.
  - Stateless architecture ensures compatibility with multiple replicas.
- **Future Considerations**:
  - Add support for horizontal autoscaling based on CPU or memory usage.
  - Introduce sharding or partitioning for database scalability when transitioning to persistent storage.

---

### **8. Testing and CI/CD**

- **Current Implementation**:
  - Unit tests validate individual components like utility functions and API endpoints.
  - Integration tests ensure the end-to-end flow of the application works as expected.
  - A GitHub Actions workflow is provided for linting, testing, and building.
- **Future Considerations**:
  - Add performance testing for API endpoints under high concurrency.
  - Expand CI/CD to include staging and production deployments with rollback mechanisms.

---


## Setup

### Prerequisites

1. **General Requirements**:
   - Docker (if using containerization)
   - Python 3.12 and pip (if running locally)

2. **Database**:
   - SQLite is used for chat history storage. Ensure SQLite is available on your system (most systems already include it by default).

3. **Frontend Setup**:
   - Node.js and npm are required for managing the React-based frontend.

---

### Using Docker
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <repo-directory>
   ```
2. Use Docker Compose to build and start both the backend and React-based frontend:
    ```she
    docker-compose up --build
    ```
3. Access the application in your browser:
   - **Frontend**: `http://localhost:3000`
   - The frontend communicates with the backend through RESTful APIs.

4. The SQLite database (`chat.db`) will be created automatically when the backend starts.

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
3. Start the FastAPI backend:
   ```sh
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

   The API will be available at `http://127.0.0.1:8000`.

   The SQLite database (`chat.db`) is created automatically when the backend starts.
   ```
#### Frontend Setup:
4. Navigate to the `frontend` directory and install the React dependencies:
   ```sh
   cd ../my-frontend
   npm install
   ```

5. Start the React development server:
   ```sh
   npm start
   ```

   By default, the frontend runs at `http://localhost:3000`.

6. Ensure the backend is running at `http://127.0.0.1:8000` to enable API communication.

---

### Database Configuration

- The backend uses **SQLite** for storing chat history. By default, the database file (`chat.db`) is created in the `backend` working directory upon running the application.
- You can choose a custom SQLite path or migrate to another database (e.g., PostgreSQL) by changing the database URL in the backend configuration (e.g., `settings.py`).

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
   - Open the browser at `http://<external-ip>:3000`.

### Notes:
- Review resources, scaling, and deployment policies based on production needs.
- Use tools like Helm or Kustomize for easier management of Kubernetes deployments.

---
# React Frontend for Syndio AI/ML Backend

## Overview
This project is a React-based frontend application designed to interact with the AI/ML backend. The frontend provides a user-friendly interface to manage and visualize data, communicate with the backend APIs, and display results.

## Features
- Simple and interactive user interface.
- Fetches and displays data from the backend REST API.
- Functionality to submit user inputs to the backend.
- Realtime or dynamic interactions using React state management.

---

## Requirements
Make sure the following software is installed on your machine:
- **Node.js** (v16+ recommended)
- **npm** (Node Package Manager - comes with Node.js)

You can check your Node.js and npm versions by running:
```bash
node -v
npm -v
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project folder:
   ```bash
   cd <project-folder-name>
   ```

3. Install all dependencies:
   ```bash
   npm install
   ```

---

## Running the Application

To start the React development server, run:
```bash
npm start
```
- This launches the app in development mode.
- Open your browser and go to [http://localhost:3000](http://localhost:3000) to view the app.

---

## Interacting with the Backend

Ensure that the backend server is running and accessible. Update the backend API URL in the React frontend if necessary:

- Open `src/App.js` and look for the `apiUrl` variable:
   ```javascript
   const apiUrl = 'http://127.0.0.1:8000/chat'; // Update this if your backend is hosted on a different URL
   ```

---

## Building for Production

To build a production-ready version of the app:
```bash
npm run build
```

- This generates optimized static files in the `build/` directory.
- You can deploy the content of the `build/` folder to any static server.


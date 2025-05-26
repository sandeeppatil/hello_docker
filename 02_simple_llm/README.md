# Streamlit Hello World App

This project is a simple Streamlit application that displays "Hello, World!" in a web browser. It is packaged in a Docker container for easy deployment.

## Project Structure

```
hello_docker
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Prerequisites

- Docker installed on your machine
- A Docker Hub account (optional, for pushing the image)

## Getting Started

1. **Clone the repository** (if applicable):
   ```
   git clone <repository-url>
   cd hello_docker
   ```

2. **Build the Docker image**:
   ```
   docker build -t your-dockerhub-username/hello_docker .
   ```

3. **Run the Docker container**:
   ```
   docker run -p 8501:8501 your-dockerhub-username/hello_docker
   ```

4. **Access the app**:
   Open your web browser and go to `http://localhost:8501`.

## Pushing to Docker Hub

1. **Log in to Docker Hub**:
   ```
   docker login
   ```

2. **Push the image to Docker Hub**:
   ```
   docker push your-dockerhub-username/hello_docker
   ```

Replace `your-dockerhub-username` with your actual Docker Hub username.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
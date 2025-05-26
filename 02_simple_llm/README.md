# DeutschGramWelt

This project is a Streamlit application for German word grammatical analysis using Gemini LLM, packaged in a Docker container for easy deployment.

## Project Structure

```
DeutschGramWelt
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
   cd DeutschGramWelt
   ```

2. **Build the Docker image**:
   ```
   docker build -t patilcomplex/deutschgramwelt .
   ```

3. **Run the Docker container**:
   ```
   docker run -p 8502:8502 patilcomplex/deutschgramwelt
   ```

4. **Access the app**:
   Open your web browser and go to `http://localhost:8502`.

## Pushing to Docker Hub

1. **Log in to Docker Hub**:
   ```
   docker login
   ```

2. **Push the image to Docker Hub**:
   ```
   docker push patilcomplex/deutschgramwelt
   ```

Replace `patilcomplex` with your actual Docker Hub username if different.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
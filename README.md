# Prisca Web App (Dockerized Website)

This project is a simple static website built with HTML and CSS and containerized using Docker and Nginx.

## Project Task

- Create a Dockerfile to containerize the application
- Build the container image from the dockerfile
- Create a custom bridge network for the container 
- Run the container using a hostport:container port and on the custom network created
- Access the application on the broswer
- Push application image to your Docker Hub repository
- Access docker logs and report finding
- Access container logs
- Create a new docker volume on the host
- inspect the docker volume
- Attach the volume(bind mount) to the container. HINT: stop/remove and rerun the container with volume
- workaround adding data to the bind mount volume and accessing the data in the container and on the Host


## 📌 Project Description

This project demonstrates how to package a basic web application into a Docker container, run it on a custom network, and publish it to Docker Hub.

It is part of my DevOps learning journey.

## 🤔💭 First Ask

- What type of app is this? → Static website (HTML/CSS)
- Does it need backend? → No
- Best server? → Nginx
- Which port? → 80
- Any secrets/database? → No
- Deployment target? → Docker Hub
✔ Decision: Use Nginx container.

## ⚙️ Technologies Used

- HTML
- CSS
- Docker
- Nginx
- Docker Hub

## 🚀 How to Use (I will be using my details here and I already have a static html and css file ready)

### 1. Go to your project folder:
Run:
```
cd /home/prisca/web-project
```


Make sure it looks like this:
```
web-project/
 ├── index.html
 ├── style.css
```

### 2. Now create Dockerfile:
Run:
```
nano Dockerfile
```
In your terminal, type in:
```bash
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

COPY style.css /usr/share/nginx/html/style.css

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

Then Save and exit (Ctrl + X, press Y and Enter)


### 3. Build Docker Image

Run:The command to build the docker image is run from the same directory as the Dockerfile
```
docker build -t prisca-web-app .
```

### 4. Create Custom Bridge Network

Now create your own network:
```
docker network create prisca--network
```

Check it:
```
docker network ls
```
You’ll see: prisca--network


### 5. Run Container on Custom Network

Now run your container:
```
docker run -d --name web-container --network prisca--network -p 8080:80 prisca-web-app
```
### 6. Open in Browser
Your Docker container is port-forwarded to your browser using this socket address
Now open:
```
http://localhost:8080
```
🎉 Your HTML + CSS will show.

### 7. Push to dockerhub

Create a Docker Hub Account (If You Don’t Have One)

Go to:
👉 https://hub.docker.com

Sign up and note your username.
Example (I’ll use priskah26)


### 8. Login to Docker Hub from Terminal

Run:
```
docker login
```
Enter:
- Username
- Password

If successful, you’ll see:
Login Succeeded


### 9. Tag Your Image for Docker Hub

Run:
```
docker tag prisca-web-app priskah26/prisca-web-app:latest
```

### 10. Push to Docker Hub

Run:
```
docker push priskah26/prisca-web-app:latest
```

### 11. Test by Pulling It Again 

Run:
```
docker pull priskah26/prisca-web-app:latest
```

### 12: Check Status

See container:
```
docker ps
```

Logs:
```
docker logs web-container
```

Network info:
```
docker inspect web-container
```

Open browser:
```
http://localhost:8080
```
If it opens; perfect.



👩‍💻 Author
Chiamaka Prisca Onyemuze
DevOps Engineer in Training
Nigeria 🇳🇬

📄 License
Free for learning and practice.


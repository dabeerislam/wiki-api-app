# wiki-api-app
This application has been containerized
In order to build this application in docker, docker must be installed on the machine that will clone this repo
Once the repo is cloned you can run the following command
docker build -t wiki-app .
Once the image is built we can run the application as a container with the following command
docker run -it -d -p 5000:5000 wiki-app
Once that has run your application will now be running and listening on port 5000
I currently have this running as a container on a public EC2 instance in my personal AWS account linked at the following endpoint
http://18.191.176.243:5000/view_count 

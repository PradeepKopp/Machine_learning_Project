
# Housing Price Prediction by MachineLearning CI/CD

My machine learning project focuses on predicting house prices. Using advanced machine learning algorithms, I developed a model that accurately forecasts house values based on various features. The deployment process was streamlined through CI/CD pipelines, ensuring seamless updates and maintenance. The application is hosted on the Heroku platform, providing a robust and scalable web service for users to interact with the prediction model.

## Project  Requirements 

1.Github Account
2.Heroku Account
3.VS Code IDE
4.GIT cli
## Creating conda environment 

```bash
  conda create -p venv python==3.7 -y
```
```bash
 conda activate venv/
```
```bash
  pip install -r requirements.txt
```

<<<<<<< HEAD
TO add files to Git 
'''
git add . 
git add <filename>
'''
=======
##  To add files to Git 
```bash
  git add . 
```
```bash
  git add <filename>
```
```bash
  git commit -m <comment>
```
```bash
  git push origin main
```
>Note: To ignore the files or folders to ignore from git we can write name of file/folder in .gitignore file 


>To check the git status
```bash
git status 
```

>To check all the version control maintained by git
```
git log 
```

>To Create version/commit all changes by git 
```
git commit -m "message"
```

>To send version/changes to github 
```
git push origin main
```

>To check remote url 
```
git remote -v
```
## To setup CI/CD pipeline 
1.Heruku Email-
2.Heroku Api key-
3.Heroku App_Name-
## Build Docker Image 

```
docker build -t <image_name>:<tagname> .
```
>Note: Image name for docker must be lowercase 

>To list docker image 
```
docker images
```

>To list docker images 
```
docker images
```

>Run Docker image 
```
docker run -p 5000:5000 -e PORT=5000 
```

>To check running conatainers in docker 
```
docker ps
```

>To stop docker container 
 ```
 docker stop <conatainer id>
 ```

 ```
 python setup.py install
 ```

 ```
 python install -e .
 ```
>Install ipynbkernel

```
pip install ipykernel
```
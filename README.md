# Machine_learning_Project
This is my first machine Learning End to End project

Machine Learning Project 
Requirements 

1.Github Account
2.Heroku Account
3.VS Code IDE
4.GIT cli 

Creating conda environment 
'''
conda create -p venv python==3.7 -y
conda activate venv/
pip install -r requirements.txt
'''

TO add fioles to Git 
'''
git add . 
git add <filename>
'''

-Note: To ignore the files or folders to ignore from git we can write name of file/folder in .gitignore file 

To check the git status
'''
git status 
'''

To check all the version control maintained by git
'''
git log 
'''

To Create version/commit all changes by git 
'''
git commit -m "message"
'''

To send version/changes to github 
'''
git push origin main
'''
To check remote url 
'''
git remote -v
'''

To setpup CI/CD pipeline 
1.Heruku Email-
2.Heroku Api key-
3.Heroku App_Name-

Build Docker Image 
'''
docker build -t <image_name>:<tagname> .
'''
>Note: Image name for docker must be lowercase 

To list docker image 
'''
docker images
'''

To list docker images 
'''
docker images
''''

Run Docker image 
'''
docker run -p 5000:5000 -e PORT=5000 
'''

To check running conatainers in docker 
'''
docker ps
'''

To stop docker container 
 '''
 docker stop <conatainer id>
 '''

 '''
 python setup.py install
 '''
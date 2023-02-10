# Travel Records Management Platform (Backend)

## Description
This repo contains backend APIs for the management of travel records.

We sometimes forget those wonderful travels we had with our families, friends, or just ourselves. Does it sound nice if we can have a tool that helps us 
manage all the travel records which we can edit and review at any time or even share with others?

“Travel Records Management Platform” is such a tool built with web application techniques, i.e., FastAPI and SQLite, where users can manage their travel 
records easily. They can create new travel records or update the existing records within only a few minutes, and retrieve those records with just a few 
clicks.

## Load and Run (in Terminal)
Step1. Clone this repo to the local machine

Step2. Once this repo has been cloned successfully, open terminal and go into the direcory of this repo

Step3. Run the following command inside the "side-project-BingLiang666" folder :
```
uvicorn record.main:app --reload
```

Step4. You will see the following responses and can go to different endpoints of http://127.0.0.1:8000 to use these APIs.
```
ice@Bings-MacBook-Pro side-project-BingLiang666 % uvicorn record.main:app --reload 
INFO:     Will watch for changes in these directories: ['/Users/ice/Documents/Keep Calm and Code On/CS601 PRINCIPLES OF SOFTWARE DEVELOPMENT/side-project/side-project-BingLiang666']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [41437] using StatReload
INFO:     Started server process [41439]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Setp5. FastAPI offers a powerful docs platform that we can try using those APIs: http://127.0.0.1:8000/docs. (Note: Please keep the backend server running during using this platform.)


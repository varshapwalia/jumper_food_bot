## JUMPER
Jumper_food_bot contains all url endpoints for application

## Setup Guide

1. `sudo pip install virtualenv`
2. `virtualenv venv`
3. `source venv/bin/activate`

## How to use

1. Clone the whole project
2. Install the required packages
3. Follow setup instructions
4. Start creating your application
5. Change `.env` file according to the requirements


Note: Also install the required packages from requirements.txt

## Upgrade
pip install -r requirements.txt --upgrade

## Structure

1. Controllers for APIs needed and handling requests.
2. Models for Database structuring
3. Scripts for custom jobs and intiating projects.
4. Workers for cron and queing based jobs
5. requirements.txt keeps the track of required packages.
6. Staticd for files, Custom CSS an JS
7. Templates for Html pages.
8. Procfile and runtime.txt for server enviroment and deployent

## Liberties Taken
1. I used Sandbox environment to speed up the dev process which is easly replacebe with production apis.
2. In consideration of time boundation I allowed merchants to fill merchant IDs and access tokens to access data without wasting time. Thoufh i have kept the code i would have used for user in model/user and app.py for login process.
3. othersie they had to go through a sign up and login based system that i would have created to handling idividual data and protecting the privacy. 
4. Not using Rich Respose to make it look like cards and options to choose from.

## Ways To Improve the Project and learnings

1. Creating a well defined Sign up project where we can give individual access to users.
2. Making it auto delete and replace previous queries to update bot.
3. Making RichResponse type question to direct the flow.
4. better UI and management of accounts.
5. Authentication of user.
6. Attaching tiwtter bot and slack bot as well.

## Challanges Faced and Issues

1. Process and procedures of clover took some time to go through the whole documentation.
2. Google NAtural Language was paid service by hour so i had to go with Dialogflow (google owned chatbot builder).
3. Deleting the existing same intents and finding their ids. Had to recieve ID for that purpose from google.

# Guestbook

## Installation

### Create a virtual environment  

I use [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) but you can choose which virtual environment tool you want. Specify Python 3.10 to be installed in your environment.  

`$ conda create -n guestbook python=3.10`  

### Install required stuff  
`$ pip install -e . -r requirements.txt`  

## Usage
Run Uvicorn ASGI server from projects base directory:  
`$ uvicorn guestbook.api.app:app`  

Go to http://127.9.9.1:8000/docs to test app with Swagger UI (automatic interactive API documentation)  

There is no front end for this app yet. But all database and API functionality can be tested from previously mentioned Swagger UI

## Description
A guestbook app using FastApi and SQLModel running on Uvicorn  

## Test usage
I have not written any tests for this app so far. Lazy me...


 
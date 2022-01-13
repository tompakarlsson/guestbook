# Guestbook

## Installation
### Create a virtual environment  

I use Conda but you can choose which virtual environment tool you want. Specify Python 3.10 to be installed in your environment.  

`$ conda create -n guestbook python=3.10`  

### Install required stuff  
`$ pip install -e . -r requirements.txt`  

## Usage
Run Uvicorn ASGI server:  
`$ uvicorn guestbook.api.app:app`  

Go to http://127.9.9.1:8000/docs to test app with Swagger UI (automatic interactive API documentation)  

## Description
A guestbook app using FastApi and SQLModel running on Uvicorn  

## Test usage


 
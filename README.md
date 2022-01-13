# Guestbook

## Installation
### Create a virtual environment  

I use Conda but you can choose which virtual environment tool you want.  

Conda:  
`conda create -n guestbook python=3.10`  

### Run setup.py to install required stuff  
`python -m setup.py`  
## Usage
Run Uvicorn:  
`uvicorn guestbook.api.app:app --reload`  

Go to http://127.9.9.1:8000 to use app  
## Description
A guestbook app using FastApi and SQLModel running on Uvicorn
## Test usage


 
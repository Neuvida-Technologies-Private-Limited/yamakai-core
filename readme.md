## This repository contains the Ai code of yamak.ai

### Steps to run the repository
 
1. Create the virtual environment.<br/>
    **Step-1:** sudo apt-get update
    **Step-2:** sudo apt-get install python3-venv <br/>
    **Step-3:** python3 -m venv virtual_env <br/>
    **Step-4:** source virtual_env/bin/activate

2. Install the general requirements to run the app
3. Make a file .env file same as .env.example and take values from other fellow developer

#### Command to run pylint only for a directory
```
    pylint <directory name>
```    
#### Command to run any .py file
```
    python3 -m <folder>.<file without .py>
    Example: python3 -m analytics.main
```
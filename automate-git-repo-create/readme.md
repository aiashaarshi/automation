## Automate with python: this python script will automatically create a repository with the name you want

> Make sure you have python3 installed.

### Run the following commands:

```sh
pip3 install -r requirements.txt
touch .env
```

Then open the .env file and store your USERNAME, PASSWORD, and DIR variables in the following way:

```sh
USER_NAME=YOUR_USER_OR_EMAIL
PASSWORD=YOUR_PASS
DIR=PROJECT_DIR
```

Run the python file:

```sh
python3 create-repo.py -r "test-repo"
```

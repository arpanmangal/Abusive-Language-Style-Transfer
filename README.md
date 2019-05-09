# Style Transfer: Saving the world from Hate Speech


## Setup

### Setting up Google-Translate
Generate a service account key (`service.json`) for Google Translate API. ([Instructions](https://cloud.google.com/translate/docs/quickstart-client-libraries#client-libraries-install-python))

Store it in the model/ directory.

### Requirements
```
$ virtualenv --no-site-packages env -p python3
$ source env/bin/activate
$ pip install -r requirements.txt
```

## Running
```
$ source env/bin/activate
$ python app.py
```

## Demo
Have fun [here](https://noabuse.herokuapp.com/)

A brief summary of our experiments, their results and comparison with state-of-the-art models can be found in [Experiments_Summary.pdf](https://noabuse.herokuapp.com/report.pdf).

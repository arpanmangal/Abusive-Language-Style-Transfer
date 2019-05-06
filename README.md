# Style Transfer: Saving the world from Hate Speech


## Setup

### Requirements
1. flask
2. hatesonar
3. NLTK (PorterStemmer)
4. google.cloud:

```
$ pip install --upgrade google-cloud-translate
```

### Setting up Google-Translate
Generate a service account key for Google Translate API. ([Instructions](https://cloud.google.com/translate/docs/quickstart-client-libraries#client-libraries-install-python))

Store it in the current directory.

## Running
Either execute below command directly, or, make necessary modifications to run.sh .
```
$ ./run.sh
```

## Demo
Have fun [here](http://13.76.41.83:7100/)

A brief summary of our experiments, their results and comparison with state-of-the-art models can be found in [Experiments_Summary.pdf](Experiments_Summary.pdf).

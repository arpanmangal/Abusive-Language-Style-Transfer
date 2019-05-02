export FLASK_APP=server.py
export GOOGLE_APPLICATION_CREDENTIALS="$PWD/service.json"
flask run --host=0.0.0.0 --port=7100

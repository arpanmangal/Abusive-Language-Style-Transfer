export GOOGLE_APPLICATION_CREDENTIALS="$PWD/service.json"
export FLASK_APP=server.py
flask run --host=0.0.0.0 --port=7100

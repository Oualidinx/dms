from main_app import application, create_app, cli
import os
try:
    application = create_app(os.environ.get('FLASK_ENV'))
except Exception as exception:
    print(str(exception))

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5555)

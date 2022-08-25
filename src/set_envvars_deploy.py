import json
import os


with open('zappa_settings.json', 'r+') as file:
    print('opening file')
    data = json.load(file)
    data['production']['aws_environment_variables']['DB_HOST'] = os.getenv('DB_HOST')
    data['production']['aws_environment_variables']['DB_PORT'] = os.getenv('DB_PORT')
    data['production']['aws_environment_variables']['DB_USER'] = os.getenv('DB_USER')
    data['production']['aws_environment_variables']['DB_NAME'] = os.getenv('DB_NAME')
    data['production']['aws_environment_variables']['DB_PASSWORD'] = os.getenv('DB_PASSWORD')
    data['production']['aws_environment_variables']['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate()
    print('done')

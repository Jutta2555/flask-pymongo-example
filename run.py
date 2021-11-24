
from mflix.factory import create_app

import os
import configparser


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == "__main__":
    app = create_app()
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = config['PROD']['DB_URI']
    # 'mongodb+srv://mflixuser:CQNQmXIQXlnqD4fQ@sandbox.hkmmq.mongodb.net/sample_mflix'
    # 
    # 

    app.run()

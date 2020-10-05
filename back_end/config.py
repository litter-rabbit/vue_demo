import os
from dotenv import load_dotenv


base_dir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
load_dotenv(os.path.join(base_dir,'.env'),encoding='utf-8')


class Baseconfig:

    SQLALCHEMY_DATABSE_URI='mysql://root:root@localhost:3306/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True






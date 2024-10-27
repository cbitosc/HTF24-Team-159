import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'a_secure_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://localhost/db_name')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Additional recommended settings
    DEBUG = os.getenv('FLASK_DEBUG', 'False') == 'True'
    TESTING = os.getenv('FLASK_TESTING', 'False') == 'True'
    
    # Example of additional database settings
    SQLALCHEMY_POOL_SIZE = int(os.getenv('DB_POOL_SIZE', 5))
    SQLALCHEMY_MAX_OVERFLOW = int(os.getenv('DB_MAX_OVERFLOW', 10))

    # Security headers
    SESSION_COOKIE_SECURE = os.getenv('FLASK_ENV', 'production') == 'production'
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True

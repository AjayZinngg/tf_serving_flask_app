# Flask settings
FLASK_SERVER_NAME = 'localhost:5001'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# GAN client settings
DEFAULT_TF_SERVER_NAME = '172.17.0.2'
DEFAULT_TF_SERVER_PORT = 9000
GAN_MODEL_NAME = 'gan'
GAN_MODEL_SIGNATURE_NAME = 'predict_images'
GAN_MODEL_INPUTS_KEY = 'images'

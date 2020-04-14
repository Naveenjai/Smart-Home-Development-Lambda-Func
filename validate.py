"""Alexa Smart Home Validation Package Sample Code.
This module is used by Alexa Smart Home skills to validate their Lambda responses and async
messages before sending them back to Alexa. If an error is found, an exception is thrown so that
the developer can catch the error and do something about it, instead of sending it back to Alexa
and causing an error on the Alexa side.
This specific package uses the jsonschema (https://github.com/Julian/jsonschema) Python implementation
of the JSON Schema Draft 4 to perform the actual validation against the validation schema.
"""

import json

from jsonschema import validate

def validate_message(request, response):

    # update below with path to your validation schema
    # this path works if you copy the latest validation schema into the same directory as this file
    # validation schema: https://github.com/alexa/alexa-smarthome/wiki/Validation-Schema
    path_to_validation_schema = "alexa_smart_home_message_schema.json"

    with open(path_to_validation_schema) as json_file:
        schema = json.load(json_file)
    validate(response, schema)
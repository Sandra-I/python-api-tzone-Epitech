import json
import jsonschema
from jsonschema import validate

#  the kind of schema expeted.
Schema = {
    "type": "object",
    "properties": {
        "img": {"type": "string"},
    },
    "required": ["img"]
}

Schema_translations= {
    "type": "object",
    "properties": {
        "language": {"type": "string"},
        "img": {"type": "string"},
    },
    "required": ["img","language"]
}

def validate_json(jsonData):
    try:
        validate(instance=jsonData, schema=Schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

def validate_json_translations(jsonData):
    try:
        validate(instance=jsonData, schema=Schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


#jsonData = json.loads('{"lang": "ES", "r": 25, "marks": 72}')
def translation_allowed(jsonData):
    allowed_lang = ["FR", "DE", "ES","EN-GB","EN-US"]
    for x in allowed_lang:
        if(jsonData['language'] == x):
            return True

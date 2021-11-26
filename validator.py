import json
import jsonschema
from jsonschema import validate

#  the kind of schema expeted.
Schema = {
    "type": "object",
    "properties": {
        "img": {"type": "string"},
        "lang": {"type": "number"},
    },
}

def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=Schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


#jsonData = json.loads('{"lang": "ES", "r": 25, "marks": 72}')
def translation_allowed(jsonData):
    mylist = ["FR", "DE", "ES","EN-GB","EN-US"]
    for x in mylist:
        if(jsonData[lang] == x):
            return true

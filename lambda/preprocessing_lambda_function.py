import json
import os

def lambda_handler(event, context):
    source = event['dataObject'].get('source', None)
    pairs = event['dataObject'].get('pairs', None)

    # Build response object
    output = {
        "taskInput": {
            "source": source,
            "pairs": pairs
        },
        "isHumanAnnotationRequired": "true"
    }

    return output

import copy

def required(schema: dict, requires: dict):
    schema =  copy.deepcopy(schema)
    for key, value in requires.items():
        if key not in schema['properties']:
            schema['properties'][key] = value
            if 'required' in schema:
                schema['required'].append(key)
        
    return schema
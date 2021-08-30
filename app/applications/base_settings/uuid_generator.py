import uuid 

def generate_id():
    id = uuid.uuid4().int
    code = str(id)[:8]
    return code

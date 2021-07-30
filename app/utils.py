import uuid

def generate_ref_code():
    sponser_id = str(uuid.uuid4()).replace("-","")[:6]
    return sponser_id

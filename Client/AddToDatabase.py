from riak import RiakClient, RiakNode

client = RiakClient(protocol='pbc', host='127.0.0.1', http_port=8098)

bucket = client.bucket_type('tweets').bucket('tweets')

add = bucket.new('userName', {'name': 'asd123', 'location': "Sweden", 'created_at': "123-123-123", 'id_str': "123354123"})
add.store()

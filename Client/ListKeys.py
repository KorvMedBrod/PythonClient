from riak import RiakClient, RiakNode

client = RiakClient(protocol='pbc', host='127.0.0.1', http_port=8098)

bucket = client.bucket_type('tweets').bucket('tweets')

print(bucket.get_keys())

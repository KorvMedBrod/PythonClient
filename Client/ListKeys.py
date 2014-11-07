import riak
import random
from riak import RiakClient, RiakNode

client = RiakClient(protocol='pbc', host='127.0.0.1', http_port=8098)

bucket = client.bucket_type('default').bucket('tweets')

keys = bucket.get_keys()

randm = random.randint(0,len(keys))

print(bucket.get(randm).encoded_data)

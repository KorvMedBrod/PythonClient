from riak import RiakClient, RiakNode

client = RiakClient(protocol='http', host='127.0.0.1', http_port=8098)
client.ping()

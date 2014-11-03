from riak import RiakClient
import riak

client = RiakClient(protocol='pbc', host='127.0.0.1', http_port=8098)


bucket = client.bucket_type('tweetsSchema').bucket('tweets')
print("bucket content" ,bucket)

print(client.fulltext_search("tweets","*:*"))

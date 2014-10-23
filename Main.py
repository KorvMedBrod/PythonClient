from riak import RiakClient, RiakNode

client = RiakClient(protocol='http', host='127.0.0.1', http_port=8098)
print(client.ping())
tweetBucket = client.bucket("tweets")
print(tweetBucket.get_properties())
print(client.get_buckets())
print(client.bucket_type("tweets"))
allKeysInTweets = client.get_keys(tweetBucket)
print(len(allKeysInTweets))

from pytwitter import Api


api = Api(bearer_token='AAAAAAAAAAAAAAAAAAAAALFQeQEAAAAAqhL%2FuR%2BjRTWQNQJSJrZIK%2BkQLyU%3DAPecJfUhg1QFTbv3OBlU06bhitj92OIrYnxdgUMkIDUPDPcFN8')
print(api.get_user(username='NoahCamara95'))

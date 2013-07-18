import os
import sys
import optparse

import boto
from boto.s3.key import Key

def upload(awskey, awssecret, bucket, mode, path):
	pass
	#conn = boto.connect_s3()

def main():

    optparser = optparse.OptionParser(prog='push.py', version='0.1',
        description='Push files on Amazon S3',
        usage='%prog -k [access key id] -s [secret access key] ' + \
            '-b [bucketname] -p [path] -m [mode]')
    optparser.add_option('--aws_access_key_id', '-k', dest='awskey', 
        default=os.getenv('AWS_ACCESS_KEY_ID'))
    optparser.add_option('--aws_secret_access_key', '-s', dest='awssecret', 
        default=os.getenv('AWS_SECRET_ACCESS_KEY'))
    optparser.add_option('--bucket', '-b', dest='bucket')
    optparser.add_option('--path', '-p', dest='path')
    optparser.add_option('--mode', '-m', dest='mode', choices=['assets', 'client'])
    
    options, arguments = optparser.parse_args()

    if not options.mode:
    	optparser.print_help()
    	sys.exit("Error: mode must be 'assets' or 'client'")
    if options.bucket and options.awskey and options.awssecret and options.path:
    	if os.path.exists(options.path):
    		upload(options.awskey,
    			options.awssecret,
    			options.bucket,
    			options.mode,
    			options.path)
    	else:
    		sys.exit("Error: path does not exist: %s" % options.path)
    else:
    	optparser.print_help()
    	sys.exit("Error: Missiong arguments")

if __name__ == '__main__':
	main()
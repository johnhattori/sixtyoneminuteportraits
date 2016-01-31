import os
import sys
import optparse
import logging
import json

import boto
from boto.s3.key import Key

import ssl

# Monkey patch to avoid:
# ssl.CertificateError: hostname 'my.bucket.s3.amazonaws.com'
# doesn't match either of '*.s3.amazonaws.com', 's3.amazonaws.com'
if hasattr(ssl, '_create_unverified_context'):
   ssl._create_default_https_context = ssl._create_unverified_context

logging.basicConfig(format='%(levelname)s: %(message)s',
					level=logging.INFO)

def upload_files(awskey, awssecret, bucket, path):
	logging.info("Uploading %s to bucket %s" % (path, bucket))

	logging.info("Listing files...")
	files = get_files(path)
	logging.info("Found %s files to upload" % len(files))

	logging.info("Connecting to S3")
	conn = boto.connect_s3(awskey, awssecret)
	b = conn.get_bucket(bucket)
	k = Key(b)
	for f in files:
		file_name = os.path.basename(f)
		logging.info("Uploading %s" % file_name)
		k.key = file_name
		k.set_contents_from_filename(f)
		k.set_acl('public-read')

	logging.info("Updating manifest")
	update_manifest(b, k)

def update_manifest(bucket, k):
	manifest = []
	for f in bucket.list():
		manifest.append(f.name)
	k.key = "manifest.json"
	k.set_contents_from_string(json.dumps(manifest),
							  {"Content-Type": "application/json"})
	k.set_acl('public-read')


def get_files(path):
	to_upload = []
	if os.path.isfile(path):
		to_upload.append(path)
	else:
		for root, _ , files in os.walk(path):
			for f in files:
				to_upload.append(os.path.join(root,f))
	return to_upload

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

    options, arguments = optparser.parse_args()

    if options.bucket and options.awskey and options.awssecret and options.path:
    	if os.path.exists(options.path):
    		upload_files(options.awskey,
    			options.awssecret,
    			options.bucket,
    			options.path)
    	else:
    		sys.exit("Error: path does not exist: %s" % options.path)
    else:
    	optparser.print_help()
    	sys.exit("Error: Missiong arguments")

if __name__ == '__main__':
	main()


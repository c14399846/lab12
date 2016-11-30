import boto.sqs
import boto.sqs.queue
import argparse

from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

praser = argparse.ArgumentParser()
parser.add_argument("qname")
args = parse.parse_args()
conn = boto.sqs.connect_to_region("us-west-2a")

try:
	q = conn.get_queue(args.qname)
except:
	print "failed to find queue,", args.qname

try:
	conn.delete_queue(q,True)
	print args.qname, "queue deleted"
except:
	print "could not delete queue, or doesnt exist"


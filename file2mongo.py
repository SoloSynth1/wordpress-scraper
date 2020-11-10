import os
import json
import argparse

from wpscraper.connector import MongoDBConnector
from wpscraper.document import RawDocument

parser = argparse.ArgumentParser()
parser.add_argument("filepath", type=str)
parser.add_argument("db_host", type=str)
parser.add_argument("db_port", type=int)
parser.add_argument("db_database", type=str)
parser.add_argument("db_collection", type=str)
parser.add_argument("username", type=str)
parser.add_argument("password", type=str)


def files_to_mongodb(filepath: str, db_host: str, db_port: int, db_database: str, db_collection: str,
                 username: str, password: str, **kwargs):
    files = [os.path.join(filepath, x) for x in os.listdir(filepath) if x.split(".")[-1].lower() == "json"]
    c = MongoDBConnector(db_host=db_host, db_port=db_port, db_database=db_database, db_collection=db_collection,
                         username=username, password=password, **kwargs)
    for file in files:
        with open(file, 'r') as f:
            json_obj = json.load(f)
        doc = RawDocument(raw_data=json_obj)
        resource = doc.data['resource_type']
        c.process_document(doc, resource)
        print("{} uploaded.".format(file))
    print("done.")


if __name__ == "__main__":
    args = parser.parse_args()
    files_to_mongodb(filepath=args.filepath, db_host=args.db_host, db_port=args.db_port, db_database=args.db_database,
                     db_collection=args.db_collection, username=args.username, password=args.password)

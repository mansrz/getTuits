import json
import csv
import sys

def get_hashtags(content):
    tags = {
        tag.strip("#") for tag in content.split() if tag.startswith("#")
    }
    return  ' , '.join(list(tags))

def parse_tuit(data):
    user = data.get('user', {})
    obj_dict = {
        "handle": user.get('username', ''),
        "name": user.get('displayname', ''),
        "content": data.get("content", ""),
        "replies": data.get("replyCount"),
        "retweets": data.get("retweetCount"),
        "favorite": data.get("likeCount"),
        "date": data.get("date"),
        "url": data.get("url"),
        "hashtags": get_hashtags(data.get('content', ''))
    }
    return obj_dict

def parse_json(name_file):
    obj = None
    data = None
    with open(name_file, mode="r") as file:
        tuits = "["
        lines= file.readlines()
        total = len(lines)
        for idx, line in enumerate(lines):
            tuits += f"{line}"
            if idx+1 < total:
                tuits += ","
        tuits += "]"
        obj = json.loads(tuits)
    if obj:
        data = list(map(lambda x: parse_tuit(x), obj))
    if data:
        keys = data[0].keys()
        a_file = open(f"output{name_file}.csv", "w")
        dict_writer = csv.DictWriter(a_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
        a_file.close()
            
if __name__ == "__main__":
    args = sys.argv
    if args and len(args) > 1:
        parse_json(args[1])


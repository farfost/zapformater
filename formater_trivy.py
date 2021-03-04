import json
import sys

params = {}
# -input xxx.json
# -output xxx_ready.json
# -index index_for_elk
# -type _type_of_scaner
if __name__ == "__main__":
    params.update({sys.argv[1]: sys.argv[2]})
    params.update({sys.argv[3]: sys.argv[4]})
    params.update({sys.argv[5]: sys.argv[6]})
    params.update({sys.argv[7]: sys.argv[8]})
f = open(params['-input'], 'r')
file_read = json.loads(f.read())

_id = 0
f_new = open(params['-output'], 'w')
for item in file_read[0]['Vulnerabilities']:
    header = {"index": {"_index": params['-index'], "_type": params['-type'], "_id": _id}}
    f_new.write(json.dumps(header) + '\n')
    body = {
        "VulnerabilityID": item['VulnerabilityID'],
        "PkgName": item['PkgName'],
        "InstalledVersion": item['InstalledVersion'],
        "PrimaryURL": item['PrimaryURL'],
        "Description": item['Description'],
        "Severity": item['Severity'],
        "messageId": _id,  # ??????????
        "id": _id,
    }

    if 'Title' in item:
        body.update({"Title": item['Title']})
    if 'PublishedDate' in item:
        body.update({"PublishedDate": item['PublishedDate']})
    if 'LastModifiedDate' in item:
        body.update({"LastModifiedDate": item['LastModifiedDate']})

    f_new.write(json.dumps(body) + '\n')
    _id += 1
f_new.close()

print('format succes')

import json
import sys
import datetime

now = datetime.datetime.now()

params = {}
# -input xxx.json
# -output xxx_ready.json
# -index (mesto)_(sreda)_trivyscan                     
# -type (scanimage)


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
        "Severity": item['Severity'],
        "messageId": _id,  # ??????????
        "id": _id,
        "date": now.strftime("%d.%m.%Y"),
    }

    if 'Title' in item:
        body.update({"Title": item['Title']})
    if 'PublishedDate' in item:
        body.update({"PublishedDate": item['PublishedDate']})
    if 'LastModifiedDate' in item:
        body.update({"LastModifiedDate": item['LastModifiedDate']})
    if 'Description' in item:
        body.update({"Description": item['Description']})

    f_new.write(json.dumps(body) + '\n')
    _id += 1
f_new.close()

print('format success')

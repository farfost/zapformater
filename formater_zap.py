import json
import sys

params = {}
# -input scan_s.json
# -output scan_s_ready.json
# -index (mesto)_(sreda)_(scanproject)_zapscan
# -type date

if __name__ == "__main__":
    params.update({sys.argv[1]: sys.argv[2]})
    params.update({sys.argv[3]: sys.argv[4]})
    params.update({sys.argv[5]: sys.argv[6]})
    params.update({sys.argv[7]: sys.argv[8]})
f = open(params['-input'], 'r')
file_read = json.loads(f.read())

_id = 0
f_new = open(params['-output'], 'w')
for item in file_read['site']:
    for item_2 in item['alerts']:
        for item_3 in item_2['instances']:
            header = {"index": {"_index": params['-index'], "_type": params['-type'], "_id": _id}}
            f_new.write(json.dumps(header) + '\n')
            body = {
                "sourceid": item_2['sourceid'],
                "method": item_3['method'],  # item_3
                "url": item_3['uri'],  # item_3
                "pluginId": item_2['pluginid'],
                "confidence": item_2['confidence'],
                "description": item_2['desc'],
                "messageId": _id,  # ??????????
                "reference": item_2['reference'],
                "solution": item_2['solution'],
                "alert": item_2['alert'],
                "name": item_2['name'],
                "risk": item_2['riskcode'],
                "alertRef": item_2['alertRef'],
                "id": _id,
            }
            if 'cweid' in item_2:
                body.update({"cweid": item_2['cweid']})
            if 'otherinfo' in item_2:
                body.update({"other": item_2['otherinfo']})
            if 'wascid' in item_2:
                body.update({"wascid": item_2['wascid']})

            if 'evidence' in item_3:
                body.update({"evidence": item_3['evidence']})
            if 'param' in item_3:
                body.update({"param": item_3['param']})
            if 'attack' in item_3:
                body.update({"attack": item_3['attack']})
            f_new.write(json.dumps(body) + '\n')
            _id += 1
f_new.close()

print('format succes')

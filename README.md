
python3 formater_XXX.py -input XXX.json -output XXX_ready.json -index index_for_elk -type type_of_scaner


\\webgoat
docker run --net=zapnet --name=webgoat -p 60999:8080 -t -d webgoat/webgoat-8.0



\\scaners
docker run --net=zapnet -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable:latest zap-full-scan.py  -t https://term.XXX.ru/ -a -m 5 -s -J XXX.json


trivy  -d image -f json  -o zap.json  owasp/zap2docker-stable


\\formaters
python3 formater_zap.py -input XXX.json -output XXX_ready.json -index some_index_date -type zap_scan

python3 formater_trivy.py -input XXX.json -output XXX_ready.json -index some_index_date -type trivy_scan



\\curl to elk
curl -H 'Content-Type: application/json' -u elastic:changeme  -XPOST localhost:9200/_bulk?pretty --data-binary @XXX_ready.json


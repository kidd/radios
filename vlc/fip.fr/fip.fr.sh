 curl https://www.fip.fr/rock/webradio 2>/dev/null |
 grep m3u |
 sed -e 's/[^{]*//' |
 jq '.station.substations[] | .streams[0].url' -r |
 sed 's|^.*/\([^/]*\)-\w*\.mp3.*|echo "\0" >\1.m3u|'  |
 cat

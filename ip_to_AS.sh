i="./traceroutes/$1"
n="/$1"
p="_unique_IPs"
u="_ip_to_AS_results"
#echo "$i$n$u"
#echo "$i$n$p"

echo $1
netcat whois.cymru.com 43 < "$i$n$p" > "$i$n$u"


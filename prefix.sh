#!/bin/sh
while IFS='' read -r ASN || [[ -n "$ASN" ]]; do
	echo "Finding prefixes in AS: $ASN..."
	whois -h whois.radb.net -- "-i origin AS$ASN" | grep -Eo "([0-9.]+){4}/[0-9]+" > "Prefix/AS$ASN"
done
echo "done :)"

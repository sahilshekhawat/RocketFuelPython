A Python implementation of RocketFuel topology engine.
Copyright (C) 2016 Sahil Shekhawat <sahilshekhawat01@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

### Installation

```
cd ./RocketFuel
python setup.py install
```

### Usage:

1. To start traceroute to an AS.
```
rocketfuel start <AS number>
```

2. To analyse the traceroute results
```
rocketfuel analyse <AS number>
```

3. Check licese
```
rocketfuel license
```

#### Before Running Traceroutes

1. Getting Prefixes in AS: Run "prefix.py" to get all prefixes of ASes.
2. Getting IPs from Prefixes: Run "ip_from_prefix.py" to get all IPs from advertised prefixes.

#### Running

3. Run "run.sh" to run Traceroute.java to get traceroutes from planet lab nodes.


#### After Running

1. Combine all traceroute results into one file named "<AS>_ALL"
Code:
```
cd traceroutes
for file in AS{2914,3257,13030,1239,1273,32787,16735,10026,6830,3491,18881}; do
    a="_ALL";
    touch $file$a
 	for node in $file/*; do
        cat $node >> $file$a;
    done
done
```
2. Run "Find_TraceRoute_Paths.java" to get only IP addresses from Traceroute results. A file will be created named "<AS>_path"
2. Run "Find_ip_address_from_traceroute_path.py" to get all unique ip addresses in traceroute path calculated in previous step. A file will be created named "<AS>_unique_IPs"
4. Run "ip_to_AS.sh" to get ASN for all IP addresses. File named "<AS>_ip_to_AS_results"
Code:
```
for AS in AS{2914,3257,13030,1239,1273,32787,16735,10026,6830,3491,18881}; do
	./ip_to_AS.sh $AS;
done
```
5. Run "Find_IP_address_in_particularAS.java" to get all ips in that particular as. File name: "IP_in_<AS>"
6. Run "Finding_Edge_Routers.java" to get all Edge routers. File name: "<AS>_Edge_routers"



7. Run "Find_Core_routers.py" to get all Core routers. File name: "<AS>_Core_routers"
8. Run "Find_frequency.py" to get the final results.
9. To get results. Run "results.py".

	OR
7-8-9. Run "process.py"

result is in "output" file


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

**Its still a work in progress, I am updating it daily and soon will make a release. Until then, please bear with me :)**

### About

**How it works**
1. It gets the advertised prefixes for an AS from [http://ipinfo.io/](http://ipinfo.io/)
2. Randomly get some ip addresses from each advertised prefixes.
3. ssh into each of the given host and run traceroute to those ip addresses in the background.
4. Once finished, you can calculate the results using ``analyse`` command.
5. Calculates all unique ip addresses from the traceroute ip path.
7. Finds the ip which belongs to the AS and calculate number of **Edge and Core routers**.

**Requirements**
1. **Nodes** directory: This directory must contain all the hosts from which you want to run traceroute. I recommend using [**Planet Lab**](https://www.planet-lab.org)
2. **Private Key**: A private key to ssh into those hosts.
3. **Username**: Username of the account on the hosts.

### Installation
```
cd ./RocketFuelPython
python setup.py install
```

### Usage:
1. To start traceroute to an AS. A private key is required to ssh into hosts which will run the traceroute.
(You don't want to run traceroute from you own machine, or do you? ;)

```
rocketfuel start <as-number> --key <private-key> --user <username>
```
You can check the status of the background processes by running
```
rocketfuel status
```

2. To analyse the traceroute results
```
rocketfuel analyse <AS number>
```

3. Check licese
```
rocketfuel license
```

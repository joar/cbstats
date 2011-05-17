---
layout: default
title: cbstats &ndash; CraftBukkit stats
---

# cbstats - CraftBukkit stats

`cbstats` is an abstraction for the different log files and 
settings files that a CraftBukkit installation creates.

It is capable of 
*	Determining which users are online
*	Calculating the total online time for users
*	Returning configuration settings

## Install from PyPi

	pip install cbstats

or

	easy_install cbstats

## Documentation

use

	jwandborg@sophie:~$ python3
	Python 3.1.3 (r313:86834, Nov 28 2010, 10:01:07)
	[GCC 4.4.5] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import cbstats
	>>> help(cbstats)

## Get the code

[jwandborg/cbstats](//github.com/jwandborg/cbstats) on GitHub, or
	
	git clone git://github.com/jwandborg/cbstats

## Known issues

[Large server.log file](https://github.com/jwandborg/cbstats/issues/1).

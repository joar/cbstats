cbstats - CraftBukkit Stats
===========================

Author: Joar Wandborg <http://github.com/jwandborg>

*	`cbstats` outputs usage statistics for your server based on your server log.  

*	`cbstats` is neither a plugin nor a mod for CraftBukkit.

Installation
------------

1.	`pip install cbstats` or `pip install cbstats --upgrade`, or, to install from this source `python3 setup.py install`
2.	To use the library, to something like this:

	$ python3
	Python 3.1.3 (r313:86834, Nov 28 2010, 10:01:07)
	[GCC 4.4.5] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from cbstats import CraftBukkitStats
	>>> stats = CraftBukkitStats('/home/jwandborg/bukkit-1.3/') # craftbukkit.jar folder
	>>> help(stats)
	>>>


Known issues
------------

*	As your server log increases in size, the time and memory needed by cbstats will too.
	**See [#1](https://github.com/jwandborg/cbstats/issues/1)**.

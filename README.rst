cbstats - CraftBukkit Stats
===========================

Author: Joar Wandborg http://github.com/jwandborg


-  ``cbstats`` outputs usage statistics for your server based on
   your server log.

-  ``cbstats`` is neither a plugin nor a mod for CraftBukkit.


Example
-------

`Live example <http://mc.wandborg.se/serverstats.txt>`_

Plain text:

::

      # Server stats for mc.wandborg.se
    
      Operators: raidonrai, jwandborg, rocketseed, rscott147
    
      Online right now: 
    
      Average user session length: 0:27:26
    
      # Toplist - Time online
    
      15:58:41 rscott147
      11:06:18 jwandborg
      7:57:00 rocketseed
      2:51:05 dushkin
      2:29:39 neuemod
      1:18:19 SmiJa
      1:17:43 Dennet
      0:50:24 retro_grade
      0:06:05 omnidonk
      0:05:26 ErrorOfRuto
      0:03:01 robnowelljr
      0:02:51 SerfaBoy
      0:01:46 macktns
      0:01:41 Dazaki
    
      # Configuration
    
      online-mode: true
      pvp: true
      spawn-monsters: false
      spawn-protection: 16
      max-players: 20
      spawn-animals: true
      white-list: false
      level-name: worlds/Reddit
      server-ip: 
      server-port: 25565
      hellworld: false

Installation
------------


1. ``pip install cbstats`` or ``pip install cbstats --upgrade``,
   or, to install from this source ``python3 setup.py install``
2. Use the python ``help`` function to get a description of the
   package.

   ::

       $ python3
       Python 3.1.3 (r313:86834, Nov 28 2010, 10:01:07)
       [GCC 4.4.5] on linux2
       Type "help", "copyright", "credits" or "license" for more information.
       >>> from cbstats import CraftBukkitStats
       >>> stats = CraftBukkitStats('/home/jwandborg/bukkit-1.3/') # craftbukkit.jar folder
       >>> help(stats)
       [...]


Known issues
------------


-  As your server log increases in size, the time and memory needed
   by cbstats will too.
   **See `#1 <https://github.com/jwandborg/cbstats/issues/1>`_**.



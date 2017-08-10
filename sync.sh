#!/bin/bash
rsync -Pz voteit@sfsfum.voteit.se:~/srv/sfsfum_buildout/var/Data.fs var/Data.fs
rsync -Pzr voteit@sfsfum.voteit.se:~/srv/sfsfum_buildout/var/blob var/.

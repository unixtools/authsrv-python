#!/usr/bin/env python

import authsrv

# Will fast exit, but will validate module can load
x = authsrv.fetch()

# Expected to fail, but will actually call out to the utilities
# Each request should only show up in syslog once since the lookup(failure) should be cached in authsrv module
x = authsrv.fetch(user="test", instance="a")
x = authsrv.fetch(user="test", instance="b")
x = authsrv.fetch(user="test", instance="a")
x = authsrv.fetch(user="test", instance="b")

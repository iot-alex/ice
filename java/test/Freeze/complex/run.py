#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2004 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

import os, sys

for toplevel in [".", "..", "../..", "../../..", "../../../.."]:
    toplevel = os.path.normpath(toplevel)
    if os.path.exists(os.path.join(toplevel, "config", "TestUtil.py")):
        break
else:
    raise "can't find toplevel directory!"

sys.path.append(os.path.join(toplevel, "config"))
import TestUtil

name = os.path.join("Freeze", "complex")
testdir = os.path.join(toplevel, "test", name)
os.environ["CLASSPATH"] = os.path.join(testdir, "classes") + TestUtil.sep + os.getenv("CLASSPATH", "")

#
# Clean the contents of the database directory.
#
dbdir = os.path.join(testdir, "db")
TestUtil.cleanDbDir(dbdir)

client = "java -ea Client"

print "starting populate...",
populatePipe = os.popen(client + TestUtil.clientOptions + " --dbdir " + testdir + " populate" + " 2>&1", "r", 0)
print "ok"

TestUtil.printOutputFromPipe(populatePipe)

populateStatus = populatePipe.close()

if populateStatus:
    sys.exit(1)

print "starting verification client...",
clientPipe = os.popen(client + TestUtil.clientOptions + " --dbdir " + testdir + " validate" + " 2>&1", "r", 0)
print "ok"

TestUtil.printOutputFromPipe(clientPipe)

clientStatus = clientPipe.close()

if clientStatus:
    sys.exit(1)

sys.exit(0)

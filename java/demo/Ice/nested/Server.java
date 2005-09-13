// **********************************************************************
//
// Copyright (c) 2003-2005 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

import Demo.*;

public class Server extends Ice.Application
{
    public int
    run(String[] args)
    {
        Ice.ObjectAdapter adapter = communicator().createObjectAdapter("Nested.Server");
        NestedPrx self = NestedPrxHelper.uncheckedCast(adapter.createProxy(Ice.Util.stringToIdentity("nestedServer")));
        adapter.add(new NestedI(self), Ice.Util.stringToIdentity("nestedServer"));
        adapter.activate();
        communicator().waitForShutdown();
        return 0;
    }

    public static void
    main(String[] args)
    {
        Server app = new Server();
        int status = app.main("Server", args, "config");
        System.exit(status);
    }
}

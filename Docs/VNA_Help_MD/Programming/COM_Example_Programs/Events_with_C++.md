# Events with C++

* * *

The following code, along with the Header file, shows how to use the VNA
Events.

[Download the Header file
'preventcatcher.h'](../../assets/misc/Programming/pnaeventcatcher.h)

#include <atlbase.h>

#include <atlcom.h>

#include <iostream>

#import "835x.tlb" no_namespace,raw_interfaces_only,named_guids

#include "pnaeventcatcher.h"

inline void HR(HRESULT hr)

{

if (FAILED(hr))

throw hr;

}

class MyEventCatcher : public CPNAEventCatcher

{

public:

MyEventCatcher()

{

CoInitialize(NULL);

CComPtr<IApplication> app;

HR(app.CoCreateInstance(CLSID_Application));

CPNAEventCatcher::SubscribeCatcher(app);

HR(app->AllowAllEvents());

}

~MyEventCatcher()

{

CPNAEventCatcher::Release();

CoUninitialize();

}

virtual void OnMeasurementEvent(long eventID,long measurementNumber) {}

virtual void OnChannelEvent(long eventID,long ch)

{

if (eventID == 0x68070709L) //MSG_ALL_SWEEPS_COMPLETED_AND_PROCESSED

{

static int i =0;

++i;

std::cout << "Sweep:" << i << std::endl;

}

}

};

\----------------------------

In a .cpp file, (just like most ATL projects) you must have a declared an
instance of CComModule. This will work:

CComModule _Module;

\-----------------------------

Remember that you are now the "Server" and the VNA is the Client. That makes
DCOM a bit complicated.

This code was tested in VS2005 using a wizard generated MFC MDI project.

* * *


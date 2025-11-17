# Programming the VNA with C++

* * *

The programming information contained in this Help system is aimed at the
Visual Basic programmer. VB does a lot of work for the programmer when it
comes to managing and accessing components. Using a lower level language like
C++ requires a more thorough understanding of the underlying tenets of COM. It
is not the intent of this section to teach COM programming. The following is
intended to acquaint you with some of the basic concepts you need to know in
order to program against COM.

  * [Initializing COM](c%2b%2b_and_the_com_interface.md#init)

  * [Importing the Type Library](c%2b%2b_and_the_com_interface.md#imp)

  * [Creating the Application Object](c%2b%2b_and_the_com_interface.md#app)

  * [Errors](c%2b%2b_and_the_com_interface.md#error)

  * [Events](c%2b%2b_and_the_com_interface.md#events)

  * [Additional Reading](c%2b%2b_and_the_com_interface.md#read)

  * [Example](c%2b%2b_and_the_com_interface.md#ex)

Note: The information in this section assumes development on a Windows OS
using Microsoft tools.

[Other Topics about COM Concepts](Learning_about_COM.md)

### Initializing COM

The first thing you must do before performing any COM transactions is to
initialize the COM library. You can do this in a number of ways. The most
basic of these is a call to CoInitialize( ) or CoIntializeEx( ). Alternatively
you can use the MFC (Microsoft Foundation Classes) AfxOleInit( ).

Conversely, before your program exits you must uninitialize COM. You can
accomplish this with CoUninitialize( ) or the MFC routine AfxOleTerm( ).

* * *

### Importing the Type Library

To make a component available to the client, the server exports what is called
the type library. For the VNA, this file is 835x.tlb. It is located on the
VNA's hard drive at C:\Program Files(x86)\ Keysight\Network
Analyzer\Automation. See [Configure for COM-DCOM
Programming](Configure_for_COM-DCOM_Programming.htm).

The type library can be read and deciphered using another COM interface called
ITypeLib. VB uses this interface to present, for example, its object browser.
Visual C++ can also read type libraries. This is done by importing the type
library into your project with a compiler directive:

#import "C:\Program Files\Common Files\Keysight\Pna\835x.tlb", named_guids

When you compile your program with this statement in it, the compiler creates
two other files: 835x.tlh and 835x.tli. The first is a header file that
contains the type definitions for the VNA's COM interfaces and their methods.
The second file contains inline functions that wrap the VNA's interface
methods. The wrappers are beneficial in that they contain error reporting for
each of the method calls.

The .tlh file defines a smart pointer which you can use to access the VNA's
objects. The smart pointer definition looks like this:

_com_smartptr_typedef(Iapplication, _uuidof(Iapplication))

A smart pointer is a term used for a C++ object that encapsulates a pointer
used to refer to a COM object. All COM objects derive from the interface
IUnknown. This interface has three methods: QueryInterface( ), AddRef( ), and
Release( ). The function of the AddRef and Release methods is to maintain a
reference count on the object and thus control the object's lifetime. Anytime
you copy or create a reference to a COM object, you are responsible for
incrementing its reference count. And likewise, when you are finished using
that reference, it is your responsibility to Release it. Smart pointers do
this work for you, as shown in the [example
program](c%2b%2b_and_the_com_interface.htm#ex). In addition, smart pointers
will also perform the QueryInterface call when required. QueryInterface is a
method that requests a specific interface from an object. In the example
program we gain access to the IArrayTransfer interface of the Measurement
object. In the ReadMethod routine, we see this:

PTransferData = pMeas;

The assignment operator is overloaded for the smart pointer and in reality,
this simple statement does this:

HRESULT hr = pMeas->QueryInterface(
IID_IArrayTransfer,(void**)&pTransferData);

Using the existing interface pointer (pMeas) to the object, this call asks the
object if it supports the IArrayTransfer interface, and if so to return a
pointer to it in pTransferData. Smart pointer makes life easier for the C++
programmer. Read more about smart pointers in Microsoft Developer's Network
Library (MSDN).

* * *

### Creating the Application Object

The only createable object exported by the VNA is the [Application
object](../COM_Reference/Objects/Application_Object.htm). Typically this would
be done with a call to CoCreateInstance:

STDAPI CoCreateInstance(  
CLSID__IApplication, //Class identifier (CLSID) of the object  
NULL, //Pointer to controlling IUnknown  
CLS_CTX_SERVER, //Context for running executable code  
IID_IApplication, //Reference to the IID of the interface  
(void**)&pNA //Address of output variable that receives  
// the interface pointer requested in riid  
);

With the smart pointer, this is taken care of with the following call:

IApplicationPtr pNA; // declare the smart pointer  
pNA = IApplicationPtr("AgilentPNA835x.Application.1");

* * *

### Errors

All COM method calls are required to return an HRESULT. This is 32 bit long
with a specific format.

  * The most significant bit indicates success(0) or failure(1).

  * The lower 16 bits indicate the specific failure.

Visual Basic strips off the returned HRESULT and raises an error object for
non-successful returns. The C++ programmer must himself be diligent about
handling errors. You must check the return value of each COM call to ensure
its success.

* * *

### Events

The Application object sources the INetworkAnalyzerEvents interface. This
object is the source for all events. To use events in C++, you must do two
things:

  1. Implement the INetworkAnalyzerEvents interface - derive an object from INetworkAnalyzerEvents and implement the methods described there.

  2. Subscribe to the IconnectionPoint interface of the Application object. - obtain a pointer to the IConnectionPointContainer interface of the Application object and making the following request:

FindConnectionPoint( IID_InetworkAnalyzerEvents, &pConnection );

A successful call to this interface will return a valid pointer in
pConnection. Use this pointer to subscribe to the Application object:

pConnect->Advise( IUnknown* punk, DWORD dwCookie);

This call provides the server object with a callback address. The Iunkown
pointer in this call is the IUnkown pointer of the object that implements the
INetworkAnalyzerEvents interface. This is the event sink. The application
object needs a pointer to this object in order to call your interface when an
event occurs. The dwCookie is your subscription key. Use it to unsubscribe
(see Unadvise( ) ).

* * *

### Additional Reading

"MSDN" \- Microsoft Developer's Network Library

"Learning DCOM", by Thuan L. Thai, published by O'Reilly(1999)

"Inside COM", by Dale Rogerson, published by Microsoft Press (1997)

"Understanding ActiveX and OLE", by David Chappell, also published by
Microsoft Press (1996)

"Beginning ATL COM Programming", published by Wrox Press (1998)

* * *

### Example

The example uses the smart pointer created by Microsoft Visual Studio. The
calls to CoInitialize and CoUninitialize open and close the COM libraries. In
the example, notice that the pointers local to the main routine are explicitly
released. When smart pointers go out of scope, they will perform this duty
implicitly. However, we are calling CoUninitialize before they have the chance
to be destroyed, so we are obliged to release them.

See the [example](../COM_Example_Programs/C_Example.md) program.

* * *


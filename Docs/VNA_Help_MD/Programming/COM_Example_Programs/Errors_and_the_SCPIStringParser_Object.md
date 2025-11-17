# Errors and the SCPIStringParser Object

* * *

This C++ program uses the
[SCPIStringParser.Parse](../COM_Reference/Methods/Parse_Method.md) command to
detect the failed HRESULT and interrogate the errorInfo object for more
details.

// scpierrors.cpp : Defines the entry point for the console application.

//

#include <iostream>

#include "afx.h"

#include "atlbase.h"

#import "C:\program files(x86)\Keysight\Network Analyzer\Automation\835x.tlb"
raw_interfaces_only, no_namespace, named_guids

using namespace std;

HRESULT SendScpiCommand( IScpiStringParser* parser, CComBSTR& cmd, CComBSTR&
response)

{

CComBSTR bstr;

HRESULT hr = parser->Parse(CComBSTR(cmd), &response);

if (FAILED(hr))

{

// see if this interface supports ErrInfo

CComPtr<ISupportErrorInfo> spSupportsErrInfo;

if (SUCCEEDED(parser->QueryInterface(&spSupportsErrInfo)))

{

// it does, so let's get the errorinfo object

CComPtr<IErrorInfo> spErrorInfo;

if (SUCCEEDED(GetErrorInfo(0, &spErrorInfo)))

{

CComBSTR errStr;

spErrorInfo->GetDescription(&errStr);

std::cout << "ERROR: " << CString(errStr) << std::endl;

}

}

}

return hr;

}

int main()

{

CoInitialize(NULL);

{

CComBSTR response;

CComPtr<IApplication> spPNA;

CComPtr<IScpiStringParser> spSCPI;

if (SUCCEEDED(spPNA.CoCreateInstance(CLSID_Application)))

{

spPNA->get_ScpiStringParser(&spSCPI);

SendScpiCommand(spSCPI, CComBSTR("SYSTEM:PRESET"), response);

SendScpiCommand(spSCPI, CComBSTR("CALC:PAR:CAT?"), response);

std::cout << CString(response) << std::endl;

SendScpiCommand(spSCPI, CComBSTR("THIS:IS:A:SYNTAX:ERROR"), response);

}

}

CoUninitialize();

return 0;

}


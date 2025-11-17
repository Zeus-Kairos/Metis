## C++ Example

* * *

The following example uses the smart pointer created by Microsoft Visual
Studio. The calls to CoInitialize and CoUninitialize open and close the COM
libraries.

Also notice that the pointers local to the main routine are explicitly
released. When smart pointers go out of scope, they will perform this duty
implicitly. However, we are calling CoUninitialize before they have the chance
to be destroyed, so we are obliged to release them.

* * *

// An example program to illustrate the use of #import to bind to the  
// PNA type library.  
//

#ifndef _UNICODE

#define _UNICODE

#endif

#include "stdafx.h"  
#include "stdio.h"  
#include "math.h"  
  
/////////////////////////////////////////////  
// import the network analyzer type library  
/////////////////////////////////////////////  
#import "C:\Program Files\Common Files\Keysight\Pna\835x.tlb" no_namespace,
named_guids  
/////////////////////////////////////////////  
// include the error definitions for the PNA so we can implement  
// error handling.  
/////////////////////////////////////////////  
#include "C:\Program Files\Common Files\Keysight\Pna\errorsystemmessage.h"  
  
IApplicationPtr pNA; // top level application pointer  
float fScalarData [1601]; // global buffer for data retrieval  
float fScalarData2[1601];  
  
DWORD dwCookie;  
  
/////////////////////////////////////////////  
// SetupChannel:  
//  
// input: pointer to the channel  
//  
// function: sets properties on the channel  
/////////////////////////////////////////////  
void SetupChannel(IChannelPtr pChannel)  
{  
pChannel->put_StartFrequency( 1.2E9 );  
pChannel->put_StopFrequency ( 4.2E9 );  
pChannel->put_NumberOfPoints ( 201);  
  
}  
  
/////////////////////////////////////////////  
// AcquireData:  
//  
// input: pointer to the channel  
//  
// function: single sweeps the channel  
/////////////////////////////////////////////  
void AcquireData( IChannelPtr pChannel )  
{  
pChannel->Single( TRUE );  
}  
  
/////////////////////////////////////////////  
// ReadData:  
//  
// input: pointer to the Measurement object  
//  
// function: reads data from the measurment's formatted  
// result data buffer  
/////////////////////////////////////////////  
void ReadScalarData(IMeasurementPtr pMeas )  
{  
IArrayTransferPtr pDataTransfer;  
pDataTransfer = pMeas;  
long numVals = 1601;  
float* pData = fScalarData;  
  
if(pDataTransfer){  
  
pDataTransfer->getScalar( naMeasResult, naDataFormat_LogMag, &numVals, pData);  
  
for (int i = 0; i < numVals; i++)  
printf("%d/t%f/n",i,pData[i]);  
}  
TCHAR msg[100];  
BSTR param;  
pMeas->get_Parameter(&param);  
swprintf(msg,L"Review %s data",param);  
MessageBox(NULL,msg,L"User Message",0);  
::SysFreeString(param);  
}  
  
  
void ReadComplexData(IMeasurementPtr pMeas )  
{  
IArrayTransferPtr pDataTransfer;  
pDataTransfer = pMeas;  
long numVals = 1601;  
float* pReal= fScalarData;  
float* pImag = fScalarData2;  
  
if(pDataTransfer){  
  
pDataTransfer->getPairedData( naRawData, naRealImaginary, &numVals, pReal,
pImag);  
  
for (int i = 0; i < numVals; i++)  
printf("%d/t%f/t%f/n",i,pReal[i], pImag[i]);  
}  
TCHAR msg[100];  
BSTR param;  
pMeas->get_Parameter(&param);  
swprintf(msg,L"Review %s data",param);  
MessageBox(NULL,msg,L"User Message",0);  
::SysFreeString(param);  
}  
/////////////////////////////////////////////  
// PutData:  
//  
// input: pointer to the Measurement object  
//  
// function: writes data to the measurement's raw data  
// buffer  
/////////////////////////////////////////////  
void PutData( IMeasurementPtr pMeas )  
{  
IArrayTransferPtr pDataTransfer;  
pDataTransfer = pMeas;  
long numVals = 201;  
  
if(pDataTransfer){  
  
NAComplex* pComplex = new NAComplex[numVals];  
  
pComplex[0].Im = 0;  
pComplex[0].Re = 1;  
for (int i = 1; i < numVals; i++)  
{  
pComplex[i].Im = (float)sin(i)/i;  
pComplex[i].Re = (float)cos(i)/i;  
}  
  
pDataTransfer->putNAComplex( naRawData, numVals, pComplex,
naDataFormat_Polar);  
delete [] pComplex;  
}  
}  
  
/////////////////////////////////////////////  
// printError  
/////////////////////////////////////////////  
void printError( HRESULT hr)  
{  
BSTR text;  
  
hr = pNA->get_MessageText ((NAEventID) hr, &text);  
MessageBox(NULL,text,L"Network Analyzer error",0);  
::SysFreeString(text);  
}  
  
  
/////////////////////////////////////////////  
// main  
/////////////////////////////////////////////  
int main(int argc, char* argv[])  
{  
HRESULT hr;  
const long channel1 = 1;  
const long window1 = 1;  
const long srcport = 1;  
IMeasurementPtr pMeasurement;  
IChannelPtr pChannel;  
  
// initialize COM libraries  
CoInitialize(NULL);  
  
try {  
pNA = IApplicationPtr("AgilentPNA835x.Application.1");  
  
pNA->put_Visible(TRUE);  
pNA->Reset();  
  
  
pNA->CreateMeasurement (channel1, "S21",srcport, 3);  
hr = pNA->get_ActiveChannel( &pChannel);  
  
if (SUCCEEDED (hr))  
{  
SetupChannel( pChannel);  
AcquireData(pChannel);  
}  
  
hr= pNA->get_ActiveMeasurement( &pMeasurement);  
if (SUCCEEDED(hr))  
{  
pMeasurement->put_Format( naDataFormat_Polar);  
ReadScalarData( pMeasurement);  
ReadComplexData( pMeasurement);  
PutData(pMeasurement);  
}  
if (FAILED(hr))  
{  
printError(hr);  
}  
  
// make sure to release the remaining pointers  
// before calling CoUninitialize  
  
pMeasurement.Release();  
pChannel.Release();  
pNA.Release();  
}  
catch (_com_error err)  
{  
printError( err.Error() );  
}  
  
CoUninitialize();  
return 0;  
}

* * *


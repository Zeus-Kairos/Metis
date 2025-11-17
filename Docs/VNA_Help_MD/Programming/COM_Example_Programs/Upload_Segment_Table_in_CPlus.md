## Upload a Segment Table using C++

* * *

This example program shows the Variant method for uploading a segment sweep to
the VNA using the
[SetAllSegments](../COM_Reference/Methods/SetAllSegments_Method.md) method

#include "stdafx.h"

#include <stdio.h>

#include "atlbase.h"

#include "objbase.h"

// import the VNA type library

//----------------------------------------------------------------------------------

#import "C:\Program Files(x86)\Common Files\Keysight\PNA\835x.tlb"
no_namespace, named_guids

int _tmain(int argc, _TCHAR* argv[])

{

// interface pointers to retrieve COM interfaces

HRESULT hr;

IUnknown* pUnk = 0;

IApplication* pNA = 0;

IChannel* pChan = 0;

IMeasurement* pMeas = 0;

IMeasurement5* pMeas5 = 0;

IArrayTransfer* pTrans = 0;

ISegments* pSeg = 0;

ISegments2* pSeg2 = 0;

//Variables for X and Y data read portion

SAFEARRAY* sArray;

_variant_t vXVals;

double HUGEP* xVals;

float* pScalarData;

//Variables for Segment portion

double Fstart, Fstop, SegWidth;

long i[2];

int num_points = 11;

SAFEARRAY* pSA;

VARIANT vSeg;

VARIANT v;

int NUM_SEGS = 10;

int SEG_SIZE = 7;

//Create SafeArray to hold the segment data

SAFEARRAYBOUND aDim[2]; //This must be 2 the VNA expects to see a 2
dimensional array

aDim[0].lLbound = 0;

aDim[0].cElements = SEG_SIZE; //This will be set to 7 unless port power is
uncoupled

aDim[1].lLbound = 0;

aDim[1].cElements = NUM_SEGS;

pSA= SafeArrayCreate(VT_VARIANT,2,aDim); //The cDim parameter must be set to 2
as the VNA expects a 2D array

//Init Variant to set values in Safearray

VariantInit(&vSeg);

Fstart=10e6;

Fstop=3e9;

SegWidth=(Fstop-Fstart)/NUM_SEGS;

//Loop to write segment data

for(int j=0; j<NUM_SEGS; ++j)

{

i[1]=j; //Set Segment #

//Segment Definition

i[0] = 0;

vSeg.vt = VT_BOOL; //First parameter is Boolean

vSeg.boolVal = VARIANT_TRUE; //Segment State

SafeArrayPutElement(pSA, i, &vSeg);

i[0] += 1;

vSeg.vt = VT_I4; //Second parameter is an integer

vSeg.intVal = num_points; //Number of Points

SafeArrayPutElement(pSA, i, &vSeg);

i[0] += 1;

vSeg.vt = VT_R8; //Remaining parameters are of type double

vSeg.dblVal = Fstart+j*SegWidth; //Start Frequency

SafeArrayPutElement(pSA, i, &vSeg);

i[0] += 1;

vSeg.dblVal=vSeg.dblVal+SegWidth; //Stop Frequency

SafeArrayPutElement(pSA, i, &vSeg);

i[0] += 1;

vSeg.dblVal = 1.0e3; //IF Bandwidth

SafeArrayPutElement(pSA, i, &vSeg);

i[0] += 1;

vSeg.dblVal = 0.0; //Dwell time

SafeArrayPutElement(pSA, i, &vSeg);

i[0] += 1;

vSeg.dblVal = -5.0; //Power

SafeArrayPutElement(pSA, i, &vSeg);

}

//vSeg no longer needed, clean up

VariantClear(&vSeg);

//Declare Variant to use with Segment data

VariantInit(&v);

v.vt = VT_ARRAY|VT_VARIANT;

v.parray = pSA; //write safearray to variant

// Initialize the COM subsystem

CoInitialize(NULL);

CoInitializeSecurity(NULL, //security descriptor

-1, // authn svc entries

NULL, // authn svcs

NULL, // reserved

RPC_C_AUTHN_LEVEL_NONE,

RPC_C_IMP_LEVEL_IMPERSONATE,

NULL, // authn info

0, // capabilities

NULL); // reserved

// Create an instance of the network analyzer

// Request the NA's IUnknown interface

hr = CoCreateInstance(CLSID_Application,0,CLSCTX_ALL,IID_IUnknown, (void**)
&pUnk);

if (!FAILED(hr))

{

// QueryInterface for the INetworkAnalyzer interface of the NetworkAnalyzer
object

hr = pUnk->QueryInterface(IID_IApplication,(void**)&pNA);

if (!FAILED(hr))

{

// Reset the analyzer to instrument preset

pNA->Reset();

// Create S11 measurement

pNA->CreateSParameter(1,1,1,1);

// Set pChan variable to point to the active channel

pNA->get_ActiveChannel(&pChan);

//Show Segment table

pNA->NAWindows->Item(1)->ShowTable((NATableType)2);

//Get handle to ISegments Interface

pChan->get_Segments(&pSeg);

//Get handle to ISegments2 Interface

hr = pSeg->QueryInterface(IID_ISegments2, (void**)&pSeg2);

//Set Segment Sweep Options

pSeg2->IFBandwidthOption = VARIANT_TRUE;

pSeg2->SourcePowerOption = VARIANT_TRUE;

//Push segments to VNA

pSeg2->SetAllSegments(v);

//Set Sweep Type to Segment Sweep

pChan->SweepType = naSegmentSweep;

if (pChan)

{

// Set pMeas variable to point to the active measurement

pNA->get_ActiveMeasurement(&pMeas);

if(pMeas)

{

// Setup the channel for a single trigger

pChan->Hold(true);

pNA->TriggerSignal = naTriggerManual;

pChan->TriggerMode = naTriggerModeMeasurement;

// Make the VNA application visible

pNA->put_Visible(true);

// Send a manual trigger to initiate a single sweep

pChan->Single(true);

// QueryInterface for the IArrayTransfer interface of the NetworkAnalyzer
object

hr = pMeas->QueryInterface(IID_IArrayTransfer,(void**)&pTrans);

// Get handle for IMeasurement5 interface

hr = pMeas->QueryInterface(IID_IMeasurement5, (void**)&pMeas5);

if (!FAILED(hr))

{

int val = num_points*NUM_SEGS;

// Store the data in the "result" variable

pScalarData = new float[val];

xVals = new double[val*2];

//Get X axis values

vXVals=pMeas5->GetXAxisValues();

//Convert _variant_t array to a SAFEARRAY

sArray = vXVals.parray;

//Convert data from SAFEARRAY to double array. Each SAFEARRAY value

//is 16 bytes so it takes up 2 floats so the xVals size is double

//the number of points. This also means that every other data point

//in the resulting array can be discarded.

hr = SafeArrayAccessData(sArray, (void HUGEP**)&xVals);

//Get Measurement Values

pTrans->getScalar(naRawData, naDataFormat_LogMag, (long *)&val, pScalarData);

// Display the result

printf("S11(dB) \- Visual C++ COM Example for PNA operating in segment sweep
mode/n/n");

for (int j = 0; j < val; j++)

{

//Write value...the xVals array is offset by 1 in each data point since

//the return data is 16 bytes and each double is 8.

printf("%.3lf GHz, %.4f/n",xVals[2*j+1]/1e9, pScalarData[j]);

}

}

}

}

}

else

{

printf("Programmed failed to connect to the PNA.");

}

}

CoUninitialize();

system("PAUSE");

return 0;

}


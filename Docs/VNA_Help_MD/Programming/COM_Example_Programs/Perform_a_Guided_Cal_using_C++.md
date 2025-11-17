# Perform a Guided Calibration using C++

* * *

This example uses the
[GuidedCalibration](../COM_Reference/Objects/GuidedCalibration_Object.md)
interface to perform a 4 port Guided Calibration using 4 Thru paths and the
Unknown Thru Algorithm.

This example was tested using a N5242A with A.09.42.10 firmware.

Learn more about [Reading and Writing Calibration data using
COM.](../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)

[See Other COM Example Programs](COM_Example_Intro.md)

#include <afxdisp.h> #include <stdio.h> #include "atlbase.h" #include
"objbase.h" // import the VNA type library
//----------------------------------------------------------------------------------
#import "C:\Program Files(x86)\Keysight\Network Analyzer\Automation\835x.tlb"
no_namespace, named_guids int _tmain(int argc, _TCHAR* argv[]) { // interface
pointers to retrieve COM interfaces IUnknown* pUnk = 0;  IApplication* pNA =
0; IApplication9* pNA9 = 0; IChannel* pChan = 0; IMeasurement* pMeas = 0;
IArrayTransfer* pTrans = 0; ITriggerSetup* pTrig = 0; ICalManager* pCalMgr =
0; ICalManager3* pCalMgr3 = 0; IGuidedCalibration* pGuidedCal = 0;
IGuidedCalibration6* pGuidedCal6 = 0; VARIANT thruList; COleSafeArray sa; long
thrus[8]={1,2,1,4,2,3,3,4}; long i, num_points = 0, numSteps=0; float*
pScalarData; HRESULT hr; // Initialize the COM subsystem CoInitialize(NULL);
CoInitializeSecurity(NULL, //security descriptor -1, // authn svc entries
NULL, // authn svcs NULL, // reserved RPC_C_AUTHN_LEVEL_NONE,
RPC_C_IMP_LEVEL_IMPERSONATE, NULL, // authn info 0, // capabilities NULL); //
reserved // Create an instance of the network analyzer // Request the NA's
IUnknown interface hr =
CoCreateInstance(CLSID_Application,0,CLSCTX_ALL,IID_IUnknown, (void**) &pUnk);
if (!FAILED(hr)) { // QueryInterface for the INetworkAnalyzer interface of the
NetworkAnalyzer object hr =
pUnk->QueryInterface(IID_IApplication,(void**)&pNA); if (!FAILED(hr)) { //
Reset the analyzer to instrument preset pNA->Reset(); // Create S11
measurement pNA->CreateSParameter(1,1,1,1); // Set pChan variable to point to
the active channel pNA->get_ActiveChannel(&pChan); if (pChan) { // Set pMeas
variable to point to the active measurement
pNA->get_ActiveMeasurement(&pMeas); // Make the VNA application visible
pNA->put_Visible(true); // Set channel parameters pChan->NumberOfPoints = 11;
pChan->put_StartFrequency(3.0e9); pChan->put_FrequencySpan(4.0e9);
pChan->put_IFBandwidth(1.0e3); pChan->put_SweepGenerationMode(naSteppedSweep);
// Get CalManager3 Access and GuidedCalibration access
hr=pNA->raw_GetCalManager(&pCalMgr);
hr=pCalMgr->QueryInterface(IID_ICalManager3, (void**)&pCalMgr3);
pCalMgr3->get_GuidedCalibration((IDispatch**)&pGuidedCal);
hr=pGuidedCal->QueryInterface(IID_IGuidedCalibration6, (void**)&pGuidedCal6);
// Initialize the Guided Calibration Process pGuidedCal6->Initialize(1,
VARIANT_TRUE); // Set Port Connectors pGuidedCal6->put_ConnectorType(1,
(_bstr_t) "APC 3.5 female"); pGuidedCal6->put_ConnectorType(2, (_bstr_t) "APC
3.5 female"); pGuidedCal6->put_ConnectorType(3, (_bstr_t) "APC 3.5 female");
pGuidedCal6->put_ConnectorType(4, (_bstr_t) "APC 3.5 female"); // Set Cal Kit
pGuidedCal6->put_CalKitType(1, (_bstr_t) "85052D");
pGuidedCal6->put_CalKitType(2, (_bstr_t) "85052D");
pGuidedCal6->put_CalKitType(3, (_bstr_t) "85052D");
pGuidedCal6->put_CalKitType(4, (_bstr_t) "85052D"); // Convert thrus to
VARIANT sa.CreateOneDim(VT_I4, sizeof(thrus)/sizeof(long), thrus, 0);
thruList=sa.Detach(); // Set Thru Port List
pGuidedCal6->put_ThruPortList(thruList); // Set Thru Path Calibration Types
pGuidedCal6->put_PathCalMethod(1, 2, (_bstr_t) "SOLT");
pGuidedCal6->put_PathCalMethod(1, 4, (_bstr_t) "SOLT");
pGuidedCal6->put_PathCalMethod(2, 3, (_bstr_t) "SOLT");
pGuidedCal6->put_PathCalMethod(3, 4, (_bstr_t) "SOLT"); // Set Thru Cal Method
pGuidedCal6->put_PathThruMethod(1, 2, (_bstr_t) "Undefined Thru");
pGuidedCal6->put_PathThruMethod(1, 4, (_bstr_t) "Undefined Thru");
pGuidedCal6->put_PathThruMethod(2, 3, (_bstr_t) "Undefined Thru");
pGuidedCal6->put_PathThruMethod(3, 4, (_bstr_t) "Undefined Thru");
//Initialize after modifying the SmartCal logic pGuidedCal6->Initialize(1,
VARIANT_TRUE); // Generate Calibration Steps
numSteps=pGuidedCal6->GenerateSteps(); printf("Number of Calibration Steps =
%ld/n/n", numSteps); // Collect calibration steps for(i=0; i<numSteps; i++) {
printf("Step %d >>> %s /n ",i+1, (char
*)pGuidedCal6->GetStepDescription(i+1)); system("PAUSE");
pGuidedCal6->AcquireStep(i+1); } // Complete Calibration by Generating Error
Terms pGuidedCal6->GenerateErrorTerms(); if(pMeas) { //Get handle to
IApplication9 hr = pNA->QueryInterface(IID_IApplication9, (void**)&pNA9);
//Get handle to ITriggerSetup pNA9->get_TriggerSetup(&pTrig); // Setup the
channel for a single trigger pChan->Hold(true); pTrig->Source =
naTriggerSourceInternal; pNA->TriggerSignal = naTriggerManual;
pChan->TriggerMode = naTriggerModeMeasurement; // Send a manual trigger to
initiate a single sweep pChan->Single(true); // QueryInterface for the
IArrayTransfer interface of the NetworkAnalyzer object hr =
pMeas->QueryInterface(IID_IArrayTransfer,(void**)&pTrans); if (!FAILED(hr)) {
// Store the data in the "result" variable num_points = pChan->NumberOfPoints;
pScalarData = new float[num_points]; //Get Measurement Values
pTrans->getScalar(naCorrectedData, naDataFormat_LogMag, &num_points,
pScalarData); // Display the result printf("/nSingle Sweep S11 Data:/n"); for
(i = 0; i < num_points; i++) { //Write value... printf("%f/n",
pScalarData[i]); } } } } sa.Destroy(); delete [] pScalarData; pUnk->Release();
pMeas->Release(); pChan->Release(); pTrans->Release(); pCalMgr->Release();
pCalMgr3->Release(); pGuidedCal->Release(); pGuidedCal6->Release();
pTrig->Release(); pNA9->Release(); pNA->Release(); } else { printf("Programmed
failed to connect to the PNA."); } } CoUninitialize(); system("PAUSE"); return
0; }  
---  
  
* * *

* * *


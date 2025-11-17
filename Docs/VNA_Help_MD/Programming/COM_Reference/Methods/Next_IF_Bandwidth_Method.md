##### Write-only

|

##### [About Dynamic Range](../../../S2_Opt/Dyn_Rge.md)  
  
---|---  
  
## NextIFBandwidth Method

* * *

#### Description

|  A function that returns the Next higher IF Bandwidth value. Use to retrieve
the list of available IFBandwidth settings.  
---|---  
  
####  VB Syntax

|  chan.Next_IFBandwidth bw  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A Channel (object)  
bw |  (double) - The argument that you use to send an IFBandwidth. The function uses this argument to return the Next higher IFbandwidth.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Public pnbw As Double 'declare variable outside of procedure pnBW =
chan.IFBandwidth 'put the current IFBW in pnBW  
chan.Next_IFBandwidth pnBW 'function returns the Next higher IFBandwidth.  
chan.IFBandwidth = pnBW 'set IFBW to the Next value  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Next_IFBandwidth (double *pVal)  
  
#### Interface

|  IChannel


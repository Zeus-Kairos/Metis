##### Write-only

|

##### [About Dynamic Range](../../../S2_Opt/Dyn_Rge.md)  
  
---|---  
  
## PreviousIFBandwidth Method

* * *

#### Description

|  A function that returns the previous IF Bandwidth value. Use to retrieve
the list of available IFBandwidth settings.  
---|---  
  
####  VB Syntax

|  chan.Previous_IFBandwidth bw  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A Channel (object)  
bw |  (double) - The argument that you use to send an IFBandwidth. The function uses this argument to return the previous IFbandwidth.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Public pnbw As Double 'declare variable outside of procedure PreBW =
chan.IFBandwidth 'put the current IFBW in PreBW  
chan.Previous_IFBandwidth PreBW 'function returns the Previous IFBandwidth of
the current one.  
chan.IFBandwidth = PreBW 'set IFBW to the previous value  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Previous_IFBandwidth (double *pVal)  
  
#### Interface

|  IChannel


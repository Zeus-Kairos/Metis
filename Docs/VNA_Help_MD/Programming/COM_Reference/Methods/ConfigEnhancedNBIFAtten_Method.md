##### Write-Read

|

##### [Learn about the Pulsed
Application](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## ConfigEnhancedNBIFAtten Method

* * *

#### Description

|  Sets PNA-X receivers to auto gain setting.  
---|---  
  
####  VB Syntax

|  Pulsed.ConfigEnhancedNBIFAtten (PRF, RxWidth, IFAtten)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Pulsed |  (interface) An interface to the agilentpnapulsed.dll application interface.  
PRF |  (Double) [in] The Pulse Repetition Frequency.  
RxWidth |  (Double) [in] Receiver gate width.  
IFAtten |  (Long Integer) [out] IF attenuation value.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Example

|  [See an example using this command.](../../COM_Example_Programs/PNA-
X_Create_a_Pulsed_Measurement.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ConfigEnhancedNBIFAtten(double *pPRF, double *pWidth, long *pIF)  
  
#### Interface

|  AgilentPNAPulsed.Application  
  
* * *


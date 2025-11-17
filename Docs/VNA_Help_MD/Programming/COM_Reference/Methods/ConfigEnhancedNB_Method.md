##### Write-Read

|

##### [Learn about the Pulsed
Application](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## ConfigEnhancedNB Method - Superseded

* * *

#### Description

|  Note: This command is replaced by [ConfigEnhancedNB2
Method](ConfigEnhancedNB2_Method.htm) This subroutine determines, then
returns, the proper configuration for pulsed measurements on the PNA-X ONLY
using the spectral nulling technique. The configuration returned needs to be
sent to the VNA and any other related external equipment. The routine will
take a desired Pulse Repetition Frequency (PRF) and measurement IFBW and
return a possibly modified PRF and IFBW for proper pulsed operation on the
VNA.  
---|---  
  
####  VB Syntax

|  Pulsed.ConfigEnhancedNB (PRF, BW, PhysicalIF, NCO, Stage1TapArray,
Stage2TapArray, Stage3TapArray, FixedPRF)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Pulsed |  (interface) An interface to the agilentpnapulsed.dll application interface.  
PRF |  (Double) The Pulse Repetition Frequency. [out] The pulse repetition frequency that has been optimized for use with the VNA. NOTE: This value may be different from the value requested. [in] The desired pulse repetition frequency.  
BW |  (Long) The VNA IF Bandwidth. [out] The VNA IF bandwidth that has been optimized for use with the VNA. NOTE: This value may be different from the value requested. Zero (0) is returned if no solution is found for the specified PRF and BW. [in] The desired VNA IF bandwidth.  
PhysicalIF |  (Double) Returns physical intermediate frequency.  
NCO |  (Double) Returns numeric controlled oscillator frequency.  
Stage1TapArray |  (Long array) Returns the stage 1 filter coefficients  
Stage2TapArray |  (Long array) Returns the stage 2 filter coefficients  
Stage3TapArray |  (Long array) Returns the stage 3 filter coefficients  
FixedPRF |  (Boolean) 1 (True) Signals the .DLL routine to NOT adjust the PRF value; rather adjust ONLY the IF Bandwidth. This is the default setting. 0 (False) Adjust both the PRF and IF Bandwidth values as necessary.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Example

|  [See an example using this command.](../../COM_Example_Programs/PNA-
X_Create_a_Pulsed_Measurement.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT ConfigEnhancedNB(double *pPRF, long *pBW, double *pIF, double
*pNCO, double *pStg1, double *pStg2, double *pStg3)  
  
#### Interface

|  AgilentPNAPulsed.Application  
  
* * *


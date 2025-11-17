##### Write-Read

|

##### [Learn about the Pulsed
Application](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## ConfigEnhancedNB2 Method

* * *

#### Description

|  Note: This command replaces [ConfigEnhancedNB
Method](ConfigEnhancedNB_Method.htm). This subroutine determines, then
returns, the proper configuration for pulsed measurements on the PNA-X ONLY
using the spectral nulling technique. The configuration returned needs to be
sent to the VNA and any other related external equipment. The routine will
take a desired Pulse Repetition Frequency (PRF) and measurement IFBW and
return a possibly modified PRF and IFBW for proper pulsed operation on the
VNA. Note: If an error is returned suggesting that nulling has not been found,
add a small offset to the PRF (for example, 2.1 MHz instead of 2 MHz) or set
Fixed PRF to False.  
---|---  
  
####  VB Syntax

|  Pulsed.ConfigEnhancedNB2 (PRF, BW, PhysicalIF, NCO, ClockFreq,
Stage1TapArray, Stage2TapArray, Stage3TapArray, FixedPRF, GateDelay,
GateWidth, SWGateDelay, SWGateWidth, SWGateRamp)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Pulsed |  (interface) An interface to the agilentpnapulsed.dll application interface.  
PRF |  (Double) The Pulse Repetition Frequency. [out] The pulse repetition frequency that has been optimized for use with the VNA. NOTE: This value may be different from the value requested. [in] The desired pulse repetition frequency.  
BW |  (Long) The VNA IF Bandwidth. [out] The VNA IF bandwidth that has been optimized for use with the VNA. NOTE: This value may be different from the value requested. Zero (0) is returned if no solution is found for the specified PRF and BW. [in] The desired VNA IF bandwidth.  
PhysicalIF |  (Double) [out] Returns physical intermediate frequency.  
NCO |  (Double) [out] Returns numeric controlled oscillator frequency.  
ClockFreq |  (Double) [out] Returns the clock frequency (in Hz) of the PNA-X.  
Stage1TapArray |  (Long array) [out] Returns the stage 1 filter coefficients  
Stage2TapArray |  (Long array) [out] Returns the stage 2 filter coefficients  
Stage3TapArray |  (Long array) [out] Returns the stage 3 filter coefficients  
FixedPRF |  (Boolean) [in]

  * 1 (True) Signals the .DLL routine to NOT adjust the PRF value; rather adjust ONLY the IF Bandwidth. This is the default setting.
  * 0 (False) Adjust both the PRF and IF Bandwidth values as necessary.

  
GateDelay |  (Double) [in] Highest delay value in seconds used in any of the receiver gates.  
GateWidth |  (Double) [in] Widest pulse width value in seconds used in any of the receiver gates.  
SWGateDelay |  (Double) [out]  Returns the SW gate delay in seconds.  
SWGateWidth |  (Double) [out] Returns the SW Gate width in seconds.  
SWGateRamp |  (Long) [out]  Returns the SW Gate ramp  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Example

|  [See an example using this command.](../../COM_Example_Programs/PNA-
X_Create_a_Pulsed_Measurement.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ConfigEnhancedNB2(double *pPRF, long *pBW, double *pIF, double
*pNCO, double *clock, double *pStg1, double *pStg2, double *pStg3,
VARIANT_BOOL fixPRF, double gateDelay, double gateWidth, double *SWgateDelay,
double *SWgateWidth, long *SWgateRamp)  
  
#### Interface

|  AgilentPNAPulsed.Application  
  
* * *


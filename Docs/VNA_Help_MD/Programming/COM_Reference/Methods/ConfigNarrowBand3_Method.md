##### Write-Read

|

##### [Learn about the Pulsed
Application](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## ConfigNarrowBand3 Method

* * *

#### Description

| Note: This method replaces ConfigNarrowBand2 Method. The BW argument now
returns 0 if no solution is found for the specified PRF and BW. In addition,
adjustments were made to the filter finder algorithm This subroutine
determines, then returns, the proper configuration for pulsed measurements on
the VNA using the spectral nulling technique. The configuration returned needs
to be sent to the VNA and any other related external equipment such as pulse
generators. The routine will take a desired Pulse Repetition Frequency (PRF)
and measurement IFBW and return a possibly modified PRF and IFBW for proper
pulsed operation on the VNA. The routine will also return the Sample Rate,
Number of Taps, and Offset that must be sent to the VNA to configure it in
pulsed mode using the spectral nulling technique. Although the example below
uses COM programming to communicate with the VNA, these commands can be
replaced with SCPI equivalents. Note: The pulsed application may set the
offset frequency (option S93080A/B) of the VNA to some value other than zero
(the default value). If the stop frequency is set to the maximum of the VNA
model, then an error message may appear on the VNA stating that the response
frequency has exceeded the maximum allowed frequency. To fix this, set the
stop frequency to a value that is at least 2 KHz less than the maximum
allowed.  
For example, if you have a 20 GHz VNA, and the stop frequency is set to 20
GHz, and the error message appears, then set the stop frequency to 19.999998
GHz  
---|---  
  
####  VB Syntax

| Pulsed.ConfigNarrowBand (PRF, NumTaps, BW, OffSet, SampleRate, Precision,
FixedPRF, PG81110)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Pulsed | (interface) An interface to the agilentpnapulsed.dll application interface.  
PRF | (Double) The Pulse Repetition Frequency. [out] The pulse repetition frequency that has been optimized for use with the VNA. NOTE: This value may be different from the value requested. [in] The desired pulse repetition frequency.  
NumTaps | (Long) The number of taps to send to the VNA for pulsed operation.  
BW | (Long) The VNA IF Bandwidth. [out] The VNA IF bandwidth that has been optimized for use with the VNA. NOTE: This value may be different from the value requested. Zero (0) is returned if no solution is found for the specified PRF and BW. [in] The desired VNA IF bandwidth.  
Offset | (Double) The offset value to send to the VNA for pulsed operation. The offset value is used to adjust the VNA for the two different possible sample rates that may be returned.  
SampleRate | (Double) [out] The sample rate to send to the VNA for pulsed operation. [in] Passing a value of 6.2 us will make sure that the offset frequency is not shifted and therefore could be used with converter measurements. Otherwise enter 0.  
Precision | (Double)  The precision variables sets the precision that will be used to decrement the PRF when running the configuration routines. This variable can be set to the precision required by the external pulse generators so that the configuration routine will not return a PRF that is not within the precision limits of the pulse generators.  
FixedPRF | (Boolean) 1 (True) Signals the .DLL routine to NOT adjust the PRF value; rather adjust ONLY the IF Bandwidth. This is the default setting. 0 (False) Adjust both the PRF and IF Bandwidth values as necessary.  
PG81110 | (Boolean) 1 (True) You are using an Keysight 81110 as the pulse generator. This allows increased accuracy in adjustments for offset and PRF. 0 (False) Not using an Keysight 81110.  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Example

| Removed example from help file.  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT ConfigNarrowBand(double *pPRF, long *pNumTaps, long *pBW, double
*pOffset, double *pSampleRate, int Precision)  
  
#### Interface

| AgilentPNAPulsed.Application  
  
* * *


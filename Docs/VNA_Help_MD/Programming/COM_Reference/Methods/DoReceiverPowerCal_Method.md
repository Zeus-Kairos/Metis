##### Write-only

|

##### [About Receiver
Cal](../../../S3_Cals/PwrCalibration.htm#ReceiverPowerCal)  
  
---|---  
  
## DoReceiverPowerCal Method

* * *

#### Description

|  Note: This command replaces [DataToDivisor](DataToDivisor_Method.md),
[LogMagnitudeOffset](../Properties/LogMagnitudeOffset_Property.md),
[Normalization](../Properties/Normalization_Property.md),
[InterpolateNormalization](../Properties/InterpolateNormalization_Property.md).
Immediately performs a receiver power calibration. The connection to the
receiver must be in place when this command is sent. A Receiver Power Cal
requires that the active measurement be an
[Unratioed](../../../S1_Settings/Measurement_Parameters.md#Unratioed_Power)
power measurement.  
---|---  
  
####  VB Syntax

|  cal.DoReceiverPowerCal(param, srcPort [,pwrOffset])  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A [Calibrator](../Objects/Calibrator_Object.md) (object)  
param |  (string)  Receiver to be calibrated. Choose any receiver in your VNA. [See a block diagram of your VNA.](../../../Specs/ManualChoice.md#Block_diag_opt) Receivers can also be referred to using logical receiver notation. This notation makes it easy to refer to receivers with an [external test set](../../../System/External_Testset_Control.md) connected to the VNA. You do not need to know which physical receiver is used for each test port. [Learn more.](../../../S1_Settings/Measurement_Parameters.md#RecNotation)  
srcPort |  (long integer)  Number of the port which will supply source power to the receiver during this cal. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
pwrOffset |  (double)  Optional argument. Offset value in dB. Adjusts a receiver power cal to account for components or adapters that are added between the source port and receiver while performing this cal. Specify loss as a negative number; and gain as a positive number.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  cal.DoReceiverPowerCal "B", 1, -10  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT DoReceiverPowerCal(BSTR parameter, long lSrcPort, double
dPowerOffset);  
  
#### Interface

|  ICalibrator5  
  
* * *


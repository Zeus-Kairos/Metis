##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## SourcePowerCalPowerOffset Property

* * *

#### Description

|  Sets or returns a power level offset from the VNA test port power. This can
be a gain or loss value (in dB) to account for components you connect between
the source and the reference plane of your measurement. For example, specify
10 dB to account for a 10 dB amplifier at the input of your DUT. Cal power is
the sum of the test port power setting and this offset value. Following the
calibration, the VNA power readouts are adjusted to the cal power. This
property performs the same function as the power offset argument on
[SetCalInfoEx Method](../Methods/SetCalInfoEx_Method.md), except that this
property can read the offset value.  
---|---  
  
#### VB Syntax

|  chan.SourcePowerCalPowerOffset (sourcePort) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  (object) - A [Channel](../Objects/Channel_Object.md) object  
sourcePort |  (long integer) \- The source port for which to set this power offset value.  
value |  (double) \- Gain or loss value in dB. Choose a value between -200 and 200.  
  
#### Return Type

|  Double  
  
#### Default

|  0 dB  
  
#### Examples

|  chan.SourcePowerCalPowerOffset(1) = 10 'Write  
offset = chan.SourcePowerCalPowerOffset(2) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SourcePowerCalPowerOffset(long sourcePort, double *pVal);
HRESULT put_SourcePowerCalPowerOffset(long sourcePort, double newVal);  
  
#### Interface

|  IChannel4  
  
* * *


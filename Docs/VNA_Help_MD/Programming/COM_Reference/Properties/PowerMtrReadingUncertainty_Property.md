##### Read-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
# PowerMtrReadingUncertainty Property

* * *

#### Description

| Returns the power uncertainty associated with the specific power meter at
the specified frequency and power.  
---|---  
  
####  VB Syntax

| pwrUnc = pwrSensor.PowerMtrReadingUncertainty(freq,power)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrUnc | (Double) Variable to store the returned power meter reading uncertainty.   
pwrSensor | A [PowerSensorUncertainty](../Objects/PowerSensorUncertainty_Object.md) (Object)   
freq | (Double) Frequency (Hz).  
power | (Double) Power (dBm).  
  
#### Return Type

| Double (Watts)  
  
#### Default

| Not Applicable  
  
#### Examples

| pwrUnc = pwrSensor.PowerMtrReadingUncertainty(10e9,0.0)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT PowerMtrReadingUncertainty(double freq, double power, double
*pwrUnc);  
  
#### Interface

| IPowerSensorUncertainty


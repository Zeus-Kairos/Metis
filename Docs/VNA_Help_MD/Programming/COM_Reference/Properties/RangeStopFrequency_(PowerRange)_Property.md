##### Write/Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
# RangeStopFrequency (PowerRange) Property

* * *

#### Description

|  Sets and reads the upper bound of the frequency range used for range based
power min and max.  
---|---  
  
####  VB Syntax

|  powerRange.RangeStopFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerRange |  A [PowerRange](../Objects/Power_Range_Object.md) (object)  
  
#### value

|  (Double) Stop frequency. Choose a number within the frequency limits of the
analyzer. Units are Hz.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
|  powerRange.RangeStopFrequency = 10e9 'Write  
value = powerRange.RangeStopFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RangeStopFrequency(double* stopfreq); HRESULT
put_RangeStopFrequency(double stopfreq);  
  
#### Interface

|  IPowreRange  
  
* * *


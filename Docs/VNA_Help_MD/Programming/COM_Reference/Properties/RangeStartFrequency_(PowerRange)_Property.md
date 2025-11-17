##### Write/Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
# RangeStartFrequency (PowerRange) Property

* * *

#### Description

|  Sets and reads the lower bound of the frequency range used for range based
power min and max.  
---|---  
  
####  VB Syntax

|  powerRange.RangeStartFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerRange |  A [PowerRange](../Objects/Power_Range_Object.md) (object)  
  
#### value

|  (Double) Start frequency. Choose a number within the frequency limits of
the analyzer. Units are Hz.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
|  powerRange.RangeStartFrequency = 1e9 'Write  
value = powerRange.RangeStartFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RangeStartFrequency(double* startfreq); HRESULT
put_RangeStartFrequency(double startfreq);  
  
#### Interface

|  IPowreRange  
  
* * *


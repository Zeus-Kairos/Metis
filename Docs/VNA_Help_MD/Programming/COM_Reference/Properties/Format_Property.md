##### Write/Read

|

##### [About Data Format](../../../S1_Settings/Data_Format.md)  
  
---|---  
  
## Format Property

* * *

#### Description

|  Sets or returns the display format of the measurement.  
---|---  
  
####  VB Syntax

|  meas.Format = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
value |  (enum NADataFormat) \- Choose from: 0 - naDataFormat_LinMag 1 - naDataFormat_LogMag 2 - naDataFormat_Phase 3 - naDataFormat_Polar 4 - naDataFormat_Smith 5 - naDataFormat_Delay 6 - naDataFormat_Real 7 - naDataFormat_Imaginary 8 - naDataFormat_SWR 9 - naDataFormat_PhaseUnwrapped 10 - naDataFormat_InverseSmith 11 - naDataFormat_Kelvin 12 - naDataFormat_Fahrenheit 13 - naDataFormat_Celsius 14 - naDataFormat_PhasePositive  
  
#### Return Type

|  Long Integer  
  
#### Default

|  1 \- naDataFormat_LogMag  
  
#### Examples

|  meas.Format = naDataFormat_Real 'Write  
fmt = meas.Format 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Format(tagDataFormat *pVal) HRESULT put_Format(tagDataFormat
newVal)  
  
#### Interface

|  IMeasurement  
  
* * *


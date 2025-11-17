##### Write/Read

|

##### [About SweptIMDCal](../../../Applications/Swept_IMD.md#CalOverview)  
  
---|---  
  
## CalibrationFrequencies Property

* * *

#### Description

|  Sets and returns the whether to perform the source power cal at the center
frequencies midway between the main tones, or at all main tone frequencies.  
---|---  
  
####  VB Syntax

|  imd.CalibrationFrequencies = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMDCal](../Objects/SweptIMDCal_Object.md) (object)  
value |  (Enum as NAIMDCalibrationFrequencies) Choose from: 0 - naIMDCenterFrequencies -Perform source power calibration at only the center frequencies midway between the main tones. 1 - naIMDALLFrequencies \- Perform source power calibration at all main tone frequencies.  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naIMDCenterFrequencies  
  
#### Examples

|  imd.CalibrationFrequencies = naIMDALLFrequencies 'Write  
calFreq = imd.CalibrationFrequencies 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CalibrationFrequencies(tagNAIMDCalibrationFrequencies * Val)
HRESULT put_CalibrationFrequencies(tagNAIMDCalibrationFrequencies newVal)  
  
#### Interface

|  ISweptIMD  
  
* * *


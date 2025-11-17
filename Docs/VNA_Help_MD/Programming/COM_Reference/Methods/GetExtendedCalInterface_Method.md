##### Write-only

|  
---|---  
  
## GetExtendedCalInterface Method

* * *

#### Description

|  Returns an interface that exposes the properties of Noise Calibration.  
---|---  
  
####  VB Syntax

|  Cal2.GetExtendedCalInterface (interface)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
Cal2 |  An ICalibrate2 (object)  
interface |  (object) Returns a handle to the specified interface. Choose from ' "NoiseCal"  
  
#### Return Type

|  
  
#### Default

|  
  
#### Example

|  dim noiseCal  
dim noiseCalExtensions  
set noiseCal= Get Calmanager?.CreateCustomCalEx("NoiseCal")  
set noiseCalExtensions = noiseCal.GetExtendedCalInterface("INoiseCal")  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetExtendedCalInterface();  
  
#### Interface

|  ICalibrate2  
  
* * *


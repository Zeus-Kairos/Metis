##### Read only

## GetCalTypes Method

* * *

#### Description

|  Returns a list of available calibration types known to the VNA. The
Standard CalTypes are the same on all VNA's, but the Custom CalTypes are not
necessarily the same. They are dependent on the custom measurement in the VNA.
[Learn more about applying Cal
Types.](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.htm#Applying)
See also [CalibrationTypeID](../Properties/CalibrationTypeID_property.md) to
apply a Cal Type containing in a Cal Set.  
---|---  
  
####  VB Syntax

|  v = mgr.GetCalTypes  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mgr |  A [CalManager](../Objects/CalManager_Object.md) (Object)  
v |  Name/GuidPair that contains the calibration type name and associated GUID for each cal type known to the VNA.  
  
#### Return Type

|  (variant) Two dimensional array.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  v =CalManager.GetCalTypes  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetCalTypes( VARIANT * NameGuidPair )  
  
#### Interface

|  ICalManager2


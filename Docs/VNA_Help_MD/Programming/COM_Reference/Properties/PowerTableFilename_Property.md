##### Write/Read

|

##### [About Guided Power Cal](../../../S3_Cals/Guided_Power_Calibration.md)  
  
---|---  
  
## PowerTableFilename Property

* * *

#### Description

|  Loads a file that defines a power table to be used during a SMC Guided
Power Cal or Cal All Channels on a mmWave system. This feature is available
because power sensors are NOT typically available at mmWave frequencies.
[Learn
more.](../../../IFAccess/External_Test_Head_Configuration.htm#SMCPowerProcess)  
---|---  
  
####  VB Syntax

|  guided.PowerTableFilename (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guided |  A [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object )  
n |  (Long) Source port being calibrated.  
value |  (String) Full path and filename of a *.prn file that defines the power table. An error is returned if the file is not found.  
  
#### Return Type

|  String  
  
#### Default

|  Not applicable.  
  
#### Examples

|  guided.PowerTableFilename(1) = "c:\powertable1.prn" 'Write  
value = guided.PowerTableFilename(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerTableFilename (long port, BSTR* val); HRESULT
put_PowerTableFilename (long port, BSTR newVal);  
  
#### Interface

|  IGuidedCalibration9  
  
* * *


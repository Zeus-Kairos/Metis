##### Write-only

|

#####  
  
---|---  
  
## GenerateGlobalDeltaMatchSequence Method

* * *

#### Description

|  Initiates a global delta match calibration. [Learn more about Delta match
calibration.](../../../S3_Cals/TRL_Calibration.htm#4Port) See example of a
complete Delta Match calibration.  
---|---  
  
####  VB Syntax

|  numSteps = guided.GenerateGlobalDeltaMatchSequence conn,cKit  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
numSteps |  Long Integer \- Variable to store the returned number of connection steps required by the Global Delta Match Cal.  
guided |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
conn |  String Connector Type for port 1.  
cKit |  String Cal Kit for all ports.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  guided.GenerateGlobalDeltaMatchSequence APC 3.5 female,"85052B"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GenerateGlobalDeltaMatchSequence(BSTR port_1_conn, BSTR cal_kit,
long *num_steps);  
  
#### Interface

|  IGuidedCalibration2


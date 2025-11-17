##### Read-only

|

##### [About User
Characterization](../../../S3_Cals/ECal_User_Characterization.htm)  
  
---|---  
  
## GetEcalUserCharacterizer Method

* * *

#### Description

|  This method returns a handle to an
[ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) object.  
---|---  
  
####  VB Syntax

|  calMgr.GetEcalUserCharacterizer( )  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr |  A [CalManager Object](../Objects/CalManager_Object.md) (object)  
  
#### Return Type

|  IEcalUserCharacterizer  
  
#### Default

|  Not Applicable  
  
#### Example

|  Dim mgr as ICalManager  
Set mgr = app.GetCalManager  
Dim ecalCharacterizer  
Set ecalCharacterizer = mgr.GetECalUserCharacterizer()  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetEcalUserCharacterizer( IECalUserCharacterizer **obj);  
  
#### Interface

|  ICalManager6  
  
* * *


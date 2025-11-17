##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## FirmwareMajorRevision Property

* * *

#### Description

|  Returns the major firmware revision number as an integer. For example,
given a firmware revision number A.03.30, this command returns 3.  
---|---  
  
####  VB Syntax

|  value = cap.FirmwareMajorRevision  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) - Variable to store the returned integer value of the firmware revision number.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.FirmwareMajorRevision 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FirmwareMajorRevision(long * majorRev );  
  
#### Interface

|  ICapabilities


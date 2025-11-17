##### Write/Read

|

##### [About External
Sources](../../../System/Configure_an_External_Source.htm)  
  
---|---  
  
# EnableModulationControl Property

* * *

#### Description

|  Sets and reads the state of the modulation control. Modulation control must
be ON to control the modulation of an external source.  
---|---  
  
#### VB Syntax

|  extSource.EnableModulationControl = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extSource |  An [ExternalSource Object](../Objects/ExternalSource_Object.md) (object)  
value |  (Boolean) Choose from: 1 \- Enable control of external modulation. 0 \- Disable control of external modulation. [Learn about these settings](../../../System/Configure_an_External_Source.md) and about [adding an external source](../../../System/Configure_an_External_Device.md).  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  extSource.EnableModulationControl = 1 'Write  
value = extSource.EnableModulationControl 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_EnableModulationControl(VARIANT_BOOL bEnable); HRESULT
get_EnableModulationControl(VARIANT_BOOL* bEnable);  
  
#### Interface

|  IExternalSource2  
  
* * *


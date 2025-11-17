##### Read/Write

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## IsOn Property

* * *

#### Description

|  Sets and returns the ON |OFF state of Embedded LO.  
---|---  
  
####  VB Syntax

|  obj.IsOn = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  An [EmbeddedLO](../Objects/EmbeddedLO_Object.md) (object) or A [ConverterEmbeddedLO](../Objects/ConverterEmbeddedLO_Object.md) (object)  
value |  (Boolean) False \- Turns Embedded LO OFF True \- Turns Embedded LO ON  
  
#### Return Type

|  (Boolean)  
  
#### Default

|  False (OFF)  
  
#### Examples

|  embedLO.IsOn = True 'write  
data= embedLO.IsOn 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IsOn( VARIANT_BOOL* IsOn); HRESULT put_IsOn( VARIANT_BOOL
IsOn);  
  
#### Interface

|  IEmbededLO  
  
* * *


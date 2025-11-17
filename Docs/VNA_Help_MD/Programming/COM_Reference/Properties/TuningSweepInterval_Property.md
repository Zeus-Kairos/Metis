##### Read/Write

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## TuningSweepInterval Property

* * *

#### Description

|  Set how often a tuning sweep is performed.  
---|---  
  
####  VB Syntax

|  obj.TuningSweepInterval = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  An [EmbeddedLO](../Objects/EmbeddedLO_Object.md) (object) or A [ConverterEmbeddedLO](../Objects/ConverterEmbeddedLO_Object.md) (object)  
value |  (Long) Tuning sweep interval.  
  
#### Return Type

|  (Long)  
  
#### Default

|  1  
  
#### Examples

|  embedLO.TuningSweepInterval = 3 'write .. tuning is performed every third
measurement sweep  
value = embedLO.TuningSweepInterval 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TuningSweepInterval(long* interval); HRESULT
put_TuningSweepInterval(long interval);  
  
#### Interface

|  IEmbededLO  
  
* * *


##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NoiseSourceState Property

* * *

#### Description

|  Sets and reads the noise source [(28V)](../../../Rear_Panel/XRtour.md#28)
ON and OFF.  
---|---  
  
####  VB Syntax

|  app.NoiseSourceState = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
state |  (boolean) False (0) \- Turns Noise Source OFF True (1) \- Turns Noise Source ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  For VNA models with a Noise Figure option (028/029/H29), the 28V line is ON
at application start and after a preset. The ON/OFF state is also available
from a VNA softkey menu. For VNA models WITHOUT a Noise Figure option
(028/029/H29), the 28V line is OFF at application start and its state is not
affected by a preset. The ON/OFF state is NOT available from a VNA softkey
menu.  
  
#### Examples

|  app.NoiseSourceState = True 'Write  
coupl = app.NoiseSourceState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_NoiseSourceState(VARIANT_BOOL bState)  
HRESULT get_NoiseSourceState(VARIANT_BOOL *bState)  
  
#### Interface

|  IApplication13  
  
* * *

  


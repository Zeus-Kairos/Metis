##### Write/Read

|

##### [About Auxiliary
Triggering](../../../S1_Settings/External_Triggering.htm#AuxTrigDiag)  
  
---|---  
  
## HandshakeEnable Property

* * *

#### Description

|  Turns handshake ON / OFF. To enable handshake, the main trigger enable must
ALSO be set using [Enable](Enable_Property.md). When ON, VNA acquisition
waits indefinitely for the input line to be asserted before continuing with
the acquisition. Note: Use on PNA-X ONLY. Other models do NOT have an Aux
Input.  
---|---  
  
####  VB Syntax

|  auxTrig.HandshakeEnable = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
auxTrig |  An [AuxTrigger](../Objects/AuxTrigger_Object.md) (object)  
state |  (boolean) - True \- Handshake enabled False \- Handshake NOT enabled  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Exaamples

|  auxTrig.HandshakeEnable = True 'Write  
value = auxTrig.HandshakeEnable 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_HandshakeEnable(VARIANT_BOOL * enable);  
HRESULT put_HandshakeEnable(VARIANT_BOOL enable);  
  
#### Interface

|  IAuxTrigger  
  
* * *


##### Write/Read

|

##### About 2-Port Fixturing  
  
---|---  
  
## Reverse2PortAdapter Property

* * *

#### Description

|  Set and read whether or not to reverse ports on a 2-port fixture or adapter
to be de-embedded.  
---|---  
  
####  VB Syntax

|  fixture.Reverse2PortAdapter (port) = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  VNA port number for which SNP file is to be de-embedded.  
bool |  True \- Reverse ports. False \- Do NOT reverse ports.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.Reverse2PortAdapter = True  
value = fixture.Reverse2PortAdapter 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Reverse2PortAdapter(short portNum, VARIANT_BOOL *pRev); HRESULT
put_Reverse2PortAdapter(short portNum,VARIANT_BOOL bRev);  
  
#### Interface

|  IFixturing6  
  
* * *


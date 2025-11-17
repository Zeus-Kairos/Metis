##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## DiffPortMatchMode Property

* * *

#### Description

|  Sets the differential matching circuit type. To select a user-defined
circuit, specify IN ADVANCE the 2-port touchstone filename with
[DiffPortMatch_UserFilename Property](DiffPortMatchUserFilename_Property.md).
If you do not specify the appropriate file and you select USER, an error
occurs and naNO_CIRCUIT is automatically selected.  
---|---  
  
####  VB Syntax

|  fixture.DiffPortMatchMode(pNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
pNum |  (Integer) Balanced (logical) port number. Choose from logical ports 1, 2, or 3. [Learn more about logical ports.](../../../S1_Settings/Balanced_Measurements.md#mapping)  
value |  (Enum as NADiffPortMatchCircuitMode) Choose from: 0 or naSHUNT_L_SHUNT_C_CIRCUIT \- Specifies the circuit that consists of shunt L and shunt C. 1 or naUSER_FILE_CIRCUIT \- Specifies the user-defined circuit. 2 or naNO_CIRCUIT \- Specifies no-circuit.  
  
#### Return Type

|  Enum  
  
#### Default

|  naSHUNT_L_SHUNT_C_CIRCUIT  
  
#### Examples

|  fixture.DiffPortMatchMode(2) = naNO_CIRCUIT 'Write  
value = fixture.DiffPortMatchMode(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DiffPortMatchMode( short port, tagNADiffPortMatchCircuitMode
*eVal) HRESULT put_DiffPortMatchMode( short port,
tagNADiffPortMatchCircuitMode eVal)  
  
#### Interface

|  IFixturing2


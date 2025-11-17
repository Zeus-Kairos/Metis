##### Write-only

|  
---|---  
  
## put_PortCData Method

* * *

#### Description

|  Writes a 4-bit value to Port C on the Aux I/O connector (pins 22-25) and
the Material Handler IO (pins 21-24 Anritsu) - (pins 22-25 Avantest). Note:
These lines are connected to both the Handler IO and Aux IO in the VNA.
Therefore, this command will affect both of these connectors in the same way.  
---|---  
  
####  VB Syntax

|  AuxIO.put_PortCData num  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
AuxIO |  (object) - A Hardware Auxiliary Input / Output object  
num |  (variant) \- 4 bit binary value. Choose from 0-15  
  
#### Return Type

|  None  
  
#### Default

|  None  
  
#### Examples

|  HWAuxIO.put_PortCData 15 'If Positive Logic, Port C lines C0, C1, C2, C3 go
High. If Negative Logic, they go Low.  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_PortCData( VARIANT Data );  
  
#### Interface

|  IHWAuxIO


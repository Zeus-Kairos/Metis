##### Read-only

|  
---|---  
  
## get_PortCData Method

* * *

#### Description

|  Reads a 4-bit value from Port C of the Aux I/O connector (pins 22-25) and
the Material Handler IO (pins 21-24 Anritsu) - (pins 22-25 Avantest). Note:
These lines are connected to both the Handler IO and Aux IO in the VNA.  
---|---  
  
####  VB Syntax

|  value = AuxIO.get_PortCData  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (variant) \- Variable to store the returned data  
AuxIO |  (object) - A Hardware Auxiliary Input / Output object  
  
#### Return Type

|  Integer  
  
#### Default

|  None  
  
#### Examples

|  value = auxIo.get_PortCData 'Reading a value of 15 when in Positive Logic
indicates Port C lines C0, C1, C2, C3 are High. If in Negative Logic they are
Low.  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortCData( VARIANT* Data );  
  
#### Interface

|  IHWAuxIO


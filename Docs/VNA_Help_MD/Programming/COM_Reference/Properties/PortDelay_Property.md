##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## PortDelay Property

* * *

#### Description

|  Sets and returns the Port Extensions Delay value for the specified port
number. Note: This command affects ALL measurements on the channel. This
command replaces [Port 1](Port_1_Property.md) [Port 2](Port_2_Property.md)
[Port_3](Port_3_Property.md) Properties.  
---|---  
  
####  VB Syntax

|  fixture.PortDelay(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive delay value.  
value |  (Double) Delay value in seconds. Choose a value between -1E18 and 1E18.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  fixture.PortDelay(2) = .002 'Write  
value = fixture.PortDelay(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortDelay(short port double *pVal)  
HRESULT put_PortDelay(short port double newVal)  
  
#### Interface

|  IFixturing


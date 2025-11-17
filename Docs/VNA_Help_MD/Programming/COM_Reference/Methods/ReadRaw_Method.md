##### Read-only

|

##### [About the ExtTestSetIO connector](../../TestSetIO_Connector.md)  
  
---|---  
  
## ReadRaw Method

* * *

#### Description

|  Reads a 16-bit value from the external test set. The 16-bit value is
comprised of lines AD0 - AD12, Sweep Holdoff In and Interrupt In (inverted).
When this command is used the analyzer does NOT generate the appropriate
timing signals; it simply reads the lines. The user needs to first use the
[WriteRaw](WriteRaw_Method.md) method to do the initial setup. The RLW line
(pin25) must be set to the appropriate level in order to read the test set
connected. Below is the format of data that is read with ReadRaw:  
---|---  
  
|  Pin |  Bit |  Signal name  
---|---|---|---  
|  22 |  0 |  AD0*  
|  23 |  1 |  AD1*  
|  11 |  2 |  AD2*  
|  10 |  3 |  AD3*  
|  9 |  4 |  AD4*  
|  21 |  5 |  AD5*  
|  20 |  6 |  AD6*  
|  19 |  7 |  AD7*  
|  6 |  8 |  AD8*  
|  5 |  9 |  AD9*  
|  4 |  10 |  AD10*  
|  17 |  11 |  AD11*  
|  3 |  12 |  AD12*  
|  2 |  13 |  Sweep Holdoff In  
|  13 |  14 |  Interrupt In (inverted internally)  
|  na |  15 |  Always Zero, grounded internally  
  

####

|  *These lines are dependent on the state of RLW (pin25).  
Writing a 0(low) to RLW will set lines AD0-AD12 to write mode.  
Writing a 1(high) to RLW will set lines AD0-AD12 to read mode.  
---|---  
  
####  VB Syntax

|  value = ExtIO.ReadRaw (address)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (variant) \- Variable to store the returned data  
ExtIO |  (object) - An External IO object  
address |  (variant) \- Address to read data from  
  
#### Return Type

|  Real  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = ExtIO.ReadRaw (address)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT ReadRaw( VARIANT* Input );  
  
#### Interface

|  IHWExternalTestSetIO


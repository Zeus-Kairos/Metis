##### Write/Read

|

##### [About Safe
Sweep](../../../Applications/Gain_Compression_Application.htm#Safe)  
  
---|---  
  
# SafeSweepMaximumDCLimit Property

* * *

#### Description

| Set and read the maximum limit of the external DC device.  
---|---  
  
####  VB Syntax

| gca.SafeSweepMaximumDCLimit = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca | A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value | (Double)  Maximum DC level.   
  
#### Return Type

| Double  
  
#### Default

| -5  
  
#### Examples

| gca.SafeSweepMaximumDCLimit = -5 'Write  
maxLimit = gca.SafeSweepMaximumDCLimit 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SafeSweepMaximumDCLimit(double* value) HRESULT
put_SafeSweepMaximumDCLimit(double value)  
  
#### Interface

| IGainCompression6  
  
* * *


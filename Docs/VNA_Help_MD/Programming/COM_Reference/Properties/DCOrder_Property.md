##### Write/Read

|

#####  
  
---|---  
  
# DCOrder Property

* * *

#### Description

| Set and read the order for the specified DC source in the multi-dimensional
sweep.  
---|---  
  
####  VB Syntax

| md.DCOrder (_name,port_) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
_md_ | A [MultiDimensionalSweep](../Objects/MultiDimensionalSweep_Object.md) (object) which belongs to a SA channel.  
_name,port_ | (string) Name of the "DC source, port"  
_value_ | (long) Dimension order. Choose an integer value of 1 or higher.  
  
#### Return Type

| long  
  
#### Default

| 1  
  
#### Examples

| md.DCOrder ("AO1") = 2  'Write  
value = md.DCOrder("MyDCSource,Port 1") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_DCOrder (BSTR name, long value); HRESULT get_DCOrder (BSTR name,
long* value);  
  
#### Interface

| IMultiDimensionalSweep  
  
* * *


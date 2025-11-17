##### Write/Read

|

#####  
  
---|---  
  
# SourcePortFixedFrequency Property

* * *

#### Description

| Set and read the fixed frequency value for a specific port.  
---|---  
  
####  VB Syntax

| chan.SourcePortFixedFrequency(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan | A SA [Channel](../Objects/Channel_Object.md) (object)  
port | (long) **Source port number for which to set the fixed frequency value.**  
_value_ | (double) Fixed frequency value.  
  
#### Return Type

| double  
  
#### Default

| 1  
  
#### Examples

| chan.SourcePortFixedFrequency(1) = 1e9  'Write  
value = chan.SourcePortFixedFrequency(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_SourcePortFixedFrequency(long port, double value); HRESULT
get_SourcePortFixedFrequency(long port, double* value);  
  
#### Interface

| IChannel27  
  
* * *


##### Write/Read

|

#####  
  
---|---  
  
# SourcePortStartFrequency Property

* * *

#### Description

| Set and read the start frequency value for a specific port.  
---|---  
  
####  VB Syntax

| chan.SourcePortStartFrequency(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan | A SA [Channel](../Objects/Channel_Object.md) (object)  
port | (long) **Source port number for which to set the start frequency value.**  
_value_ | (double) Start frequency value.  
  
#### Return Type

| double  
  
#### Default

| 1  
  
#### Examples

| chan.SourcePortStartFrequency(1) = 1e9  'Write  
value = chan.SourcePortStartFrequency(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_SourcePortStartFrequency(long port, double value); HRESULT
get_SourcePortStartFrequency(long port, double* value);  
  
#### Interface

| IChannel27  
  
* * *


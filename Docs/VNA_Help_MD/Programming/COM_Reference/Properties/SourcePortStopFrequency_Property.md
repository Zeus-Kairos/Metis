##### Write/Read

|

#####  
  
---|---  
  
# SourcePortStopFrequency Property

* * *

#### Description

| Set and read the stop frequency value for a specific port.  
---|---  
  
####  VB Syntax

| chan.SourcePortStopFrequency(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan | A SA [Channel](../Objects/Channel_Object.md) (object)  
port | (long) **Source port number for which to set the stop frequency value.**  
_value_ | (double) Stop frequency value.  
  
#### Return Type

| double  
  
#### Default

| 1  
  
#### Examples

| chan.SourcePortStopFrequency(1) = 1e9  'Write  
value = chan.SourcePortStopFrequency(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_SourcePortStopFrequency(long port, double value); HRESULT
get_SourcePortStopFrequency(long port, double* value);  
  
#### Interface

| IChannel27  
  
* * *


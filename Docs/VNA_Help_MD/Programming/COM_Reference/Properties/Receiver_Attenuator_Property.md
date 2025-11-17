##### Write/Read

|

##### [About Receiver
Attenuation](../../../S1_Settings/Power_Level.htm#Receiver_Atten)  
  
---|---  
  
## ReceiverAttenuator Property

* * *

#### Description

| Sets or returns the value of the specified receiver attenuator control.  
---|---  
  
####  VB Syntax

| object.ReceiverAttenuator(rec) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object | Channel (object) or CalSet (object) - Read-only property  
rec | (long integer) \- Receiver with attenuator control to be changed. Choose from any of the available receivers in your VNA 1 \- Receiver A 2 \- Receiver B 3 \- Receiver C 4 \- Receiver D Receiver attenuation can not be set using [logical receiver notation](../../../S1_Settings/Measurement_Parameters.md#RecNotation).  
value | (double) - Attenuator value in dB. Choose any Long Integer between 0 and 35 in 5dB steps: If an invalid value is entered, the analyzer will select the next lower valid value. For example, if 19.9 is entered the analyzer will select 15 dB attenuation.  
  
#### Return Type

| Double  
  
#### Default

| 0 db  
  
#### Examples

| chan.ReceiverAttenuator(1) = 5 'Write  
attn = chan.ReceiverAttenuator(2) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT get_ReceiverAttenuator(long lport, double* pVal)  
HRESULT put_ReceiverAttenuator(long lport, double newVal)  
  
#### Interface

| IChannel |CalSet3


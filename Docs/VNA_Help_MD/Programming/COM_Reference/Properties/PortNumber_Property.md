##### Write / Read

|

##### [About Receiver Leveling](../../../S1_Settings/Receiver_Leveling.md)  
  
---|---  
  
# PortNumber Property

* * *

#### Description

|  Sets and reads the port number for power range data. When two sources are available in combiner mode, refer to the following table. |  Port Number property of power range object |  Power returned for a two port instrument |  Power returned for a four port instrument  
---|---|---  
1 |  Port 1 |  Port 1  
2 |  Port 2 |  Port 2  
3 |  Src2-Out11 |  Port 3  
4 |  Src2-Out21 |  Port 4  
5 |  Port1-Src21 |  Port1-Src21  
  
1 Indicates that the port requires option 224 or 423.  
  
####  VB Syntax

|  powerRange.PortNumber = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerRange |  A [PowerRange](../Objects/Power_Range_Object.md) (object)  
  
#### value

|  (Integer) Port number for power range data.  
  
#### Return Type

|  Integer  
  
#### Default

|  Not Applicable  
|  powerRange.PortNumber = 3 'Write  
value = powerRange.PortNumber 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortNumber(short* port); HRESULT put_PortNumber(short port);  
  
#### Interface

|  IPowreRange  
  
* * *


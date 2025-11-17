##### Read-only

|

#####  
  
---|---  
  
## CustomChannelConfiguration Property

* * *

#### Description

|  Returns a handle to the custom application object on the active channel.
You can either (1) use the handle directly to access measurement properties
and methods, or (2) set a variable to the measurement object. The variable
retains a handle to the original measurement. Currently, the custom
application objects to which this property provides access ares:

  * [NoiseFigure Object](../Objects/NoiseFigure_Object.md)
  * [GainCompression Object](../Objects/GainCompression_Object.md)
  * [SweptIMD Object](../Objects/SweptIMD_Object.md)

  
---|---  
  
####  VB Syntax

|  1) set custChan = chan.CustomChannelConfiguration. <setting>  
or  
2) set custChan = app.ActiveChannel.CustomChannelConfiguration  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
custChan |  A variable in which the handle to a custom application is returned. (object)  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
<setting> |  A property or method setting on the custom application object.  
  
#### Return Type

|  Custom application object  
  
#### Default

|  None  
  
#### Examples

|  See
examples:[NoiseFigure](../../COM_Example_Programs/Create_and_Cal_a_NoiseFigure_Measurement.md)
[GainCompression](../../COM_Example_Programs/Create_and_Cal_a_Gain_Compression_Measurement.md)
[SweptIMD](../../COM_Example_Programs/Create_and_Cal_a_Swept_IMD_Measurement.md)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT CustomChannelConfiguration(IDispatch** value);  
  
#### Interface

|  IChannel12  
  
* * *


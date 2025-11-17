##### Write/Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
# PulseTimingDevice Property

* * *

#### Description

| Sets and reads the device being controlled by the pulse generator output.  
---|---  
  
####  VB Syntax

| obj.TriggerInType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse | A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object)  
value | (enum NAPulseGenToDevice) Choose from: 0 \- ADC_TRIGGER - Enables offset pulses using ADC delay. 1 - RF_MODULATOR \- Iindicates that the pulse signal is used to drive the RF modulator. Only one pulse generator output can be used to drive an RF source. If you try to set more than one pulse generator output to RF_MODULATOR, then the other one will be set to UserN (where "N" is the pulse generator number) 2 - ADC_ACTIVITY \- (Pulse4 only) Pulse4 can also be set to monitor ADC activity. This selection outputs a signal on Pulse4 when the ADC is active. This is the same as [Pulse4OutAsADCActivity](Pulse4OutAsADCActivity_Property.md).  3 \- USER1 \- Use Pulse1 to control a DUT, DC biases, or other signals. 4 \- USER2 \- Use Pulse2 to control a DUT, DC biases, or other signals. 5 \- USER3 \- Use Pulse3 to control a DUT, DC biases, or other signals. 6 \- USER4 \- Use Pulse4 to control a DUT, DC biases, or other signals.  
  
#### Return Type

| Enum  
  
#### Default

| RF_MODULATOR  
  
#### Exaamples

| pulse.PulseTimingDevice = RF_MODULATOR 'Write  
value = pulse.PulseTimingDevice 'Read the value  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_PulseTimingDevice(enum NAPulseGenToDevice *val);  
HRESULT put_PulseTimingDevice(enum NAPulseGenToDevice val);  
  
#### Interface

| IPulseGenerator6  
  
* * *


##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## PortMatching_C Property

* * *

#### Description

|  Sets and returns the value for the 'C' (Capacitance) circuit element for a
port matching circuit model to simulate on port 'n'. The port matching circuit
model is selected using
[PortMatchingCktModel](PortMatchingCktModel_Property.md). You can specify C,
C1, or C2 based on the selected port matching circuit model. Setting a value
not used by the selected circuit will have no affect. Learn more. There are
three steps to set up a port matching circuit model simulation on a specified
port:

  1. Select the port matching circuit model to simulate using [PortMatchingCktModel](PortMatchingCktModel_Property.md).
  2. Set the values for R (Resistance), G (Conductance), C (Capacitance), and L (Inductance) corresponding to the selected port matching circuit model.
  3. Turn the feature on using [PortMatchingState](PortMatchingState_Property.md) to simulate the circuit and compute the measurement as if the circuit were attached to the port.

Note: This command affects ALL measurements on the channel.  
---|---  
  
####  VB Syntax

|  fixture.PortMatching_C(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive capacitance value  
value |  (Double) Capacitance value in farads. Choose a value between -1E18 to 1E18.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  fixture.PortMatching_C(2) = .00002 'Write  
value = fixture.PortMatching_C(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortMatching_C(short port double *pVal)  
HRESULT put_PortMatching_C(short port double newVal)  
  
#### Interface

|  IFixturing7


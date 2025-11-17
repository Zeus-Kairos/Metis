##### Write/Read

|

##### About Power Compensation  
  
---|---  
  
## EnablePowerCompensation Property

* * *

#### Description

|  Adjusts the source power at the specified port by the combined amount of
loss through ALL enabled fixturing operations. Use this function to set the
power level at the DUT input. Learn more. Note: This command affects ALL
measurements on the specified channel.  
---|---  
  
####  VB Syntax

|  fixture.EnablePowerCompensation (port) = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive power compensation.  
bool |  (Boolean) True \- Compensate source power False \- Do NOT compensate source power  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.EnablePowerCompensation(1) = True  
value = fixture.EnablePowerCompensation(2) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_EnablePowerCompensation(short port, VARIANT_BOOL *pState );
HRESULT put_EnablePowerCompensation(short port, VARIANT_BOOL bVal);  
  
#### Interface

|  IFixturing5  
  
* * *


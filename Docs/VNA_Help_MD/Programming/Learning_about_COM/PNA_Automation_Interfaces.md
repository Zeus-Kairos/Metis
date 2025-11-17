# VNA Interfaces

* * *

A COM interface is the connection to an object. When you [get a handle to an
object](Getting_a_Handle_to_an_Object.htm), you are actually using an
interface to an object. This subtle distinction is relevant to the COM
programmer for the following two reasons:

  * [Interface Inheritance (Coding for Multiple VNA Versions](PNA_Automation_Interfaces.md#Multiple))

  * [Custom Interfaces.](PNA_Automation_Interfaces.md#Custom)

[Other Topics about COM Concepts](Learning_about_COM.md)

### Interface Inheritance (Coding for Multiple VNA Versions)

The VNA continues to evolve and release [new firmware / software
versions](../../Whats_New.htm) that provide more functionality and features.
New commands are added to existing objects, and with them new interfaces are
added to support those commands. For example, new commands were added to the
Measurement object in VNA release 3.0. These commands are accessible from the
new IMeasurement2 interface. This can be important if you develop code using
the type library in release 3.0, and run the code on a VNA with an older
release, such as 2.0

When you use a command that was new with release 3.0, and you run that code on
a VNA with release 2.0 firmware, errors will occur because that VNA does not
recognize the new commands. However, even if you do NOT utilize new commands,
errors can still occur. The following example shows how this occurs and how to
avoid it.

The following Visual Basic statement dimensions the meas variable as an
object.

Dim meas As Measurement

When the program compiles, Visual Basic figures out what interface to use to
access that object. When dimensioning as an object, VB will use the default
interface. As new interfaces are added to an object, they become the default
interface. If this program was developed and compiled using the VNA 3.0 type
library, the default Interface of the Measurement Object was IMeasurement2.
However, if this program is run on an instrument with VNA 2.0 firmware, there
was no IMeasurement2 Interface, and an E_NOINTERFACE error will occur.

Therefore, the more robust approach would be to specify the interface instead
of the object when declaring a variable.

Dim meas As IMeasurement

This code will ONLY use the IMeasurement interface; not the default interface.

However, regardless of how you declare a variable, errors will always occur if
you use new commands, and run the code on an older instrument.

### Custom Interfaces

The VNA object model contains three "custom" interfaces use "typed" variables,
which is more efficient than using variant type variables. However, these
interfaces are only usable from VB6, C, & C++. All other programming languages
must use the other standard interfaces.

The custom interfaces are:

  * [IArrayTransfer](../COM_Reference/Objects/Measurement_Object.md#IArrayTransfer) \- Measurement object

  * [ICalData](../COM_Reference/Objects/Calibrator_Object.md#ICalData) \- Calibrator object

  * [ISourcePowerCalData](../COM_Reference/Objects/Channel_Object.md#ISourcePowerCalData) \- Channel object

* * *


# COM Data Types

* * *

The VNA uses several data types to communicate with the host computer. Before
using a variable, it is best to declare the variable as the type of data it
will store. It saves memory and is usually faster to access. The following are
the most common data types:

  * [Long Integer](COM_Data_Types.md#long)

  * [Single Precision (Real)](COM_Data_Types.md#sing)

  * [Double Precision (Real)](COM_Data_Types.md#doub)

  * [Boolean](COM_Data_Types.md#bool)

  * [String](COM_Data_Types.md#string)

  * [Object](COM_Data_Types.md#object)

  * [Enumeration](COM_Data_Types.md#enum)

  * [Variant](COM_Data_Types.md#var)

[Other Topics about COM Concepts](Learning_about_COM.md)

Long (long integer) variables are stored as signed 32-bit (4-byte) numbers
ranging in value from -2,147,483,648 to 2,147,483,647.

* * *

Double (double-precision floating-point) variables are stored as IEEE 64-bit
(8-byte) floating-point numbers ranging in value from -1.79769313486232E308 to
-4.94065645841247E-324 for negative values and from 4.94065645841247E-324 to
1.79769313486232E308 for positive values.

* * *

Single (single-precision floating-point) variables are stored as IEEE 32-bit
(4-byte) floating-point numbers, ranging in value from -3.402823E38 to
-1.401298E-45 for negative values and from 1.401298E-45 to 3.402823E38 for
positive values.

* * *

Boolean variables are stored as 16-bit (2-byte) numbers, but they can only be
True or False. Use the keywords True and False to assign one of the two states
to Boolean variables.

When other numeric types are converted to Boolean values, 0 becomes False and
all other values become True. When Boolean values are converted to other data
types, False becomes 0 and True becomes -1.

The following properties return True rather than 1 to conform with this
definition. This may affect the functionality of your COM program:

  * [Bandwidth Tracking Property](../COM_Reference/Properties/Bandwidth_Tracking_Property.md)

  * [ErrorCorrection Property](../COM_Reference/Properties/Error_Correction_Property.md)

  * [Interpolate Correction Property](../COM_Reference/Properties/Interpolate_Correction_Property.md)

  * [LimitTestFailed Property](../COM_Reference/Properties/LimitTestFailed_Property.md)

* * *

String variables hold character information. A String variable can contain
approximately 65,535 bytes (64K), is either fixed-length or variable-length,
and contains one character per byte. Fixed-length strings are declared to be a
specific length. Variable-length strings can be any length up to 64K, less a
small amount of storage overhead.

* * *

Object variables are stored as 32-bit (4-byte) addresses that refer to objects
within the analyzer or within some other application. A variable declared as
Object is one that can subsequently be assigned (using the Set statement) to
refer to any actual analyzer object.

* * *

Enumerations (Enum) are a set of named constant values. They allow the
programmer to refer to a constant value by name instead of by number. For
example:

Enum DaysOfWeek  
Sunday = 0  
Monday = 1  
Tuesday = 2  
Wednesday = 3  
Thursday = 4  
Friday = 5  
Saturday = 6  
End Enum

Given this set of enumerations, the programmer can then pass a constant value
as follows:  
SetTheDay(Monday)  
rather than  
SetTheDay(1)  
where the reader of the code has no idea what the value 1 refers to.

However, the analyzer RETURNS a long integer, not the text.  
Day = DaysofWeek(today) 'Day = 1

* * *

Variant \- If you don't declare a data type ("typed" data) the variable is
given the Variant data type. The Variant data type is like a chameleon  it
can represent many different data types in different situations.

The VNA provides and receives Variant data because there are programming
languages that cannot send or receive "typed" data. Variant data transfers at
a slower rate than "typed" data.

* * *


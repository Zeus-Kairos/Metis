# Status Command Keywords

* * *

The following keywords can be appended to the node or nodes that represent the
Status register you want to control.

  * [:CONDition?](Status_Keywords.md#cond)

  * [:ENABle](Status_Keywords.md#enab)

  * [:ENABle?](Status_Keywords.md#enabQ)

  * [:EVENt?](Status_Keywords.md#evq)

  * [:MAP](Status_Keywords.md#map)

  * [:NTRansition](Status_Keywords.md#ntr)

  * [:PTRansition](Status_Keywords.md#ptr)

[Learn about Status
Registers](../Learning_about_GPIB/Reading_the_Analyzers_Status_Registers.htm)

[SCPI Command Tree](SCPI_Command_Tree.md)

* * *

### :CONDition?

Monitors the conditions as they occur REAL TIME. That is, a condition may
occur, and then clear before the condition is read. Reading this register
returns a 16-bit decimal weighted number.

* * *

### :ENABle <bit>

Enables register bits that will monitored using the service request (SRQ)
method. (To use the direct read method, you do not have to enable the bit.)

Default value for STATus:QUEStionable:ENABle and STATus:OPERation:ENABle is 0:
No bits enabled.

Default value for all other registers :ENABle <bits> is 32767; ALL BITS
ENABLED.

Therefore it is ONLY necessary to send the ENABle keyword if you want to
DISABLE some conditions. For example, to enable ONLY Trace1 (bit 2) of the
LIMIT1 register (disable all other traces) , send:
STATus:QUEStionable:LIMit1:ENABle 4

* * *

### :ENABle?

Read the enable register to verify the bits that you enabled. Returns a 16 bit
weighted sum of the bits that are enabled.

* * *

### [:EVENt]?

Query only - This is the Default keyword for most registers. Use it to
determine if a condition has occured. These bits remain set until they are
read or otherwise cleared.

* * *

### :MAP <bit>,<error>

Associates a bit is the User register with an error number. For example

STATus:QUEStionable:DEFine:USER2:MAP 0,-113

0 is the bit that will be set

-113 is the error

When error -113 "Undefined Header" occurs, bit 0 in the USER2 register will be
set to 1.

* * *

### :NTRansition <bits>

Write-Read - Negative Transition register bits set the condition to be set on
the Negative going (True to False) transition. Use this register if you are
only interested in a condition changing from True to False.

### :NTRansition?

queries the register to verify that you set a negative transition.

* * *

### :PTRansition <bits>

Write-Read - Positive Transition register bits set the condition to be set on
the False to True transition. Use this register if you are only interested in
the change of a condition from False to True.

### :PTRansition?

Queries the register to verify that you set a positive transition.


# Reading the Analyzer's Status Register

* * *

The VNA has several status registers that your program can read to know when
specific events occur. There are two methods of reading the status registers
in the analyzer: the Polled Bit method and the Service Request method.

  * [The Status Registers](Reading_the_Analyzers_Status_Registers.md#StatusRegisters)

  * [Setting and Reading Bits in Status Registers](Reading_the_Analyzers_Status_Registers.md#set_and_read)

  * [Polled Bit Method](Reading_the_Analyzers_Status_Registers.md#poll)

  * [Service Request Method](Reading_the_Analyzers_Status_Registers.md#srq)

### See Also

[IEE 482 Common commands](../GP-IB_Command_Finder/Common_Commands.md)

[Example: Status Reporting](../GPIB_Example_Programs/Status_Reporting.md)

[Status Commands](../GP-IB_Command_Finder/Status.md)

[IEEE 488.2 REGISTERS ON VNA AND HOW TO USE THEM FOR SYNCHRONIZATION WITH *OPC
AND PYTHON](https://support.keysight.com/KeysightdCX/s/knowledge-article-
detail?language=en_US&keyid=IEEE-488-2-Registers-on-VNA-and-how-to-use-them-
for-Synchronization-with-OPC-and-Python) (Keysight support article)

[Other Topics about GPIB Concepts](Learning_about_GPIB.md)

### Important Notes:

  * A new [Limit Line Fail command](../GP-IB_Command_Finder/Calculate/Limit.md#fail) that makes it easy to determine if Limit Line testing has failed.

  * [*OPC?](../GP-IB_Command_Finder/Common_Commands.md#opcq) can be used to easily determine when a channel has completed a sweep. This requires no interaction with the Status Register system. Most [VNA programming examples](../GPIB_Example_Programs/SCPI_Example_Programs.md) use *OPC?.

  * Most of the Status Register system can NOT be used with the [SCPIStringParser Object](../COM_Reference/Objects/SCPIStringParser_Object.md). However, *OPC? can be used.

### The Status Registers

Most of the status registers in the analyzer have sixteen bits. For
simplicity, this topic will illustrate their use with 8-bit registers. Bits in
registers represent the status of different conditions inside of the analyzer.
In the following graphic, a register is represented by a row of boxes; each
box represents a bit. Bit 3 is ON.

![](../../assets/images/Programming/status.gif)

Each VNA Status Register is actually comprised of the following registers.
[See an image of the VNA Status registers.](javascript:BSSCPopup\('../GP-
IB_Command_Finder/Status.htm'\))

  * Enable Registers - When using the [SRQ method of polling](Reading_the_Analyzers_Status_Registers.md#srq), you first set bits in the enable register which tells the VNA which events to monitor. This is not necessary using the [Polled Bit method](Reading_the_Analyzers_Status_Registers.md#poll), as you can only monitor a single event. A *CLS (clear status) command will not clear the enable register. The *ESE and *ESE? commands are used to set and query Enable bits, while *ESR is used to read and clear an Enable register. [Learn how to set bits](Reading_the_Analyzers_Status_Registers.md#set_and_read).

  * Condition Registers - A condition register continuously monitors events in the VNA. Bits in the condition register change real time as conditions occur. These bits are not latched, so this register is used mainly for diagnostic purposes. The registers that only summarize lower level registers do NOT have a condition register.

  * Event Registers - This is the register that is read to determine if an event has occurred. An event register latches the bits from the corresponding condition register. When an event register bit is set, subsequent changes to the corresponding condition register bit are ignored. The bit remains set until a query command such as *CLS clears the bit. [Learn how to read the Event Register.](Reading_the_Analyzers_Status_Registers.md#set_and_read)

  * Positive and Negative Transition Registers \- Transition registers control what type of condition register will set the corresponding bit in the event register.

  *     * Positive transitions (0 to 1) are only reported to the event register if the corresponding positive transition bit is set to 1.

    * Negative transitions (1 to 0) are only reported to the event register if the corresponding negative transition bit is set to 1.

    * Setting both transition bits to 1 causes both positive and negative transitions to be reported.

Transition registers are read-write and are unaffected by *CLS (clear status)
or queries. They are reset to their default settings at power-up and after
*RST and SYSTem:PRESet commands. The following are the default settings for
the transition registers:

  1.      * All Positive Transition registers = 1

     * All Negative Transition registers = 0

This means that, by default, the analyzer will latch all event registers on
the negative to positive transition (0 to 1).

The following is an example of why you would set transition registers:

A critical measurement requires that you average 10 measurements and then
restart averaging. You decide to poll the averaging bit. When averaging is
complete, the bit makes a positive transition. After restart, you poll the bit
to ensure that it is set back from 1 to 0, a negative transition. You set the
negative transition bit for the averaging register.

### Setting and Reading Bits in Status Registers

Both the Polled-Bit method and Service Request method require that you set and
read status register bits. Most of the VNA status registers contain 16 bits,
numbered 0 to 15. Each bit has a weighted value. The following example shows
how to set the bits in a 8-bit status register.

8-bit register

Bit | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7  
---|---|---|---|---|---|---|---|---  
Weight | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128  
  
How to set bits 4 and 5 in the Standard Event Status Enable register:

Step | Example  
---|---  
1\. Determine the weighted bit value for these bits | weights 16 and 32 (respectively)  
2\. Add these values together | 16 \+ 32 = 48  
3\. Send this number as an argument in the appropriate command. (see [Status Commands](../GP-IB_Command_Finder/Status.md)) | STAT:QUES:LIMIT1:ENAB 48  
  
* * *

### The Polled Bit Method

With the Polled Bit Method, your program monitors a bit in the status register
that represents the condition of interest to you. When the VNA sets the bit to
1, your program sees it and responds accordingly.

  * If your program periodically monitors a bit in the status register, it is free to do other things as well. However, your program can respond only as fast as the bit is polled.

  * If your program continually monitors a bit, it can respond immediately, but will be unavailable to do anything other than poll the bit.

Advantage: This method requires very little programming.

Procedure:

  1. Decide which condition to monitor. The [Status Commands](../GP-IB_Command_Finder/Status.md) topic lists all of the possible conditions that can be monitored in the analyzer.

  2. Determine the command to be used to monitor the bit.

  3. Determine how often to poll the bit until it is set.

  4. Construct the routine to respond when the bit is set.

* * *

### The Service Request (SRQ) Method

Your program enables the bits in the status registers representing the
condition of interest. When the condition occurs, the VNA actively interrupts
your program from whatever it is doing, and an event handler in your program
responds accordingly. Do this method if you have several conditions you want
to monitor or the conditions are such that it is not practical to wait for the
condition to occur.

Advantage: This method frees your program to do other things until the
condition occurs. The program is interrupted to respond to the condition.

Disadvantage: This method can require extensive programming depending on the
number and type of conditions that you want to monitor.

Procedure:

1\. Decide which conditions to monitor. The [Status Commands](../GP-
IB_Command_Finder/Status.htm) topic lists all of the possible analyzer
conditions that can be monitored.

2\. Set the enable bits in the summary registers and the status byte register.

Enabling is like making power available to a light. Without power available,
the switch can be activated, but the light won't turn ON. In the analyzer,
without first enabling a bit, the condition may occur, but the controller
won't see it unless it is enabled.

The condition, and the bit in the summary registers in the reporting path,
must be enabled. This is like streams (conditions) flowing into rivers
(summary registers), and rivers flowing into the ocean (controller). See the
diagram of status registers in [Status Commands](../GP-
IB_Command_Finder/Status.htm).

Bit 6 of the status byte register is the only bit that can interrupt the
controller. When any representative bit in the status byte register goes ON,
bit 6 is automatically switched ON.

3\. Enable your program to interrupt the controller. This is done several ways
depending on the programming language and GPIB interface card you use. An
[example program](../GPIB_Example_Programs/Status_Reporting.md) is provided
showing how this is done with in Visual Basic with a National Instruments GPIB
card.

4\. Construct a subroutine to handle the interrupt event. If you are
monitoring more than one condition in your system, your event handler must
determine which condition caused the interrupt. Use the *SPE command to
determine the instrument that caused the interrupt, then poll the summary
registers, then poll condition registers to determine the cause of the
interrupt.

* * *


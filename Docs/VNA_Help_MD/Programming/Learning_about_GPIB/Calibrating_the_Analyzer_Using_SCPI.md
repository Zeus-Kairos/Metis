# Calibrating the Analyzer Using SCPI

* * *

There are several ways to calibrate the analyzer using SCPI depending on your
measurement needs. As from the Cal Wizard, you can perform a Guided Cal,
Unguided Cal, or ECal. This topic explains the differences in these
calibration choices when using SCPI commands.

  * [Guided Calibrations](Calibrating_the_Analyzer_Using_SCPI.md#Guided)

  * [ECal](Calibrating_the_Analyzer_Using_SCPI.md#ECal)

  * [Creating Cal Sets](Calibrating_the_Analyzer_Using_SCPI.md#CreateCalSet)

  * [Applying Cal Sets and Cal Types](Calibrating_the_Analyzer_Using_SCPI.md#Applying)

  * [Uploading Error Terms](Calibrating_the_Analyzer_Using_SCPI.md#Uploading)

  * [Unguided Cals and Calibration Classes](Calibrating_the_Analyzer_Using_SCPI.md#UnguidedClass)

Note: ALWAYS send ALL measurement setup commands BEFORE initializing a remote
calibration.

### See Also

[Synchronizing the Analyzer and Controller (During a
calibration)](Understanding_Command_Synchronization.htm#Synch)

[See SCPI Calibration
Examples](../GPIB_Example_Programs/SCPI_Example_Programs.htm)

Guided Calibrations

Guided versus Unguided is the style of calibration that is selected on the
first page of the [Calibration Wizard](../../S3_Cals/Calibration_Wizard.md).
A remote 'guided' cal does not present the cal wizard, but prompts for
specific standards to be connected. In a remote 'Unguided', the steps must be
'hard-coded'.

  * To perform a Guided Calibration, use ONLY [Sens:Corr:Coll:Guided](../GP-IB_Command_Finder/Sense/CorrGuided.md) commands.

  * These commands calibrate the ACTIVE channel. Activate a channel by selecting a measurement on the channel to be calibrated using [Calc:Par:Select.](../GP-IB_Command_Finder/Calculate/Parameter.md#cps)

  * Full 1,2,3,4-port SOLT and TRL calibrations - No response cals.

  * All of the advanced calibration features (Thru method, specify DUT connectors and Cal kits for each port, port pairings).

  * A Cal Set is applied to the channel and saved at the completion of a guided cal according to the preference setting [SENS:CORR:PREF:CSET:SAVE](../GP-IB_Command_Finder/Sense/Sense_Correction.md#CsetSave)

Note: To perform an Unguided Calibration, use ONLY the [Sens:Corr](../GP-
IB_Command_Finder/Sense/Sense_Correction.htm) commands (NOT Guided).

ECal

From the Cal Wizard or from a SCPI program, ECal is fast, accurate, and very
repeatable. Unlike from the Cal Wizard, you can use SCPI to perform ECal using
either the Guided or Unguided commands. The Unguided commands are easiest to
use. However, the following situations require that you use the Guided
commands.

  * To maximize accuracy, all ECal calibrations on the analyzer perform an Unknown Thru measurement of the ECal module Thru state IF the analyzer model being used has [1 reference receiver per port](../../Support/Configurations.md). If your analyzer does NOT have 1 reference receiver per port, use Guided ECal commands and specify a Thru method.

  * If your ECal module connectors do NOT match the DUT connectors, and you choose not to perform a User Characterization, use Guided ECal commands and specify the Thru method.

ECAL Notes:

  * When using either Guided or Unguided ECal commands under low power situations, use the Orientation settings. The Guided example shows the use of these commands. When using Unguided, they must appear before the Acquire command.

  * The frequency range of the measurement must be within the range of the ECal module. Otherwise, the calibration will fail.

  * You do NOT have to send the ECal module state 'switch' commands. The ECal algorithm switches ECal states automatically.

  * All of these ECal choices are listed in the [Programming Command Finder](../CalTopic.md) function in this Help file.

See [Using ECal](../../S3_Cals/Using_ECal.md) to learn about all of the ECal
features.

Creating Cal Sets

There are several ways to store guided cal data into a unique Cal Set. The
following is probably the easiest. It does not require the name of an existing
Cal Set and it allows you to name the Cal Set.

[SENS:CORR:COLL:GUID:INIT](../GP-IB_Command_Finder/Sense/CorrGuided.md#gInit)
'start the cal with no cal set argument 'Perform the cal
[SENS:CORR:COLL:GUID:SAVE](../GP-IB_Command_Finder/Sense/CorrGuided.md#gSave)
'create cal set with auto-generated name or to cal register
[SENS:CORR:CSET:NAME 'MyCalSet'](../GP-
IB_Command_Finder/Sense/CorrCset.htm#name) 'name the current cal set.  
---  
  
Applying Cal Sets and Cal Types

A Cal Set is applied to the channel and saved at the completion of a guided
cal according to the preference setting [SENS:CORR:PREF:CSET:SAVE](../GP-
IB_Command_Finder/Sense/Sense_Correction.htm#CsetSave).

When you select a Cal Set to apply to an uncalibrated channel, the analyzer
attempts to find the most comprehensive calibration type in the Cal Set and
turn it ON. In addition, changing a measurement parameter (for example, from
S11 to S21) will also initiate an attempt to apply the best Cal Type and turn
correction ON.

There may be times when you do not want the most comprehensive Cal Type. For
example, say there is a Full 2-port Cal Set applied, but there is only an S11
measurement displayed. If measurement speed is a concern, you can apply a Full
1-Port Cal Type from that same Cal Set and save time by not doing the extra
background sweeps. [Learn more about background
sweeps.](../../S2_Opt/Fast_Swp.htm#cal)

If you change the measurement parameter, the analyzer will reapply the Full
2-Port Cal Type.

See the SCPI and COM commands for [Cal Sets](../CalTopic.md#sets) and [Cal
Types](../CalTopic.htm#CalType).

Uploading Error Terms

Note: There was a method described here for WinCal 3.x that involved a
[preference setting](../GP-
IB_Command_Finder/Sense/Sense_Correction.htm#Simcal). That method is no longer
supported.

To upload error terms into a created or selected Cal Set:

SENS:CORR:CSET:CREAte or SENS:CORR:CSET:GUID  
SENS:CORR:CSET:Data <term> <port> <port> <data>  
SENS:CORR:CSET:SAVE

This method puts error terms into a Cal Set, outside of a Guided or Unguided
calibration session.

The Cal Set can then be applied at any time.

See [SENS:CORR:CSET](../GP-IB_Command_Finder/Sense/CorrCset.md) commands.

Unguided Cals and Calibration Classes

  * Use [Sens:Correction](../GP-IB_Command_Finder/Sense/Sense_Correction.md) commands.

  * 1-port, 2-port, Response.

  * Can select 2 sets of standards.

  * TRL is NOT recommended.

The following describes how to perform an unguided calibration using SCPI. The
objective here is to make clear the relationship between the physical port on
which a standard is being measured, the actual device in the cal kit, and the
SCPI command used to acquire the device.

Calibration standards classes are categories of standard types. To perform a
2 port calibration, the cal wizard requires the following types of standards
to be measured:

3 reflection standards on the forward port:

  * Class S11A typically an open

  * Class S11B typically a short

  * Class S11C typically a load

Likewise, 3 reflection standards are required for the reverse port:

  * Class S22A typically an open

  * Class S22B typically a short

  * Class S22C typically a load

There is also a transmission standard that is measured in both directions:

  * Class S21T typically a thru

The following illustrates the relationship between cal kit physical standards
and calibration classes. Here is a list of the physical devices in my
calibration kit.

Standard #1 = "3.5 mm male short"

Standard #2 = "3.5 mm male open"

Standard #3 = "3.5 mm male broadband load"

Standard #4 = "Insertable thru standard"

Standard #5 = "3.5 mm male sliding load"

Standard #6 = "3.5 mm male lowband load"

Standard #7 = "3.5 mm female short"

Standard #8 = "female to female characterized thru adapter"

Standard #9 = "0-2 Load"

Standard #10 = "Open"

Standard #11 = "Non-insertable thru"

Standard #12 = "3.5 mm female lowband load"

Standard #13 = "3.5 mm female sliding load"

Standard #14 = "3.5 mm female broadband load"

Standard #15 = "3.5 mm female open"

When you perform a calibration remotely using SCPI, you dont specify the
device number directly. Rather, you specify the class you want to measure.
Each device in the calibration kit is assigned to a class. And since more than
one device can be assigned to the same class, each class contains an ordered
list of devices. The class assignments are set using the Advanced Modify Cal
Kit dialog or the SCPI command:

[SENS:CORR:COLL:CKIT:ORDer](../GP-
IB_Command_Finder/Sense/CorrCollCKIT.htm#sccco)<class>, <std>, <std>, <std>,
<std>,<std>,<std>,<std>

The 85052B kit used in the example program has the following standard list for
each class: The list was obtained by issuing the corresponding SCPI query:

[SENS:CORR:COLL:CKIT:OLIST1?](../GP-
IB_Command_Finder/Sense/CorrCollCKIT.htm#olist) S11A = +2,+15,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST2? S11B = +1,+7,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST3? S11C = +6,+5,+3,+12,+13,+14,+0

SENS:CORR:COLL:CKIT:OLIST4? S21T = +4,+8,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST5? S22A = +2,+15,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST6? S22B = +1,+7,+0,+0,+0,+0,+0

SENS:CORR:COLL:CKIT:OLIST7? S22C = +6,+5,+3,+12,+13,+14,+0

SENS:CORR:COLL:CKIT:OLIST8? S12T = +4,+8,+0,+0,+0,+0,+0

When you perform the calibration, you acquire data by issuing the ACQuire
command:

[SENS:CORR:COLL:ACQ <class>[, <subst> ]](../GP-
IB_Command_Finder/Sense/Sense_Correction.htm#scca)

For example:

[SENS:CORR:COLL:SFOR](../GP-
IB_Command_Finder/Sense/Sense_Correction.htm#sforward) 1

SENS:CORR:COLL:ACQ STANA, SST2

The SFOR command tells the wizard to make the next acquisition in the forward
direction. The ACQuire command specifies that we are measuring the 2nd device
in the list for STANA. And since we are measuring SFORward, then STANA refers
to class #1 or S11A. The list of devices for this class are specified in the
OLIST1 query above.

Alternately, you could modify the device order for the S11A class to move
device #15 into the first position (SENS:CORR:COLL:CKIT:ORDER1). When the
desired device is in the first position, you need not specify the order number
in the ACQuire command. The default is the first device in the OLIST. This
works well for two port network analyzers where the order for S11A,B,C classes
is set up for port 1 and the order for S22A,B,C is set up for port 2. With the
kit set up in the proper order, you eliminate the need to specify the
substandard number (SST<n>).

[See an example: Perform an Unguided 2-port Cal on a 4-port
analyzer.](../GPIB_Example_Programs/Perform_an_Unguided_Cal_on_a_4-Port_PNA_using_SCPI.htm)


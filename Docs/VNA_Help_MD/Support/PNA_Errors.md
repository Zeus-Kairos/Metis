# Analyzer Error Messages

* * *

  * [500 - 750 Calibrate](PNA_Errors.md#Cal)

  * [770 - 1000 Hardware](PNA_Errors.md#Hardware)

  * [1000 - 1200 Measure](PNA_Errors.md#Measure)

  * [1281 - 1535 Parser](PNA_Errors.md#Parser)

  * [1536 - 1650 Display](PNA_Errors.md#Display)

  * [1700 - 2000 Channel](PNA_Errors.md#Channel)

  * 2001 \- 3021 General

  * [Standard SCPI Errors](SCPI_Errors.md)

Note: The EventID's listed below are provided for COM programming. For more
information, see [Working with analyzer
Events](../Programming/Learning_about_COM/Working_with_PNA_Events.htm)

See Also: [About Error Messages](About_Error_Messages.md)

### Memory Overflow Error

Memory overflow. Trigger state set to Hold. Lower the IF bandwidth, or
increase dwell or sweep time.

Severity: Informational

Further explanation: The measurement that you are currently making requires
that data be stored faster than it can be processed. Very few customers will
experience this situation.

Suggestions: To limit the amount of data to be stored, try lowering the IF
Bandwidth, slow the sweep time, increase the dwell time, or limit the number
of data points. There are many other settings that can be adjusted to solve
this problem.

EventID:

* * *

### Cal Errors

* * *

Message: 512

"A secondary parameter (power, IFBW, sweep time, step mode) of the calibrated
state has changed."

Severity: Informational

Further explanation: The calibration is questionable when any of these
secondary parameters change after the calibration is performed.

Suggestions: If you require an accurate measurement with the new settings,
repeat the calibration.

EventID: 68020200 (hex)

### Message: 513

"Calibration cannot be completed until you have measured all the necessary
standards for your selected Cal Type."

Severity: Informational

Further explanation: You probably received this message because you attempted
to turn correction on without first measuring all of the calibration standards

Suggestions: Finish measuring the cal standards

EventID: 68020201 (hex)

### Message: 514

"Calibration set has been recalled using a file previously saved on an
analyzer that had a different hardware configuration."

Severity: Informational

Further explanation:

Suggestions:

EventID: 68020202 (hex)

### Message: 515

"Calibration is required before correction can be turned on. Channel number is
<x>, Measurement is <x>."

Severity: Informational

Further explanation: There are no error correction terms to apply for the
specified channel and measurement.

Suggestions:Perform or recall a calibration

EventID: 68020203 (hex)

### Message: 516

"Critical parameters in your current instrument state do not match the
parameters for the calibration set, therefore correction has been turned off.
The critical instrument state parameters are sweep type, start frequency,
frequency span, and number of points."

Severity: Informational

Further explanation: None

Suggestions: You can either recalibrate using the new settings or change back
to the original setting that was used when the calibration was performed.

EventID: 68020204 (hex)

### Message: 517

"Interpolation is turned off and you have changed the stimulus settings of the
original calibration, so correction has been turned off."

Severity: Informational

Further explanation: The most accurate calibration is maintained only when the
original stimulus settings are used.

Suggestions: If reduced accuracy is OK, set interpolation ON to allow stimulus
setting changes.

EventID: 68020205 (hex)

### Message: 518

"Interpolation is turned off and you have selected correction ON. Correction
has been restored with the previous stimulus settings."

Severity: Informational

Further explanation: None

Suggestions: None

EventID: 68020206 (hex)

### Message: 519

"Stimulus settings for your current instrument state exceeded the parameters
of the original calibration, so correction has been turned off."

Severity: Informational

Further explanation: Correction data outside the stimulus settings does not
exist.

Suggestions: Perform a broadband calibration, with increased numbers of points
with interpolation ON, to maintain calibration over the widest possible
stimulus frequency settings.

EventID: 68020207(hex)

### Message: 520

"Cal Type is set to NONE for Channel <x>, Measurement <x>; please select
Calibration menu or press Cal hard key."

Severity: Informational

Further explanation: A cal operation can not proceed until a calibration
exists or the cal type is selected. This error can occur if the calibration
can not be found. Also this error can happen if a calibration type is not
specified before attempting to programmatically execute cal acquisitions.

Suggestions To find a calibration, select a Cal Set that contains the
calibration needed for the current measurements. OR specify the cal type
before beginning a calibration procedure.

EventID: 68020208 (hex)

### Message: 521

"The measurement you set up does not have a corresponding calibration type, so
correction has been turned off or is not permitted."

Severity: Informational

Further explanation: The calibration for the channel may apply only to certain
S-Parameters. For example, a 1-Port calibration for S11 can not be applied to
a 1-Port calibration applied to S22.

Suggestions: Select a calibration type, such as full 2-Port cal, that can be
applied to all the measurements to be selected.

EventID: 68020209 (hex)

### Message: 522

"The calibration type you selected cannot be set up."

Severity: Informational

Further explanation: "Please use the SCPI command
[ROUTe:PATH:DEFine:PORT](../Programming/GP-IB_Command_Finder/Route_SCPI.md)
<num>,<num> for full 2 port type port assignment."

Suggestions:

EventID: 6802020A (hex)

### Message: 523

"The calibration path you selected cannot be set up because it is not valid
for the current measurement."

Severity: Informational

Further explanation: "Please use the SCPI command
[ROUTe:PATH:DEFine:PORT](../Programming/GP-IB_Command_Finder/Route_SCPI.md)
<num>,<num> for full 2 port type port assignment related to your current
measurement."

Suggestions:

EventID: 6802020B (hex)

### Message: 524

"The source power calibration is complete."

Severity: Informational

Further explanation:

Suggestions:

EventID: 6802020C (hex)

### Message: 525

"You have specified more than 7 standards for one or more calibration
classes."

Severity: Informational

Further explanation: These have been truncated to 7 selections.

EventID: 6802020D (hex)

### Message: 526

"No user calibration found for this channel."

Severity: Informational

Further explanation: A cal operation can not proceed until a calibration
exists.

Suggestions: To find a calibration, you can select a Cal Set that contains the
calibration needed for the current measurement.

EventID: 6802020E (hex)

### Message: 527

"You do not need to acquire this standard for this calibration type."

Severity: Informational

Further explanation: This error can happen as a result of PROGRAMMATICALLY
requesting the measurement of an un-needed calibration standard during a
calibration procedure.

Suggestions: Check the specified cal type or eliminate the request for the
measurement of the standard.

EventID: 6802020F (hex)

### Message: 528

"Could not configure the Electronic Calibration system. Check to see if the
module is plugged into the proper connector."

Severity: Informational

Further explanation: During an ECal operation, communication could not be
established with the ECal module. The calibration will not be initiated until
the presence of the ECal module is verified.

Suggestions: Verify the USB cable is connected properly. Disconnect and re-
connect the cable to ensure the analyzer recognizes the module.

EventID: 68020210 (hex)

### Message: 529

"DATA OUT OF RANGE: Design Limits Exceeded"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020211(hex)

### Message: 530

"EXECUTION ERROR: Could not open ECal module memory backup file"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020212 (hex)

### Message: 531

"EXECUTION ERROR: Access to ECal module memory backup file was denied"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020213 (hex)

### Message: 532

"EXECUTION ERROR: Failure in writing to ECal module memory backup file"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020214 (hex)

### Message: 533

"EXECUTION ERROR: Failure in reading from ECal module memory backup file"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020215 (hex)

### Message: 534

"EXECUTION ERROR: Array index out of range"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020216 (hex)

### Message: 535

"EXECUTION ERROR: Arrays wrong rank"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020217 (hex)

### Message: 536

"EXECUTION ERROR: CPU"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020218 (hex)

### Message: 537

"EXECUTION ERROR: Cannot ERASE module"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020219 (hex)

### Message: 538

"EXECUTION ERROR: Cannot WRITE module"

Severity: Error

Further explanation:

Suggestions:

EventID: E802021A (hex)

### Message: 539

"EXECUTION ERROR: Entry Not Found"

Severity: Error

Further explanation:

Suggestions:

EventID: E802021B (hex)

### Message: 540

"EXECUTION ERROR: Invalid command while system is busy"

Severity: Error

Further explanation:

Suggestions:

EventID: E802021C (hex)

### Message: 541

"Electronic Cal: Unable to orient ECal module. Please ensure the module is
connected to the necessary measurement ports."

Severity: Error

Further explanation: There is no RF connection to the ECal module during a
calibration step. An ECal orientation measurement has been attempted but the
signal was not found.

Suggestions: Connect the ECal module RF connections to ports specified for the
calibration step. The ECal module typically requires at least -18dBm for
measurements. If your measurement requires the power level to be less than
that, clear the Do orientation checkbox to bypass the automatic detection
step.

EventID: E802021D (hex)

### Message: 542

"EXECUTION ERROR: NO SPACE for NEW CAL, DELETE A CAL"

Severity: Error

Further explanation:

Suggestions:

EventID: E802021E (hex)

### Message: 543

"EXECUTION ERROR: No More Room"

Severity: Error

Further explanation:

Suggestions:

EventID: E802021F (hex)

### Message: 544

"EXECUTION ERROR: Other array error"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020220 (hex)

### Message: 545

"EXECUTION ERROR: Ranks not equal"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020221 (hex)

### Message: 546

"EXECUTION ERROR: Too few CONSTANT ranks"

Severity: Error

EventID: E8020222 (hex)

### Message: 547

"EXECUTION ERROR: Too few VARYing ranks"

Severity: Error

EventID: E8020223 (hex)

### Message: 548

"EXECUTION ERROR: Unknown error"

Severity: Error

EventID: E8020224 (hex)

### Message: 549

"EXECUTION ERROR: ecaldrvr.dll bug or invalid module #"

Severity: Error

EventID: E8020225 (hex)

### Message: 550

"EXECUTION ERROR: unexpected error code from ecal driver"

Severity: Error

EventID: E8020226 (hex)

### Message: 551

"EXECUTION ERROR: unexpected internal driver error"

Severity: Error

EventID: E8020227 (hex)

### Message: 552

"HARDWARE ERROR: Can't access ECal Interface Module"

Severity: Error

EventID: E8020228 (hex)

### Message: 553

"HARDWARE ERROR: Can't release LPT port, reboot"

Severity: Error

EventID: E8020229 (hex)

### Message: 554

"HARDWARE ERROR: VNA Error"

Severity: Error

EventID: E802022A (hex)

### Message: 555

"HARDWARE ERROR: not enough data read from ECal module"

Severity: Error

EventID: E802022B (hex)

### Message: 556

"OPERATION ABORTED BY HOST COMPUTER"

Severity: Error

EventID: E802022C (hex)

### Message: 557

"OPERATION ABORTED BY USER"

Severity: Error

EventID: E802022D (hex)

### Message: 558

"OUT OF MEMORY"

Severity: Error

EventID: E802022E (hex)

### Message: 559

"QUERY INTERRUPTED:Message(s Abandoned"

Severity: Error

EventID: E802022F (hex)

### Message: 560

"QUERY UNTERMINATED: INCOMPLETE PROGRAM Message"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020230 (hex)

### Message: 561

"QUERY UNTERMINATED: NOTHING TO SAY"

Severity: Error

Further explanation:

Suggestions:

EventID: E8020231 (hex)

### Message: 562

"QUEUE OVERFLOW"

Severity: Error

EventID: E8020232 (hex)

### Message: 563

"SETTINGS CONFLICT: ADDITIONAL STANDARDS ARE NEEDED"

Severity: Error

EventID: E8020233 (hex)

### Message: 564

"SETTINGS CONFLICT: Adapter Cal is NOT possible"

Severity: Error

EventID: E8020234 (hex)

### Message: 565

"SETTINGS CONFLICT: COMMAND OUT OF SEQUENCE"

Severity: Error

EventID: E8020235 (hex)

### Message: 566

"SETTINGS CONFLICT: Cal STOPPED - VNA SETUP CHANGED"

Severity: Error

EventID: E8020236 (hex)

### Message: 567

"SETTINGS CONFLICT: Calibration is NOT in progress"

Severity: Error

EventID: E8020237 (hex)

### Message: 568

"SETTINGS CONFLICT: Can't find specified GPIB board"

Severity: Error

EventID: E8020238 (hex)

### Message: 569

"SETTINGS CONFLICT: Can't find/load gpib32.dll"

Severity: Error

EventID: E8020239 (hex)

### Message: 570

"SETTINGS CONFLICT: Can't find/load sicl32.dll"

Severity: Error

EventID: E802023A (hex)

### Message: 571

"SETTINGS CONFLICT: Can't initialize VNA (bad address?"

Severity: Error

EventID: E802023B (hex)

### Message: 572

"SETTINGS CONFLICT: Can't load LPT port driver or USB driver DLL"

Severity: Error

EventID: E802023C (hex)

### Message: 573

"SETTINGS CONFLICT: Invalid Calibration Sweep Mode."

Severity: Error

EventID: E802023D (hex)

### Message: 574

"SETTINGS CONFLICT: Invalid Calibration Type"

Severity: Error

EventID: E802023E (hex)

### Message: 575

"SETTINGS CONFLICT: Invalid Calibration"

Severity: Error

EventID: E802023F (hex)

### Message: 576

"SETTINGS CONFLICT: Invalid GPIB board number specified"

Severity: Error

EventID: E8020240 (hex)

### Message: 577

"SETTINGS CONFLICT: Invalid GPIB board type specified"

Severity: Error

EventID: E8020241 (hex)

### Message: 578

"SETTINGS CONFLICT: Invalid Module Status"

Severity: Error

EventID: E8020242 (hex)

### Message: 579

"SETTINGS CONFLICT: Invalid States"

Severity: Error

EventID: E8020243 (hex)

### Message: 580

"SETTINGS CONFLICT: LPT port must be between 1 and 4"

Severity: Error

EventID: E8020244 (hex)

### Message: 581

"Could not configure the Electronic Calibration system. Check to see if the
module is properly connected."

Severity: Error

EventID: E8020245 (hex)

### Message: 582

"SETTINGS CONFLICT: Specified LPT port does not exist"

Severity: Error

EventID: E8020246 (hex)

### Message: 583

"SETTINGS CONFLICT: Use frequency domain for cal"

Severity: Error

EventID: E8020247 (hex)

### Message: 584

"SETTINGS CONFLICT: Use step sweep type for cal."

Severity: Error

EventID: E8020248 (hex)

### Message: 585

"SETTINGS CONFLICT: VNA address must be between 0 and 30"

Severity: Error

EventID: E8020249 (hex)

### Message: 586

"SETTINGS CONFLICT: Wrong LPT port driver or USB driver DLL"

Severity: Error

EventID: E802024A (hex)

### Message: 587

"SYNTAX ERROR: ECAL:DELAY command must have 2 numbers"

Severity: Error

EventID: E802024B (hex)

### Message: 588

"SYNTAX ERROR: INCORRECT SYNTAX"

Severity: Error

EventID: E802024C (hex)

### Message: 589

"SYNTAX ERROR: UNKNOWN COMMAND"

Severity: Error

EventID: E802024D (hex)

### Message: 590

"Wrong port of module in RF path"

Severity: Error

EventID: E802024E (hex)

### Message: 591

"User characterization not found in module"

Severity: Error

EventID: E802024F (hex)

### Message: 592

Severity:Informational

"No source power calibration found for the channel and source port of the
current measurement."

Further explanation: You tried to turn on source power cal but there is no
source power cal data.

Suggestions: Perform a source power calibration

EventID: 68020250 (hex)

### Message: 593

Severity:Informational

"A source power calibration sweep was not performed, so there is no correction
for the channel and source port of the current measurement."

Further explanation: You tried to turn on source power cal but there is
incomplete source cal data.

Suggestions:Perform a complete source power calibration

EventID: 68020251 (hex)

### Message: 594

Severity: Informational

"A new trace could not be added to the active window for viewing the source
power cal sweep, because it would have exceeded the limit on number of
traces/window. Please remove a trace from the window before proceeding with
source power cal."

Further explanation: The source power cal attempts to add a data trace to the
active window. The active window already contains four traces.

Suggestions:Make the active window contain less than trace limit.

EventID: 68020252 (hex)

### Message: 595

Severity: Informational

"A new measurement could not be added for performing the source power cal
sweep, because the limit on number of measurements has been reached. Please
remove a measurement before proceeding with source power cal."

Further explanation: The source power cal attempts to add a measurement. The
analyzer already has the maximum number of measurements.

Suggestions: Delete a measurement.

EventID: 68020253 (hex)

### Message: 596

Severity: Informational

"The calibration power value associated with the source power calibration of
Port %1 on Channel %2 was changed with the calibration on. The calibration was
not turned off, but the power value might no longer represent the
calibration."

Further explanation: The source power cal accuracy is questionable.

Suggestions: If high accuracy is required, perform another source power
calibration.

EventID: 68020254 (hex)

### Message: 597

Severity: Informational

\- Message that is passed from the power meter driver for a source power
calibration. -

Further explanation: This error is generated by the power meter driver and
passed through the analyzer.

EventID: 68020255 (hex)

### Message: 598

"During the acquisition of the sliding load standard, the slide was not
properly moved to perform a circle fit. The standard's raw impedance was used
to determine the directivity for one or more points."

Severity: Informational

Further Explanation: To accurately characterize the standard, the sliding load
must be move sufficiently to ensure enough samples around the complex circle
or Smith Chart. Under-sampling will cause an inaccurate result.

Suggestions:  For best results when using a sliding load, be sure to use
multiple slide positions that cover the full range of movement from front to
back of the slot.

EventID: 68020256 (hex)

### Message: 599

"This feature requires an unused channel, but could not find one. Please free
up a channel and try again."

Severity: Informational

Further Explanation: You attempted to view an item within a calset. However,
the calset viewer requires that the result be displayed in a channel that is
not currently in use. All the channels are currently used. The view can not
display the requested item.

Suggestions: You must delete at least one channel that is currently in use.

EventID: 68020257 (hex)

### Message: 600

"Interpolation of the original calibration is not allowed since it was
performed using Segment Sweep. Correction has been turned off."

Severity: Informational

EventID: 68020258 (hex)

### Message: 601

"Cal preferences saved. Cal preference settings can be changed from the 'Cal
Preferences' drop down Cal menu."

Severity: Informational

EventID: 68020259 (hex)

### Message: 608

"CalType not set."

Severity: Error

Further explanation: A cal operation can not proceed until a calibration
exists or the proper cal type is selected.

Suggestions: This error can happen if the calibration can't be found. To find
a calibration, you can select a Cal Set that contains the calibration needed
for the current measurements. This error can also happen if a calibration type
is not specified before attempting to programmatically execute cal
acquisitions. Specify the cal type before beginning a calibration procedure.

EventID: E8020260 (hex)

### Message: 609

"The Calibration feature requested is not implemented."

Further explanation: The specified cal type can be one of many choices. For
example, response calibrations require single standards, 1-Port calibrations
require 3 standards, and 2-Port calibrations require up to 12 standards.

Suggestions: Be sure to measure only the standards needed for the specified
cal type.

EventID: E8020261 (hex)

### Message: 610

"The Calibration Class Acquisition requested is not valid for the selected
Calibration Type. Please select a different acquisition or a different
Calibration Type."

EventID: E8020262 (hex)

### Message: 611

"The Calibration Standard data required for the selected caltype was not
found."

Severity: Error

Further explanation:  An unsuccessful attempt was made to retrieve a specified
standard from the raw measurement buffer. The buffer should contain the raw
measurements of cal standards stored during a calibration procedure.

Suggestions: Be sure the requested standard is required for the current cal
type. Not all standards are needed for all cal types.

EventID: E8020263 (hex)

### Message: 612

" The Error Term data required for the selected caltype was not found."

Severity: Error

Further explanation: An unsuccessful attempt was made to retrieve a specified
error term from the error correction buffer. The buffer should contain the
error correction arrays for the current calibration.

Suggestions: Be sure the requested error term is required for the current cal
type. Not all error terms are needed for all cal types.

EventID: E8020264 (hex)

### Message: 613

The Calibration data set was not found.

Severity: Error

Further explanation: An unsuccessful attempt to access a cal set has been
made. This may indicate a calset has been deleted or has been corrupted.

Suggestions: Try again or select another cal set. If the cal set appears in
the cal set list, it may need to be deleted.

EventID: E8020265 (hex)

### Message: 614

"The specified measurement does not have a calibration valid for Confidence
Check. Please select a different measurement, or recall or perform a different
Calibration Type."

Severity: Error

Further explanation: The measurement choice is prevented so that calibration
will not be turned off. Not all cal types support all measurements. For
example, an 1-Port cal on S11 can not be used to calibrate an S12 measurement.
When a measurement is selected that does not have a calibration which can be
applied, an informational message is displayed and calibration is turned off.

Suggestions: Use a full 2-Port calibration to be compatible with any
S-Parameter.

EventID: E8020266 (hex)

### Message: 615

" New calset created."

Severity: Informational message.

Further explanation: The newly created cal set will be automatically named and
time stamped. If this is the beginning of a calibration procedure, the cal set
will not be stored to memory until the calibration has completed successfully.
The new cal set will be deleted if the calibration is canceled or does not
otherwise complete successfully.

Suggestions: Informational

EventID: 68020267

### Message: 617

The calset file: <x> appears to be corrupted and cannot be removed. Exit the
application, remove the file, and restart.

Severity: Error

Suggestions: The cal set file is stored in the application home directory
D:\analyzerCalSets.dat. Remove this file, then restart the application.

EventID: E8020269 (hex)

### Message: 634

"The calset file: <x> load failed."

Severity: Error

Further explanation: The calset file contains a collection of calsets. The
file resides on the hard drive.

Suggestions: Try restarting the application. If the failure persists, you may
have to delete the cal set data file and restart the application. The cal set
file is stored in the application home directory. D:\analyzerCalSets.dat.
Remove this file, then restart the application.

EventID: E802027A (hex)

### Message: 635

"The calset file: <x> save failed."

Severity: Error

Further explanation: The file operation detected an error. The save operation
was aborted.

Suggestions: Retry.

EventID: E802027B (hex)

### Message: 636

"A calset was deleted."

Severity: Informational

Further explanation: One of the calsets has been successfully deleted from the
collection of calsets available. This can happen as the result of a user
request or intentional operation.

Suggestions: None

EventID: 6802027C (hex)

### Message: 637

"The version of the calset file: <x> is not compatible with the current
instrument."

Severity: Error

Further explanation: A versioning error can prevent a calset from being used.
This can happen as a result of instrument firmware upgrades.

Suggestions: If the versioning error is the result of firmware upgrade, you
will have to re-install the old version of firmware to re-use the calset file.
Or you can re-create the calsets with the current version of firmware.

The cal set file is stored in the application home directory
D:\analyzerCalSets.dat. Remove this file, then restart the application.

EventID: E802027D (hex)

### Message: 638

"Incompatible CalSets found: <x> of <y> stored calsets have been loaded."

Severity: Error

Further explanation: Errors were found on some of the calsets stored in the
calset file. The errors may have been caused by versioning issues that may
have corrupted the various calset keys.

Suggestions: Use the calset viewer to look at the contents of calset files.
Delete the files that are corrupted.

EventID: 6802027E (hex)

### Message: 639

"The Calset file: <x> was not found. A new file has been created."

Severity: Informational

Further explanation: The calset file should be stored on the hard drive. When
the application is started, a search is done and the file is loaded if it can
be found. If the file is not found, the analyzer will create a new file and
display this message.

Suggestions: None

EventID: 6802027F (hex)

### Message: 640

"The Calset specified is currently in use."

Severity: Error

Further explanation: This may indicate a conflict between multiple calset
users attempting calibration tasks.

Suggestions: Save the instrument state. Preset the analyzer and recall the
instrument state. This may abort any processes that may be in progress.

EventID: E8020280 (hex)

### Message: 641

"The calset specified has not been opened."

Severity: Error

Further explanation: Multiple users may be attempting to access the calset.

Suggestions: Close multiple calset users so that only one user will access the
calset.

EventID: E8020281 (hex)

### Message: 642

"The maximum number of cal sets has been reached. Delete old or unused cal
sets before attempting to create new ones."

Severity: Error

Suggestions: You may also delete the calsets data file.

The cal set file is stored in the application home directory.
D:\analyzerCalSets.dat. Remove this file, then restart the application.

EventID: E8020282 (hex)

### Message: 643

The requested power loss table segment was not found.

Severity: Error

EventID: E8020283 (hex)

### Message: 644

"A valid calibration is required before correction can be turned on."

Severity: Error

Further explanation: This usually indicates a calibration procedure has not
run to completion or that the selected measurement does not have a valid
calibration available from within the currently selected cal set.

Suggestions: To find a calibration, you can select a Cal Set that contains the
calibration needed for the current measurements. This error can happen if a
calibration type is not specified before attempting to programmatically
execute cal acquisitions. Specify the cal type before beginning a calibration
procedure.

EventID: E8020284 (hex)

### Message: 645

The cal data for <x> is incompatible and was not restored. Please
recalibrate."

Severity: Warning

Further explanation: None

Suggestions: None

EventID: A8020285 (hex)

### Message: 646

"CalSet not loaded, version is too new."

Severity: Error

Further explanation: An old version of firmware is attempting to run with a
new calset version. The version is incompatible.

Suggestions: The calset can be removed. You may also delete the calsets data
file if you are migrating between various firmware revisions often and you
would like to avoid this error. The cal set file is stored in the application
home directory. D:\analyzerCalSets.dat. Remove this file, then restart the
application.

EventID: E8020286 (hex)

### Message: 647

"Custom cal type not found."

Severity: Error

Further explanation:

Suggestions:

EventID: E8020287 (hex)

### Message: 648

"Custom correction algorithm defers to the client for interpolation."

Severity: Informational

EventID: 68020288 (hex)

### Message: 649

"Custom cal dll threw an exception."

Severity: Error

EventID: E8020289 (hex)

### Message: 650

"Could not load the ecal.dll library"

Severity: Error

EventID: E802028A (hex)

### Message: 656

"The argument specified is not a valid cal type."

Severity: Error

EventID: E8020290 (hex)

### Message: 657

"The function found existing interpolated data"

Severity: Informational

EventID: 68020291 (hex)

### Message: 658

"The function computed new interpolation values."

Severity: Informational

EventID: 68020292 (hex)

### Message: 659

"The source power measurement failed."

Severity: Error

Suggestions: Please check GPIB, power meter settings and sensor connections.

EventID: E8020293 (hex)

### Message: 660

"Duplicate session found. Close session and retry."

Severity: Error

EventID: E8020294 (hex)

### Message: 661

"The session does not exist. Open the session and try again."

Severity: Error

Further explanation:

EventID: E8020295 (hex)

### Message: 662

"Attempt to launch a custom calibration failed."

Severity: Error

Further explanation:

EventID: E8020296 (hex)

### Message: 663

"Request to measure a cal standard failed."

Severity: Error

Further explanation: Please ensure you are requesting to measure standards
which are defined for this calibration.

EventID: E8020297 (hex)

### Message: 664

"Since Electronic Calibration Kit is selected, Mechanical Cal Kit parameter
cannot be changed."

Severity: Error

Further explanation:

EventID: E8020298 (hex)

### Message: 665

"Frequencies of the active channel are below minimum or above maximum
frequencies of the ECal module factory characterization."

Suggestions: Change the channel frequencies, or select another ECal module.

Severity: Error

EventID: E8020299 (hex)

### Message: 666

"Calset chosen for characterizing the ECal Module Ports %1 does not contain a
calibration for analyzer Ports %2."

Severity: Error

Suggestions: Go back to select another calset or to perform another cal.

EventID: E802029A (hex)

### Message: 667

"ECal module only has sufficient memory remaining to store a maximum of %1
points in User Characterization %2."

Severity: Error

Suggestions: Decrease your number of points, or choose to overwrite another
user characterization.

EventID: E802029B (hex)

### Message: 668

Input values are non-monotonic. Cannot interpolate.

Severity: Error

EventID: E802029C (hex)

### Message: 669

Interpolation target is out of range. Cannot interpolate.

Severity: Error

EventID: E802029D (hex)

### Message: 670

Guided Calibration Error: <>

Severity: Error

EventID: E802029E (hex)

### Message: 671

The first call to the guided calibration interface must be Initialize.

Severity: Error

EventID: E802029F (hex)

### Message: 672

The selected thru cal method was not recognized.

Severity: Error

EventID: E80202A0 (hex)

### Message: 673

Could not generate the error terms.

Severity: Error

EventID: E80202A1 (hex)

### Message: 674

Guided calibration must be performed on the active channel

Severity: Error

EventID: E80202A2 (hex)

### Message: 675

You can not start using calibration steps until you have successfully called
[generate steps](../Programming/CalTopic.md#guid).

Severity: Error

EventID: E80202A3 (hex)

### Message: 676

The step number given is out of range. Step numbers should be between 1 and
the number of steps. 0 is not a valid step number.

Severity: Error

EventID: E80202A4 (hex)

### Message: 677

A calset was selected for channel: <n> without restoring stimulus.

Severity: Informational

EventID: 680202A5 (hex)

### Message: 678

A calset was selected for channel: <n> restoring stimulus.

Severity: Informational

EventID: 680202A6 (hex)

### Message: 679

The selected calset stimulus could not be applied to the channel.

Severity: Informational

EventID: 680202A7 (hex)

### Message: 680

You attempted to measure power at a frequency outside the frequency range
defined for the specified power sensor. Select another sensor or adjust the
range for this sensor.

Severity: Error

EventID: E80202A8 (hex)

### Message: 681

Specified frequency is outside the frequency ranges currently defined for the
power meter's sensors.

Severity: Error

EventID: E80202A9 (hex)

### Message: 682

Additional Calibration Standards need to be acquired in order to calibrate
over the entire frequency range currently being measured.

Severity: Informational

EventID: 680202AA (hex)

### Message: 683

The analyzer failed to convert cal kits for use by unguided calibrations. The
recommended action is to restore Cal Kit defaults.

Severity: Error

EventID: E80202AB (hex)

### Message: 684

The analyzer failed to convert cal kits for use by unguided calibrations.
CalKit defaults have been restored.

Severity: Error

EventID: E80202AC (hex)

### Message: 685

Power meter is reserved by a source power cal acquisition already in progress.

Severity: Error

EventID: E80202AD (hex)

### Message: 686

Source power calibration has not been performed or uploaded for the specified
channel and source port.

Severity: Error

EventID: E80202AE (hex)

### Message: 687

Source power calibration data array size for the specified channel and source
port does not match it's associated stimulus number of points.

Severity: Error

EventID: E80202AF (hex)

### Message: 688

Source power calibration of Port <n> on Channel <n> was turned off because the
correction array no longer exists.

Severity: Error

EventID: E80202B0 (hex)

### Message: 689

This command can only be used on a measurement created with a specified
calibration loadport.

Severity: Error

EventID: E80202B1 (hex)

### Message: 690

Interpolation is turned off and you have changed the stimulus settings of the
original calibration, so correction has been turned off.

Severity: Error

EventID: E80202B2 (hex)

### Message: 691

Stimulus settings for your current instrument state exceeded the parameters of
the original calibration, so correction has been turned off.

Severity: Error

EventID: E80202B3 (hex)

### Message: 692

Fixturing: the requested S2P file cannot be read. Possible formatting problem.

Severity: Error

EventID: E80202B4 (hex)

### Message: 693

Fixturing: the requested S2P file cannot be opened.

Severity: Error

EventID: E80202B5 (hex)

### Message: 694

Fixturing: the requested S2P file cannot be interpolated. This is usually
because the frequency range in the file is a subset of the current channel
frequency range.

Severity: Error

EventID: E80202B6 (hex)

### Message: 695

Cal Registers can only be used by one channel: the channel conveyed in the
name of the cal register. The name cannot be changed.

Severity: Error

Further explanation: See [Cal Registers](../S3_Cals/Cal_Sets.md#Registers)

EventID: E80202B7 (hex)

### Message: 696

Fixturing: cannot be enabled with Response Calibrations and has been turned
off.

Severity: Error

EventID: E80202B8 (hex)

### Message: 697

The selected calibration cannot be performed for this measurement.

Severity: Error

EventID: E80202B9 (hex)

### Message: 698

Fitting: RemoveAllConnectors() should be called prior to calling AddConnector
after a fit has been attempted.

Severity: Error

EventID: E80202BA (hex)

### Message: 699

An attempt was made to acquire calibration data before the system was properly
initialized.

Severity: Error

EventID: E80202BB (hex)

### Message: 700

Use IGuidedCalibration for multiport calibration types.

Severity: Error

EventID: E80202BC (hex)

### Message: 701

Guided calibration requires number of thru measurement paths be at least equal
to the number of calibration ports minus 1.

Severity: Error

EventID: E80202BD (hex)

### Message: 702

A thru path was specified that includes a port which the calibration was not
specified to include.

Severity: Error

EventID: E80202BE (hex)

### Message: 703

One or more of the ports to be calibrated was not found in the set of
specified thru paths.

Severity: Error

EventID: E80202BF (hex)

* * *

### Hardware Errors

* * *

### Message: 770

Input power too high. Source power is off.

Severity: Warning

EventID: A8030302 (hex)

### Message: 771

Source power restored.

Severity: Informational

EventID: 68030303 (hex)

### Message: 772

"The spampnp.sys driver is not working. Check system hardware. ! Data will be
simulated. !"

Severity: Error

Further explanation: The Network Analyzer application cannot locate the DSP
board. Hardware or a driver may be malfunctioning. This is also common when
attempting to run the Network Analyzer on a workstation.

EventID: E8030304 (hex)

### Message: 773

"Instrument Serial Bus Not Working."

Severity: Error

Further explanation: The instrument EEPROM appears to contain either all ones
or all zeros. A serial bus hardware failure prevents reading the EEPROM.

EventID: E8030305 (hex)

### Message: 784

Unleveled, source 1, out 1.

Severity: Error

Further explanation: The analyzer was unable to set the power on port <n> to
the desired level

### Message: 785

Unleveled, source 1, out 2.

Severity: Error

Further explanation: The analyzer was unable to set the power on port <n> to
the desired level

### Message: 786

Unleveled, source 1 synthesizer.

Severity: Error

### Message: 787

Unleveled, source 2, out 1.

Severity: Error

### Message: 788

Unleveled, source 2, out 2.

Severity: Error

### Message: 789

Unleveled, source 2 synthesizer.

Severity: Error

### Message: 790

Unleveled, LO drive.

Severity: Error

### Message: 791

Unleveled, LO synthesizer.

Severity: Error

### Message: 792

Unlocked, source 1 synthesizer, integrator low.

Severity: Error

### Message: 793

Unlocked, source 1 synthesizer, integrator high.

Severity: Error

### Message: 795

Unlocked, source 2 synthesizer, integrator low.

Severity: Error

### Message: 796

Unlocked, source 2 synthesizer, integrator high.

Severity: Error

### Message: 798

Unlocked, LO synthesizer, integrator low.

Severity: Error

### Message: 799

Unlocked, LO synthesizer, integrator high.

Severity: Error

### Message: 801

Unleveled, doubler 1, prelevel.

Severity: Error

### Message: 802

Unleveled, doubler 2, prelevel.

Severity: Error

### Message: 803

Unleveled, doubler 3, prelevel.

Severity: Error

### Message: 804

Unleveled, doubler 4, prelevel.

Severity: Error

### Message: 805

Unleveled, source 1, P4.

Severity: Error

### Message: 806

Unleveled, source 2, P4.

Severity: Error

### Message: 848

"Phase lock lost"

Severity: Error

Further explanation: The instrument source was not able to lock properly. This
can be the result of broken hardware, poor calibration, or bad EEPROM values.

Suggestions: Perform source calibration. Click System / Service / Adjustments
/ Source Calibration

EventID: E8030350 (hex)

### Message: 849

Phaselock restored.

Severity: Success

EventID: 0x28030351 (hex)

### Message: 850

"Unknown hardware error."

Severity: Error

Further explanation: Hardware malfunctioned prevents communication with the
DSP.

EventID: E8030352 (hex)

### Message: 851

DSP communication lost.

Severity: Error

EventID: E8030353 (hex)

### Message: 852

RF power off.

Severity: Error

EventID: E8030354 (hex)

### Message: 853

RF power on.

Severity: Success

EventID: 28030355 (hex)

### Message: 854

Hardware OK.

Severity: Success

EventID: 28030356 (hex)

### Message: 855

"Source unleveled."

Severity: Error

Further explanation: The source was unable to properly level at the requested
power. The indicated power may not be accurate.

Suggestions: Try a different power level. Recalibrate source, if problem
persists.

EventID: E8030357 (hex)

### Message: 856

Source leveled.

Severity: Success

EventID: 28030358 (hex)

### Message: 857

Input overloaded.

Severity: Error

EventID: E8030359 (hex)

### Message: 858

Input no longer overloaded.

Severity: Success

EventID: 2803035A (hex)

### Message: 859

"Yig calibration failed."

Severity: Error

Further explanation: Internal self-calibration of YIG oscillator tuning
failed.

EventID: E803035B (hex)

### Message: 860

Yig calibrated.

Severity: Success

EventID: 2803035C (hex)

### Message: 861

"Analog ramp calibration failed."

Severity: Error

Further explanation: Internal analog sweep ramp calibration has failed.

EventID: E803035D (hex)

### Message: 862

Analog ramp calibrated.

Severity: Success

EventID: 2803035E (hex)

### Message: 864

Source temperature OK.

Severity: Success

EventID: 28030360 (hex)

### Message: 865

"EEPROM write failed."

Severity: Error

Further explanation: Attempt to store calibration data to EEPROM has failed.
There is a possible hardware failure.

EventID: E8030361 (hex)

### Message: 866

EEPROM write succeeded.

Severity: Success

EventID: 28030362 (hex)

### Message: 867

Attempted I/O write while port set to read only.

Severity: Error

Further explanation: Attempt to write to an I/O data port while the port set
to input/read only.

Suggestions: Set data port to write/output before attempting to write to port.

EventID: E8030363 (hex)

### Message: 868

" Attempted I/O read from write only port.

Severity: Error

Further explanation: Attempt to read from an I/O data port while the port set
to output/write only.

Suggestions: Set data port to read/input before attempting to read from port.

EventID: E8030364 (hex)

### Message: 869

Invalid hardware element identifier.

Severity: Error

EventID: E8030365 (hex)

### Message: 870

Invalid gain level setting.

Severity: Error

EventID: E8030366 (hex)

### Message: 871

Device driver was unable to allocate enough memory. Please try rebooting.

Severity: Error

EventID: E8030367 (hex)

### Message: 872

DSP Error. Please Contact Keysight Support. Technical Information: DSP Type 1

Severity: Error

EventID: E8030368 (hex)

### Message: 873

DSP Error. Please Contact Keysight Support. Technical Information: DSP Type 2

Severity: Error

EventID: E8030369 (hex)

### Message: 874

DSP Error. Please Contact Keysight Support. Technical Information: DSP Type 3

Severity: Error

EventID: E803036A (hex)

### Message: 875

DSP Error. Please Contact Keysight Support. Technical Information: DSP Type 4

Severity: Error

EventID: E803036B (hex)

### Message: 876

DSP Error. Please Contact Keysight Support. Technical Information: DSP Type 5

Severity: Error

EventID: E803036C (hex)

### Message: 910

The trigger connection argument was not recognized as valid by the firmware.

Severity: Error

EventID: 0xE803038E (hex)

### Message: 911

The trigger connection specified does not support this trigger behavior

Severity: Error

EventID: E803038F (hex)

### Message: 912

The trigger behavior specified was not recognized as valid by the firmware.

Severity: Error

EventID: E8030390 (hex)

### Message: 913

The trigger connection specified does not physically exist on this network
analyzer

Severity: Error

EventID: E8030391 (hex)

### Message: 914

Cannot set "Accept Trigger Before Armed", since this hardware configuration
does not support edge triggering.

Severity: Error

EventID: E8030392 (hex)

### Message: 915

Cannot set "Trigger Output Enabled", since this hardware configuration does
not support BNC2.

Severity: Error

EventID: E8030393 (hex)

### Message: 916

Exceeded maximum trigger delay.

Severity: Error

EventID: E8030394 (hex)

### Message: 917

Exceeded minimum trigger delay.

Severity: Error

EventID: E8030395 (hex)

* * *

### Measure Errors

* * *

### Message: 1024

If you are going to display or otherwise use a memory trace, you must first
store a data trace to memory.

Severity: Warning

EventID: A8040400 (hex)

### Message: 1025

"The measurement failed to shut down properly. The application is in a corrupt
state and should be shut down and restarted."

Severity: Error

Further explanation: This message is displayed if the analyzer application
becomes corrupt. If you continue to get this error, please call customer
service

EventID: E8040401 (hex)

### Message: 1026

The measurement failed to shut down properly. The update thread failed to exit
properly.

Severity: Warning

EventID: A8040402 (hex)

### Message: 1027

"Group Delay format with CW Time or Power sweeps produces invalid data."

Severity: Warning

Further explanation: Group Delay format is incompatible with single-frequency
sweeps. Invalid data is produced.

Suggestions: Ignore the data or choose a different format or sweep type.

EventID: A8040403 (hex)

### Message: 1028

Severity: Informational

"MSG_LIMIT_FAILED"

Further explanation: Limit line test failed.

EventID: 68040404 (hex)

### Message: 1029

Severity: Informational

"MSG_LIMIT_PASSED"

Further explanation: Limit line test passed.

EventID: 68040405 (hex)

### Message: 1030

"Exceeded the maximum number of measurements allowed."

Severity: Warning

Further explanation: See [Traces, Channels, and Windows on the
analyzer](../S0_Start/Traces_Channels_and_Windows.htm) for learn about maximum
measurements.

EventID: A8040406 (hex)

### Message: 1031

"Network Analyzer Internal Error. Unexpected error in AddNewMeasurement."

Severity: Warning

Further explanation: If you continue to get this message, contact product
support.

EventID: A8040407 (hex)

### Message: 1032

"No measurement was found to perform the selected operation. Operation not
completed."

Severity: Warning

Further explanation: None

Suggestions:Create a measurement before performing this operation.

EventID: A8040408 (hex)

### Message: 1033

The Markers All Off command failed.

Severity: Warning

EventID: A8040409 (hex)

### Message: 1034

"A memory trace has not been saved for the selected trace. Save a memory trace
before attempting trace math operations."

Severity: Warning

Further explanation: Must have a memory trace when trying to do Trace Math,

EventID: A804040A (hex)

### Message: 1035

"MSG_SET_AVERAGE_COMPLETE"

Severity: Informational

Further explanation: Informational for COM programming. Averaging factor has
been reached.

EventID: 6804040B (hex)

### Message: 1036

"MSG_CLEAR_AVERAGE_COMPLETE"

Further explanation: Informational for COM programming. Averaging factor has
NOT been reached.

EventID: 6804040C (hex)

### Message: 1037

"Time Domain transform requires at least 3 input points. The transform has
been deactivated."

Severity: Informational

Further explanation: None

Suggestions:Increase the number of points.

EventID: 6804040D (hex)

### Message: 1038

Smoothing requires a scalar format, and has been deactivated.

Severity: Informational

EventID: 6804040E (hex)

### Message: 1039

A receiver power calibration in this instrument state file cannot be recalled
into this firmware version.

Severity: Warning

EventID: A804040F (hex)

### Message: 1047

Could not achieve target power.

Severity: Error

Further explanation: This indicates that the analyzer was unable to find a
source power during the THRU step of the cal sufficiently high to boost the
measured noise power on port 2 to 6 dB above the noise floor.

### Message: 1056

ERROR: The given LO number is out of range. For a one stage mixer, this number
must be 1. For a two stage mixer, this number can be 1 or 2.

Severity: Error

Further explanation: None

### Message: 1063

"The trigger connection argument was not recognized as valid by the firmware."

Severity: Error

Further explanation: This indicates that the analyzer was unable to find a
source power during the THRU step of the cal sufficiently high to boost the
measured noise power on port 2 to 6 dB above the noise floor.

### Message: 1073

"Unexpected error"

Severity: Error

Further explanation: None

### Message: 1084

"User Preset was issued, but no user preset state had been set."

Severity: Error

Further explanation: None

### Message: 1100

"Exceeded limit on number of measurements."

Severity: Error

Further explanation: See [Traces, Channels, and Windows on the
analyzer](../S0_Start/Traces_Channels_and_Windows.htm) for measurement limits.

EventID: E8040450 (hex)

### Message: 1104

"Exceeded limit on number of measurements."

Severity: Error

Further explanation: See [Traces, Channels, and Windows on the
analyzer](../S0_Start/Traces_Channels_and_Windows.htm) for measurement limits.

EventID: E8040450 (hex)

### Message: 1105

"Parameter not valid."

Severity: Error

Further explanation: A measurement parameter that was entered programmatically
is not valid.

EventID: E8040451 (hex)

### Message: 1106

"Measurement not found."

Severity: Error

Further explanation: Any of these could be the cause:

Trying to calibrate but already have maximum measurements.

Trying to do a confidence check but there is not a measurement.

Trying to create, activate, or alter a measurement through COM that has been
deleted through the front panel.

Trying to use a trace name through programming that is not unique.

EventID: E8040452 (hex)

### Message: 1107

"No valid memory trace."

Severity: Error

Further explanation: Must have a memory trace when trying to do Trace Math,

Suggestions: Store a memory trace.

EventID: E8040453 (hex)

### Message: 1108

"The reference marker was not found."

Severity: Error

Further explanation: Attempted to create a delta marker without first creating
a reference marker (COM only).

EventID: E8040454 (hex)

### Message: 1109

"Data and Memory traces are no longer compatible. Trace Math has been turned
off."

Severity: Error

Further explanation: Warning \- channel setting has changed while doing trace
math.

Suggestions:Store another memory trace and turn trace math back on.

EventID: A8040455 (hex)

### Message: 1110

"Data and Memory traces are not compatible. For valid trace math operations,
memory and data traces must have similar measurement conditions."

Severity: Error

Further explanation: Tried to do trace math without compatible data and memory
traces.

Suggestions: Store another memory trace.

EventID: E8040456 (hex)

### Message: 1111

"Marker Bandwidth not found."

Severity: Error

Further explanation: Could not find a portion of trace that meets the
specified bandwidth criteria.

EventID: E8040457 (hex)

### Message: 1112

"The peak was not found."

Severity: Error

Further explanation: Could not find portion of trace that meets peak criteria.

Suggestions: See Marker Peak criteria.

EventID: E8040458 (hex)

### Message: 1113

"The target search value was not found."

Severity: Error

Further explanation: Could not find interpolated data point that meets search
value.

EventID: E8040459 (hex)

### Message: 1114

"Reflection measurement, such as S11, must supply an auxiliary port to
disambiguate 2-port measurements on multiport instruments."

Severity: Error

Further explanation:

EventID: E804045A (hex)

### Message: 1115

"The receiver power calibration has been turned off because the type of
measurement or source port has changed, so the calibration is no longer
valid."

Severity: Warning

Further explanation:

EventID: A804045B (hex)

### Message: 1116

"Receiver power cal requires the active measurement to be of unratioed power."

Severity: Warning

Further explanation:

EventID: A804045C (hex)

### Message: 1117

"There is currently no source power calibration associated with the channel
and source port of the active measurement. A source power cal should be
performed or recalled before performing a receiver power calibration."

Severity: Warning

Further explanation:

EventID: A804045D (hex)

### Message: 1118

"The attempted operation can only be performed on a standard measurement
type."

Severity: Error

Further explanation:

EventID: E804045E (hex)

### Message: 1119

"The custom measurement cannot be loaded because it is not compatible with the
Network Analyzer hardware."

Severity: Error

Further explanation:

Suggestions:

EventID: E804045F (hex)

### Message: 1120

"The custom measurement cannot be loaded because it is not compatible with the
Network Analyzer software."

Severity: Error

Further explanation:

EventID: E8040460 (hex)

### Message: 1121

"The custom measurement load operation failed for an unspecified reason."

Severity: Error

Further explanation:

EventID: E8040461 (hex)

### Message: 1122

"The custom measurement data processing has generated an unhandled exception,
and will be terminated. The analyzer software may be in an unstable state and
it is recommended that the analyzer software be shutdown and restarted."

Severity: Error

Further explanation:

EventID: E8040462 (hex)

### Message: 1123

"The attempted operation can only be performed on a custom measurement type."

Severity: Error

Further explanation:

EventID: E8040463 (hex)

### Message: 1124

"The requested custom measurement is not available."

Severity: Error

Further explanation:

EventID: E8040464 (hex)

### Message: 1125

"The requested custom algorithm was not found."

Severity: Error

Further explanation:

EventID: E8040465 (hex)

### Message: 1126

"Normalization cannot be turned on because the measurement does not have a
valid divisor buffer."

Severity: Error

Further explanation:

### Message: 1127

"The Raw Data requested by the measurement could not be provided."

Severity: Warning

Further explanation:

EventID: A8040467 (hex)

### Message: 1128

"The selected Sweep Type does not allow Transform and Gating. Transform and
Gating disabled."

Severity: Error

Further explanation:

EventID: E8040468 (hex)

### Message: 1129

"ERROR: There was not enough disk space to create the FIFO data file."

Severity: Error

### Message: 1130

"ERROR: This feature is not available on this model of hardware."

Severity: Error

### Message: 1131

"The data provided has an invalid number of points. It could not be stored."

Severity: Error

EventID: E804046B (hex)

### Message: 1132

"The measurement stored in the save/recall state has an invalid version. It
could not be loaded."

Severity: Error

EventID: E804046C (hex)

### Message: 1133

"This data format argument for this operation must be "naDataFormat_Polar"

Severity: Error

EventID: E804046D (hex)

### Message: 1134

This data format argument for this operation must be a scalar data format

Severity: Error

EventID: E804046E (hex)

### Message: 1135

The memory trace is not valid for the current measurement setup.

Severity: Error

EventID: E804046F (hex)

### Message: 1136

This measurement is incompatible with existing measurements in this channel.
Choose another channel.

Severity: Error

EventID: E8040470 (hex)

### Message: 1137

Port extension correction is not available for offset frequency measurements.
Port extension correction has been disabled.

Severity: Error

EventID: E8040471 (hex)

### Message: 1138

Physical port number assignments for logical port mappings must be unique.

Severity: Error

EventID: E8040472 (hex)

### Message: 1140

"Power saturation back-off value was not found"

Severity: Error

Further explanation: None

Suggestions: None

### Message: 1141

"Power normal operating point was not found"

Severity: Error

Further explanation: None

Suggestions: None

### Message: 1147

"Specified external device was not found."

Severity: Error

Further explanation: None

Suggestions: None

### Message: 1179

"Commas are not allowed."

Severity: Error

Further explanation: None

Suggestions: None

* * *

### Parser Errors

* * *

Message: 1281

"You have sent a read command to the analyzer without first requesting data
with an appropriate output command. The analyzer has no data in the output
queue to satisfy the request."

Severity: Error

EventID: 68050501 (hex)

### Message: 1282

"You must remove the active controller from the bus or the controller must
relinquish the bus before the analyzer can assume the system controller mode."

Severity: Error

EventID: E8050502(hex)

### Message: 1283

"The analyzer did not receive a complete data transmission. This is usually
caused by an interruption of the bus transaction."

Severity: Error

EventID: E8050503 (hex)

### Message: 1284

"The instrument status byte has changed."

Severity: Informational

EventID: 68050504 (hex)

### Message: 1285

"The SCPI command received has caused error number %1: "%2"."

Severity: Informational

EventID: 68050505 (hex)

### Message: 1286

"The INET LAN server has been started as process number %1."

Severity: Informational

EventID: 68050506 (hex)

### Message: 1360

"Execution of the SCPI command has failed"

Severity: Error

EventID: E8050550 (hex)

### Message: 1361

" The INET/LAN device is not accessible."

Severity: Error

EventID: E8050551 (hex)

### Message: 1362

"The INET/LAN driver was not found. "

Severity: Error

EventID: E8050552 (hex)

### Message: 1363

"The INET/LAN driver was not found."

Severity: Error

EventID: E8050553 (hex)

### Message: 1364

"The INET/LAN device is unable to acquire the necessary resources. "

Severity: Error

EventID: E8050554 (hex)

### Message: 1365

"The INET/LAN device generated a generic system error. "

Severity: Error

EventID: E8050555 (hex)

### Message: 1366

"Invalid address for the INET/LAN device."

Severity: Error

EventID: E8050556 (hex)

### Message: 1367

"The INET I/O library was not found. "

Severity: Error

EventID: E8050557 (hex)

### Message: 1368

"An error occured in the INET system. "

Severity: Error

EventID: E8050558 (hex)

### Message: 1369

"Access to the INET/LAN driver was denied. "

Severity: Error

EventID: E8050559 (hex)

### Message: 1370

"Could not load error system message dll."

Severity: Error

EventID: E805055A (hex)

### Message: 1371

"ErrorSystemMessage.dll does not export the right function."

Severity: Error

EventID: E805055B (hex)

### Message: 1372

"Custom scpi library was not able to be knitted"

Severity: Error

EventID: E805055C (hex)

### Message: 1373

"Could not knit the scpi error messages from the ErrorSystemMessage lib"

Severity: Error

EventID: E805055D (hex)

### Message: 1374

Command is obsolete with this software version.

Severity: Error

EventID: E808055E (hex)

### Message: 1375

CALC measurement selection set to none. Use [Calc:Par:Sel](../Programming/GP-
IB_Command_Finder/Calculate/Parameter.htm#cps)

Severity: Error

EventID: E808055F (hex)

### Message: 1535

"Parser got command: %1."

Severity: Informational

EventID: 680505FF (hex)

* * *

### Display Errors 1536 - 1621

* * *

Message: 1536

"Exceeded the maximum number of traces in each window. The trace for <x> will
not be added to window <x>."

Severity: Warning

Further explanation: None

Suggestions: Create the trace in another window. See the [analyzer window
limits](../S0_Start/Traces_Channels_and_Windows.htm).

EventID: A8060600 (hex)

### Message: 1537

"Exceeded the maximum of 16 data windows. New window will not be created."

Severity: Warning

Further explanation: None

Suggestions: Create the trace in an existing window. See the [analyzer window
limits](../S0_Start/Traces_Channels_and_Windows.htm).

EventID: A8060601 (hex)

### Message: 1538

"No Data Windows are present. Unable to complete operation."

Severity: Warning

Further explanation: Your remote SCPI operation tried to create a new
measurement while there were no windows present

Suggestions: Create a new window before creating the measurement. See example
Create a measurement using SCPI

EventID: A8060602 (hex)

### Message: 1539

"No data traces are present in the selected window. Operation not completed."

Severity: Warning

Further explanation: None

EventID: A8060603 (hex)

### Message: 1540

"Cannot complete request to arrange existing measurements in <x> windows due
to the limit of <x> traces per window."

Severity: Informational

Further explanation: The arrange window feature cannot put the existing traces
into the number of windows you requested because the maximum number of traces
per window has been exceeded. [See Arranging Existing
Measurements](../S0_Start/Traces_Channels_and_Windows.htm#Window_Layout)

Suggestions:Either create more windows or delete some traces.

EventID: 68060604 (hex)

### Message: 1541

"Unable to establish a connection with the specified printer."

Severity: Warning

Further explanation: None

Suggestions: Refer to Printer Help

EventID: A8060605 (hex)

### Message: 1542

"Printout canceled."

Severity: Informational

EventID: 68060606 (hex)

### Message: 1616

"Window not found."

Severity: Error

Further explanation: A window was specified in your program which does not
exist.

Suggestions: Query the name of your window before specifying.

EventID: E8060650 (hex)

### Message: 1617

"Duplicate window ID specified."

Severity: Error

Further explanation: None

EventID: E8060651 (hex)

### Message: 1618

"Exceeded limit on number of windows."

Severity: Error

Further explanation: There is a limit of 4 windows per screen.

EventID: E8060652 (hex)

### Message: 1619

"Exceeded limit on number of traces/window."

Severity: Error

Further explanation: There is a limit of traces per window. See the [Traces,
Channels, and Windows on the
analyzer](../S0_Start/Traces_Channels_and_Windows.htm).

Suggestions: Create the trace in another window

EventID: E8060653 (hex)

### Message: 1620

"Trace not found."

Severity: Error

Further explanation: Your program tried to communicate with a non-existing
trace.

Suggestions:Query the trace ID before writing to it.

EventID: E8060654 (hex)

### Message: 1621

"The operating system does not recognize this printer."

Severity: Warning

EventID: A8060655 (hex)

### Message: 1622

Duplicate trace ID specified.

Severity: Error

EventID: E8060656 (hex)

* * *

### Channel Errors 1792 -1878

* * *

Message: 1792

"Sweep Complete."

Severity: Informational

Further explanation: None

Suggestions:None

EventID: 68070700 (hex)

### Message: 1793

"All triggerable acquisitions have completed."

Severity: Informational

Further explanation:

EventID: 68070701 (hex)

### Message: 1794

"The last trigger produced an aborted sweep."

Severity: Informational

Further explanation:

EventID: 68070702 (hex)

### Message: 1795

"The segment list must be adjusted to have at least one active segment with
more than 0 points to use segment sweep."

Severity: Informational

Further explanation: You attempted to change Sweep type to Segment sweep, but
there is either no segments defined or no sweep points in the defined segments

Suggestions: Define at least one segment with at least one measurement point.
See Segment sweep for more information

EventID: 68070703 (hex)

### Message: 1796

"MSG_SET_CHANNEL_DIRTY"

Severity: Informational

Further explanation: This informational message occurs when a channel setting
has changed but the channel still has data that was taken with the previous
setting. The following CLEAR message occurs when new channel data is taken.

EventID: 68070704 (hex)

### Message: 1797

"MSG_CLEAR_CHANNEL_DIRTY"

Severity: Informational

Further explanation: The previous SET message occurs when a channel setting
has changed but the channel still has data that was taken with the previous
setting. This CLEAR message occurs when new channel data is taken.

EventID: 68070705 (hex)

### Message: 1798

Sweep time has changed from Auto to Manual mode. If desired to return to Auto
mode, enter sweep time value of 0.

Severity: Informational

EventID: 68070706 (hex)

### Message: 1799

"Set Sweep Completed"

Severity: Informational

Further explanation: This event occurs when a sweep and it's associated sweep
calculations finish. This is typically when all sweeps on a channel complete.

EventID: 68070707 (hex)

### Message: 1800

"Clear Sweep Completed"

Severity: Informational

Further explanation: This event occurs immediately after the SET SWEEP
COMPLETED event. These two events set and clear the "Sweep Completed" bit (bit
4) on the SCPI Device Status register.

EventID: 68070708 (hex)

### Message: 1801

"All Sweeps Completed and Processed"

Severity: Informational

Further explanation: This event occurs when all of the sweeps and sweep
calculations are complete for a channel.

EventID: 68070709 (hex)

### Message: 1802

Low Pass : Frequency limits have been changed.

Severity: Informational

EventID: 6807070A (hex)

### Message: 1803

Low Pass : Number of points have been changed.

Severity: Informational

EventID: 6807070B (hex)

### Message: 1804

Low Pass : Frequency limits and number of points have been changed.

Severity: Informational

EventID: 6807070C (hex)

### Message: 1805

"Channel created"

Severity: Informational

EventID: 6807070D (hex)

### Message: 1806

"Channel deleted"

Severity: Informational

EventID: 6807070E (hex)

### Message: 1872

"Channel not found."

Severity: Error

Further explanation: A non-existent channel is being referenced under program
control.

Suggestions: Query the channel number, then refer to it by number.

EventID: E8070750 (hex)

### Message: 1873

"The requested sweep segment was not found."

Severity: Error

Further explanation: A non-existent sweep segment is being referenced under
program control.

EventID: E8070751 (hex)

### Message: 1874

"The sweep segment list is empty."

Severity: Error

Further explanation: Segment Sweep cannot be specified unless there is at
least one defined segment. This error will only occur under remote control.

EventID: E8070752 (hex)

### Message: 1875

"The number of points in active sweep segment list segments is 0."

Severity: Error

Further explanation: Segment Sweep cannot be specified unless there is at
least data point specified in a segment. This error will only occur under
remote control.

EventID: E8070753 (hex)

### Message: 1876

"The specified source attenuator is not valid."

Severity: Error

Further explanation: You tried to set the Attenuator property on the Channel
object on a analyzer that doesn't have a source attenuator.

EventID: E8070754 (hex)

### Message: 1877

"Log Frequency sweep cannot be selected with the current Number of Points.
Please reduce Number of Points."

Severity: Error

Further explanation: The maximum number of points that can be used for Log
sweep is 401.

EventID: E8070755 (hex)

### Message: 1878

"The requested Number of Points is greater than can be selected for Log
Frequency sweep."

Severity: Error

Further explanation: The maximum number of points that can be used for Log
sweep is 401.

EventID: E8070756 (hex)

### Message: 1879

"Response frequencies exceeded instrument range so Frequency Offset has been
turned off."

Severity: Error

Further explanation: This error is returned whenever the instrument detects
that the stimulus sweep setup and Frequency Offset settings result in computed
response frequencies that exceed instrument limits. When this occurs, the
instrument automatically turns off Frequency Offset to avoid the out-of-range
conditions.

Suggestions: When this condition has occurred, change settings for either the
stimulus frequencies or Frequency Offset so that the Response frequencies are
within instrument bounds. Once this is done, Frequency Offset can once again
be turned on.

EventID: E8070757 (hex)

### Message: 1880

The total number of points for all the given segments exceeds the maximum
number of points supported. The segments were not changed.

Severity: Error

EventID: E8070758 (hex)

### Message: 1881

This instance of the Channels object was not used to place the channels in
Hold, so no channels were resumed.

Severity: Error

EventID: E8070759 (hex)

### Message: 1882

The port number was outside the range of allowed port numbers.

Severity: Error

EventID: E807075A (hex)

### Message: 1883

More ports than are present are required for this operation.

Severity: Error

EventID: E807075B (hex)

* * *

### General Errors

* * *

### Message: 2009

"Channel is not a mixer channel."

Severity: Error

Further explanation: None

Suggestions: None

### Message: 2010

"The external testset type is invalid."

Severity: Error

Further explanation: None

Suggestions: None

### Message: 2011

"No ports were specified"

Severity: Error

Further explanation: None

Suggestions: None

### Message: 2012

"Cannot couple primary domain range."

Severity: Error

Further explanation: None

Suggestions: None

### Message: 2015

"The copy channel operation failed because the target channel exists and is
incompatible with the source channel."

Severity: Error

Further explanation: None

Suggestions: None

### Message: 2019

"Invalid sweep number."

Severity: Error

Further explanation: None

Suggestions: None

### Message: 2020

"IMD channel tracking not enabled."

Severity: Error

Further explanation: None

Suggestions: None

### Message: 2022

"Compression analysis not enabled due to invalid parameter(s)"

Severity: Error

Further explanation: None

Suggestions: None

### Message: 2023

"External receiver configuration not available."

Severity: Error

Further explanation: None

Suggestions: None

### Message: 2025

"Error term data not found."

Severity: Error

Further explanation: None

Suggestions: None

### Message: 2028

"The PNA platform does not support ON mode for virtual bridge. The only
supported modes are AUTO and OFF."

Severity: Error

Further explanation: None

Suggestions: None

### Message: 2048

"The function you requested requires a capability provided by an option to the
standard analyzer. That option is not currently installed."

Severity: Error

Further explanation: None

Suggestions:To view the options on your analyzer, click Help / About Network
Analyzer. For more information see [analyzer Options](Configurations.md)

EventID: 68080800 (hex)

### Message: 2049

"The feature you requested is not available on the current instrument."

Severity: Error

Further explanation: None

EventID: 68080801 (hex)

### Message: 2050

"The feature you requested is incompatible with the current instrument state."

Severity: Error

Further explanation: None

Suggestions: None

EventID: 68080802 (hex)

### Message: 2051

"File<x> has been saved."

Severity: Informational

Further explanation: None

EventID: 68080803 (hex)

### Message: 2052

"Attempt to save <x> failed."

Severity: Error

Further explanation: None

Suggestions: If using a floppy disk, ensure it is inside the drive and the
disk is not full. Check the filename for special characters.

EventID: E8080804 (hex)

### Message: 2053

"Attempt to recall file failed because <x> was not found."

Severity: Error

Further explanation: None

EventID: E8080805 (hex)

### Message: 2054

"<x> has a bad header."

Severity: Error

Further explanation: None

Suggestions: Recopy the file and / or delete the file.

EventID: E8080806 (hex)

### Message: 2056

"Request to enter hibernate state."

Further explanation: None

EventID: 68080808 (hex)

### Message: 2057

"Power up from automatic hibernate state. Program received
PBT_APMRESUMEAUTOMATIC Message."

Further explanation: None

EventID: 68080809 (hex)

### Message: 2058

"Power up from suspend hibernate state. Program received PBT_APMRESUMESUSPEND
Message."

Further explanation: None

EventID: 6808080A (hex)

### Message: 2059

"Power up from suspend hibernate state. Program received PBT_APMRESUMECRITICAL
Message."

Severity: Warning

Further explanation: None

EventID: A808080B (hex)

### Message: 2060

"Power up from unknown hibernate state UI recovery called. Program received no
PBT_Message within the time allotted and is attempting recovery."

Severity: Warning

Further explanation: None

EventID: A808080C (hex)

### Message: 2061

"<x> already exists. File is being overwritten."

Further explanation: Used only for remote applications

EventID: 6808080D (hex)

### Message: 2062

"File has not been saved."

Severity: Error

Further explanation: Used only for remote applications

EventID: E808080E (hex)

### Message: 2063

"File <x> has been recalled."

Further explanation: Used only for remote applications

EventID: 6808080F (hex)

### Message: 2064

"State version in <x> is considered obsolete by this version of this code."

Severity: Error

Further explanation: You attempted to recall a file that is no longer valid.

Suggestions: You must recreate the file manually.

EventID: E8080810 (hex)

### Message: 2065

"State version in <x> is newer than the latest version supported by this
code."

Severity: Error

Further explanation: You attempted to recall a file that was created by a
later version of the analyzer application.

Suggestions: You must recreate the file manually.

EventID: E8080811 (hex)

### Message: 2066

"Error occurred while reading file <x>"

Severity: Error

Further explanation: The file may be corrupt.

Suggestions: Try to recreate the file.

EventID: E8080812 (hex)

### Message: 2067

"Windows shell error: <x>"

Severity: Error

Further explanation: None

EventID: E8080813 (hex)

### Message: 2068

Send message timed out returning: <x>.

Severity: Error

Further explanation: None

EventID: E8080814 (hex)

### Message: 2069

"Changing GPIB mode to System Controller."

Severity: Informational

Further explanation: None

EventID: 68080815 (hex)

### Message: 2070

"Changing GPIB mode to Talker Listener."

Severity: Informational

Further explanation: None

EventID: 68080816 (hex)

### Message: 2071

"The Network Analyzer can not be put in GPIB System Controller mode until the
GPIB status is Local. Stop any remote GPIB programs which may be using the
Network analyzer, press the Macro/Local key and try again. "

Severity: Informational

Further explanation: See [LCL and RMT
Operation](../Programming/Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm#LCL)

Suggestions: Press the Macro/Local key and try again.

EventID: 68080817 (hex)

### Message: 2120

"This method can not be invoked through a late-bound COM call."

Severity: Error

Further explanation: None

Suggestions: Use the alternate method described in the [COM programming
documentation](../Programming/COM_Reference/Objects/The_Analyzer_Object_Model.htm)

EventID: E8080878 (hex)

### Message: 2128

"The specified format is invalid."

Severity:Error

Further explanation: None

EventID: E8080850 (hex)

### Message: 2129

"WINNT exception caught by Automation layer."

Severity: Error

Further explanation: None

EventID: E8080851 (hex)

### Message: 2130

"Bad port specification."

Severity: Error

Further explanation: None

EventID: E8080852 (hex)

### Message: 2131

"Failed to find a printer."

Severity: Error

Further explanation: None

Suggestions: See [Connecting to a Printer](../S5_Output/Print.htm#Connecting
to a printer)

EventID: E8080853 (hex)

### Message: 2132

"Manual trigger ignored."

Severity: Error

Further explanation: None

EventID: E8080854 (hex)

### Message: 2133

"Attempt to set trigger failed."

Severity: Error

Further explanation: None

EventID: E8080855 (hex)

### Message: 2134

"Macro execution failed."

Severity: Error

Further explanation: None

EventID: E8080856 (hex)

### Message: 2135

"Specified macro definition is incomplete."

Severity: Error

Further explanation:

EventID: E8080857 (hex)

### Message: 2137

"Block data length error."

Severity: Error

Further explanation: See [Getting Data from the
Analyzer](../Programming/Learning_about_GPIB/Getting_Data_from_the_Analyzer.htm)

EventID: E8080859 (hex)

### Message: 2139

"Requested data not found."

Severity: Error

Further explanation: None

EventID: E808085B (hex)

### Message: 2142

"The parameter supplied was out of range, so was limited to a value in range
before being applied to the instrument."

Severity: Success

Further explanation: None

Suggestions: View range limits before sending programming commands.

EventID: 2808085E (hex)

### Message: 2143

The parameter supplied was out of range, so was limited to a value in range
before being applied to the instrument.

Severity: Error

EventID: E808085F (hex)

### Message: 2144

"Request failed. The required license was not found."

Severity: Error

Further explanation: None

EventID: E8080860 (hex)

### Message: 2145

"A remote call to the front panel has returned hresult <x>"

Severity: Error

Further explanation: This may indicate a problem with the front panel

Suggestions: Contact Technical support

EventID: E8080861 (hex)

### Message: 2146

The recall operation failed.

Severity: Error

Further explanation:

EventID: E8080862 (hex)

### Message: 2147

Attempt to save file failed.

Severity: Error

Further explanation:

EventID: E8080863 (hex)

### Message: 2148

Recall attempt failed because file was not found.

Severity: Error

Further explanation:

EventID: E8080864 (hex)

### Message: 2149

Recall file has a bad header.

Severity: Error

Further explanation:

EventID: E8080865 (hex)

### Message: 2150

Recall file version is obsolete and no longer compatible with this instrument.

Severity: Error

Further explanation:

EventID: E8080866 (hex)

### Message: 2151

The recall file contains an istate version newer than this instrument. A
remote call to the front panel has returned hresult %1

Severity: Error

Further explanation:

EventID: E8080867 (hex)

### Message 2152

"Front Panel <x>

Severity: Error

Further explanation: None

EventID: E8080868 (hex)

### Message 2153

"Front Panel message"

Severity: Informational

Further explanation: None

EventID: 68080869 (hex)

### Message 2154

"Power Service <x>

Severity: Error

Further explanation: There is more than 1 instance of powerservice running.
There should only be one running. This might happen after running install
shield - especially when upgrading the CPU board.

Suggestions: Try rebooting. If this persists, please call [Customer
Support](Tech_Supp.htm).

EventID: E808086A (hex)

### Message 2155

"Power Service <x>

Severity: Informational

Further explanation: None

EventID: 6808086B (hex)

### Message 2156

"The Keysight Technologies GPIB driver can not be loaded or unloaded."

Severity: Error

Further explanation: None

Suggestions: If the problem persists, from the analyzer desktop, right-click
on My Computer. Click Properties, Click Hardware Tab. Click Device Manager
Button. Expand GPIB Devices. Right-click and click Uninstall all GPIB
interfaces devices. Reboot the analyzer.

EventID: E808086C (hex)

### Message 2157

"The National Instruments GPIB driver can not be loaded or unloaded."

Severity: Error

Further explanation: None

Suggestions: If the problem persists, from the analyzer desktop, right-click
on My Computer. Click Properties, Click Hardware Tab. Click Device Manager
Button. Expand GPIB Devices. Right-click and click Uninstall all GPIB
interfaces devices. Reboot the analyzer.

EventID: E808086D (hex)

### Message 2158

"The Keysight GPIB driver is loaded but it can not start its parser."

Severity: Error

Further explanation: None

EventID: E808086E (hex)

### Message: 2159

The front panel is in remote mode.

Severity: Warning

EventID: A808086F (hex)

### Message: 2160

The Registry Key specified could not be found.

Severity: Error

EventID: E8080870 (hex)

### Message: 2161

An overcurrent condition has been detected on a probe plugged into the front
panel.

Severity: Warning

EventID: A8080871 (hex)

### Message: 2162

The operation timed out.

Severity: Error

EventID: E8080872 (hex)

### Message 2163

"The Network Analyzer executed a preset."

Severity:Informational

Further explanation: None

EventID: 68080873 (hex)

### Message 2164

"Access to file denied."

Severity: Error

Further explanation: This means that the system can not open an output file
for writing. Most likely because the file is write protected.

Suggestions: Pick another file name or file directory, check floppy disk hard
disk write access.

EventID: E8080874 (hex)

### Message 2165

"File type is structured storage."

Severity: Informational

Further explanation: None

EventID: 68080875 (hex)

### Message 2166

"The trigger operation failed."

Severity: Error

Further explanation: None

EventID: E8080876 (hex)

### Message 2167

"Argument out of range error."

Severity: Error

Further explanation: None

Suggestions: None

EventID: E8080877 (hex)

### Message: 2169

The given COM object is not a custom application

Severity: Error

EventID: E8080879 (hex)

### Message: 2170

The eventID supplied was not recognized as a valid analyzer eventID

Severity: Error

EventID: E808087A (hex)

### Message: 2171

The operation was canceled.

Severity: Error

EventID: E808087B (hex)

### Message: 2172

High security level cannot be disabled directly. Only an instrument preset or
recall of lower security instrument state will reset this security level.

Severity: Error

EventID: E808087C (hex)

### Message: 2173

Local lockout mode is on. The analyzer application will not accept input from
front panel, keyboard or mouse until this mode is turned off from a remote
interface.

Severity: Error

EventID: E808087D (hex)

### Message: 2174

The SnP request is not valid for the selected measurement.

Severity: Error

EventID: E808087E (hex)

### Message: 2175

Preset is not supported while this dialog or wizard is open. Close the dialog
or wizard and then try again.

Severity: Error

EventID: E808087F (hex)

### Message: 2176

The function you requested requires a capability provided by an option to the
standard analyzer. That option is not currently installed.

Severity: Error

EventID: E8080880 (hex)

### Message: 2177

Catastrophic error. Crash dump recorded at <n>

Severity: Error

EventID: E8080881 (hex)

### Message: 2178

In the context of a noise calibration, this would occur if the analyzer was
unable to set the state of the tuner Ecal module.

Severity: Error

EventID: E8080882 (hex)

### Message: 2179

Failed to open gen.lic.

Severity: Error

EventID: E8080883 (hex)

### Message: 3002

Bad port specification.

Severity: Error

* * *


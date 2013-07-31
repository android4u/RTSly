RTSly
=====

##What ?

`RTSly` is a script that enables a user to track Indian Railways' Train Running Status in real time and update them if there is any change in train's status (For example, when a train's status changes from `UPCOMING STATION - TUNDLA JN  ETA - 04:55 PM   DELAY - 5 mins` to `UPCOMING STATION - KANPUR CENTRAL  ETA - 07:55 PM   DELAY - on time`). This means it can give real time status of a train.

##Requisites ?
This script requires you to have an account on [FullOnSms.com](http://fullonsms.com). Your system also needs to have [Python 2.7](http://www.python.org/download/releases/2.7.5/) downloaded and installed (If you don't have it already).

##Working
To run the software,

* On `LINUX`

      * First `download` this script from the repository (Git Clone/Download ZIP)
      * Open `rtsly.py` with any editor to Uncomment lines 20 and 84 and Comment lines 21 and 85
      * Save `rtsly.py`
      * `cd` to the extracted files directory
      * `run` the following command in the terminal
      
      ```
      $ python ./rtsly.py
      ```
* On `WINDOWS`

      * First `download` this script from the repository (Git Clone/Download ZIP)
      * Run by double clicking `rtsly.py`

##Customization
The script checks the Train status every 10 minutes (600 seconds). To change it, you can change the update frequency by editing the second last line of `rtsly.py` script.

```
  time.sleep(600) #Wait 600seconds (10mins)
``` 

##License & Credits

    Copyright (C) 2013  Naive Algorist (naivealgorist@gmail.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    For a copy of GNU General Public License see http://www.gnu.org/licenses/

This script uses Indian Railways Trains and Stations Information Service  & `sendsms` script by [siddhant3s](https://github.com/siddhant3s/sendsms)

##DISCLAIMER
The author of this script is in no way associated with [Indian Railways Trainenquiry](http://www.trainenquiry.com/) or [FullOnSms](http://fullonsms.com). The service, which the script provides, is for personal or educational use only. Any commercial use of the service is forbidden. In this context, `the service` is defined as the output of the given script as-is or a derived script in conjunctuion with third party _un-authorized_ HTTP(S) requests to `TrainEnquiry` or `FullOnSms` or any other service provider(s). Author takes no responsibility whatsoever if this script is misused in any way. Author is not responsible for any losses incurrred to any individual, company or property either directly or indirectly as a result of using this script. Also, there is no warranty of any kind with this script.

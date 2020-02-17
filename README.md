## Description:

This app is the open-source version of GeocadTek Atlas. 

Atlas is a map viewer based on OpenLayers with Javascript coding. The administration part is programmed using the Flask-admin and SQLite3 database. 

By default, the map extend shows the Netherlands. You can edit the map.js file to update the map-extend for your preference. You can find the map.js file in static/js directory. 


## Features:
- Map viewer ready for Mobile devices (Mobile design and responsive).
- Allows defining superuser and administrator accounts for maintaining users and map layers.
- Users with an authentication key can access hidden layers on the map server, such as GeoServer.
- Supports reverse proxy configuration on Apache and Nginx.
- Supports many geo-data sources from Dutch kadaster and public agencies.
- Tested with Google Chrome, Firefox, and Microsoft IE browsers (under Citrix).


## Download:

git clone https://github.com/geocadtek/atlas-starter



## Configuration:

There are two sample files for configuration. cloud_config.py is for the server (cloud) server, and local_config.py is for the local machine installation. 

You can switch between development mode and production mode by changing the app-mode variable in the Makefile. The app mode is set to DevelopmentConfig by default.

The development version runs on the port number 5700, while the application version runs on the port number 5500. You can change the port numbers in the config file, for example, local_config.py.

How to run:

If you want to set up and run the app for the first time, a quick and straightforward way is to type the following command on the command line:

$ `make all`

This command will install python requirements and run the app. Check atlas.log file for the app messages.

You can access the app through http://localhost:5700/atlas-starter in your browser.

or if you want to go step by step:

$ `make install`

$ `make db-init`

$ `make db-migrate`

$ `make db-insert`

$ `make run`

if anytime, you wish to start over:

$ `make clean`

$ `make all`

After the installation if you get the latest changes from your git repo, we suggest to use:

$ `make deploy`

Note that you may need to update Makefile to reflect your git repo settings.

Checking run status of the app:

$ `make status`

Stopping the app:

$ `make stop`

Help on the command-line options:

$ `make`    (to see a list of command options).


### How to access Atlas and administrator pages from your browser:

 atlas-starter map viewer: https://localhost:5700/atlas-starter
 atlas-starter admin: https://localhost:5700/atlas-starter/admin

The online version is accessible at https://mijndatalab.nl/atlas-starter

### Database files for SQLite:

sqlite_layers_table.py contains sample layer definitions for the Netherlands, and this file can be edit manually or from the app web interface.

sqlite_users_table.py contains sample user definitions; this file can be edit manually or from the app web interface.


### For developers,  you can access JSON dumps of layers and hidden layers  in the following links:

normal layers: http://localhost:5700/atlas-starter/layers
hidden layers: http://localhost:5700/atlas-starter/layerc


### 
###
### Versions

Atlas pro: https://mijndatalab.nl/atlas/

Atlas starter: https://mijndatalab.nl/atlas-starter/

Atlas basic: https://github.com/geocadtek/Atlas-Basic


### License

GNU General Public License

### Credits

*Mijndatalab.nl development Team*

Geocadtek 2020
###


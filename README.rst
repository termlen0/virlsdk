=======
virlsdk
=======


A python SDK wrapper for Cisco's VIRL API.

Description
===========

This SDK wraps the following API functions:
   1. Get the current simulations
   2. Launch a simulation
   3. Stop a simulation
   4. Get the status of a simulation

Please see: http://virl-dev-innovate.cisco.com/api.docs.php, for details about
the APIs themselves

HOWTO
=====
1. ```pip install virlsdk``` - This will add the sdk to your system
2. ``` git clone https://github.com/termlen0/virlsdk.git ``` - This will get the
   sample code to use the sdk
3. Update config.yaml with details of your VIRL install
   (A sample .virl file is provided for a basic hub/spoke topology)
4. ```python launch_sim.py -f config.yaml``` - This should launch the sim
   The output will have the launched session info
5. ```python stop_sim -f config.yaml -s <sim_name>``` - will stop the session

Note
====
Please see the docs dir.

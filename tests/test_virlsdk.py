#!/usr/bin/env python3

import pytest
import virlsdk.virlsdk as vsdk
#GLOBALS
VIRL = "http://10.152.123.31:19399/"
USERNAME = "guest"
PASSWORD = "guest"
flag = 0
topology_file = "hello_world.virl"

def test_simulations():
    '''Given the globals, tests list of simulations APIs'''
    myvirl = vsdk.Virl(virl=VIRL, username=USERNAME, password=PASSWORD)
    sims = myvirl.getsims().json()
    if sims['simulations'] == {}: #No existing simulations
        assert sims['simulations'] == {}
    else:
        '''If there are existing simulations, keys exist'''
        assert sims['simulations'].keys()

def test_launchsim():
    ''' Launches a simulation, given the URL to the .virl file'''
    myvirl = vsdk.Virl(virl=VIRL, username=USERNAME, password=PASSWORD)
    with open(topology_file, 'r') as tf:
        payload = tf.read()
    response = myvirl.startsim(payload)
    simname = response.text
    assert response.status_code == 200
    #Clean up the simulation
    myvirl.stopsim(simname)

def test_stopsim():
    ''' Stops a given simulation, given the simulation name'''
    myvirl = vsdk.Virl(virl=VIRL, username=USERNAME, password=PASSWORD)
    with open(topology_file, 'r') as tf:
        payload = tf.read()
    response = myvirl.startsim(payload)
    simname = response.text
    #Stop the simulation
    resp = myvirl.stopsim(simname)
    assert resp.text == 'SUCCESS'

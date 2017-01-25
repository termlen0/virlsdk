#!/usr/bin/env python3

import pytest
import virlsdk.virlsdk as vsdk
#GLOBALS
VIRL = "<Your VIRL SERVER>"
USERNAME = "guest"
PASSWORD = "guest"
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

def test_status():
    ''' Start a simulation and then test that the status-check API works'''
    myvirl = vsdk.Virl(virl=VIRL, username=USERNAME, password=PASSWORD)
    with open(topology_file, 'r') as tf:
        payload = tf.read()
    response = myvirl.startsim(payload)
    simname = response.text
    response = myvirl.getstatus(simname)
    assert response.status_code == 200
    #Clean up the simulation
    myvirl.stopsim(simname)

def test_node():
    ''' Start a simulation and then test that the node-check API works'''
    myvirl = vsdk.Virl(virl=VIRL, username=USERNAME, password=PASSWORD)
    with open(topology_file, 'r') as tf:
        payload = tf.read()
    response = myvirl.startsim(payload)
    simname = response.text
    response = myvirl.getnode(simname)
    assert response.status_code == 200
    #Clean up the simulation
    myvirl.stopsim(simname)

def test_interfaces():
    ''' Start a simulation and then test that the interface-check API works'''
    myvirl = vsdk.Virl(virl=VIRL, username=USERNAME, password=PASSWORD)
    with open(topology_file, 'r') as tf:
        payload = tf.read()
    response = myvirl.startsim(payload)
    simname = response.text
    response = myvirl.getintf(simname)
    assert response.status_code == 200
    #Clean up the simulation
    myvirl.stopsim(simname)

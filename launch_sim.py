#!/bin/env python
import virlsdk as vsdk
import argparse
import yaml

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Config yaml file")
    args = parser.parse_args()
    try:
        with open(args.file) as f:
            params = yaml.load(f)
    except:
        pass
    #Instantiate the virl sdk object
    myvirl = vsdk.Virl(virl=params['virl'],username=params['username'],
                       password=params['password'])
    with open(params['topology_file']) as tf: #get the virl file
        payload = tf.read()
    response = myvirl.startsim(payload) #Start the Sim
    print(response.status_code)
    print(response.text)



if __name__ == "__main__" :
    main()

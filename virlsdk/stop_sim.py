#!/bin/env python
import virlsdk
import argparse
import yaml

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--session", help="Running session name")
    parser.add_argument("-f", "--file", help="Config yaml file")
    args = parser.parse_args()
    try:
        with open(args.file) as f:
            params = yaml.load(f)
    except:
        pass

    #Instantiate a virlsdk object
    myvirl = virlsdk.Virl(virl=params['virl'], username=params['username'],
                          password=params['password'])
    response = myvirl.stopsim(args.session)
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    main()

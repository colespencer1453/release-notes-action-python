import os
import requests  # noqa We are just importing this to prove the dependency installed correctly
import pymsteams
import json

def main():
    my_input = json.loads(os.environ["INPUT_RELEASEPAYLOAD"])
    print(my_input)
    myTeamsMessage = pymsteams.connectorcard(os.environ["INPUT_TEAMSWEBHOOK"])
    myTeamsMessage.title(str(my_input['release']['name']))
    myTeamsMessage.text(my_input['release']['body'])
    myTeamsMessage.send()


if __name__ == "__main__":
    main()

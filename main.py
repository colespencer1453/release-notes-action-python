import os
import requests  # noqa We are just importing this to prove the dependency installed correctly
import pymsteams
import json

def main():
    my_input = json.loads(os.environ["INPUT_RELEASEPAYLOAD"])
    print(my_input)
    myTeamsMessage = pymsteams.connectorcard(os.environ["INPUT_TEAMSWEBHOOK"])
    myTeamsMessage.title("Release notes for version " + str(my_input['release']['tag_name']) +" of repository: " + str(my_input['repository']['name']))
    

    # create the section
    myMessageSection = pymsteams.cardsection()

    # Section Title
    myMessageSection.title(str(my_input['release']['name']))


    # Section Text
    myMessageSection.text(str(my_input['release']['body']))

    # Add your section to the connector card object before sending
    myTeamsMessage.addSection(myMessageSection)
    myTeamsMessage.send()


if __name__ == "__main__":
    main()

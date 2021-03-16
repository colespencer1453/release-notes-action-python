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
    

    # create the section
    myMessageSection = pymsteams.cardsection()

    # Section Title
    myMessageSection.title("Section title")

    # Activity Elements
    myMessageSection.activityTitle("my activity title")
    myMessageSection.activitySubtitle("my activity subtitle")
    myMessageSection.activityImage("http://i.imgur.com/c4jt321l.png")
    myMessageSection.activityText("This is my activity Text")

    # Facts are key value pairs displayed in a list.
    myMessageSection.addFact("this", "is fine")
    myMessageSection.addFact("this is", "also fine")

    # Section Text
    myMessageSection.text("This is my section text")

    # Section Images
    myMessageSection.addImage("http://i.imgur.com/c4jt321l.png", ititle="This Is Fine")

    # Add your section to the connector card object before sending
    myTeamsMessage.addSection(myMessageSection)
    myTeamsMessage.send()


if __name__ == "__main__":
    main()

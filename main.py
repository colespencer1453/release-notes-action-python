import os
import requests  # noqa We are just importing this to prove the dependency installed correctly
import pymsteams
import json

def main():
    my_input = json.loads(os.environ["INPUT_MYINPUT"])
    print(my_input)
    myTeamsMessage = pymsteams.connectorcard("https://appriver3651001066.webhook.office.com/webhookb2/59c2a62d-30d9-498b-b5c9-add98d4bbb07@52934c9b-912c-4480-b2bc-72fee70477bb/IncomingWebhook/1bafa1bd08fa4298ad8d07f5ebe3af51/a07dc6c5-7106-49f1-88ea-3bfd14382686")
    myTeamsMessage.title(str(my_input['release']['name']))
    myTeamsMessage.text('hello')
    myTeamsMessage.send()


if __name__ == "__main__":
    main()

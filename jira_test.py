import argparse
import os

from jira import JIRA
from md_auto_module.Vault_Tool import Vault

VAULT_SERVER = Vault()
JIRA_URL = "https://jirabpzl2.mobiledrivetech.com/"

def main(issue_key, file_path):

    secret = VAULT_SERVER.read_secret(path='token')
    username = secret['JIRA_USERNAME']
    token = secret['JIRA_PASSWORD']

    jira_server = JIRA(JIRA_URL, basic_auth=(username, token))
    issue = jira_server.issue(issue_key)

    transitions = jira_server.transitions(issue)
    for transition in transitions:
        print(f"ID: {transition['id']}, Name: {transition['name']}")

    # Change state
    #transition_id = '131'  # Replace with the actual transition ID
    #JIRA_SERVER.transition_issue(ISSUE, transition_id)
    # Leave comment
    #comment = 'This is a comment left by a Python script.'
    #JIRA_SERVER.add_comment(ISSUE, comment)
    # Assign issue
    #assignee = 'new-assignee-username'
    #JIRA_SERVER.assign_issue(ISSUE, assignee)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script that takes two arguments.")
    parser.add_argument("issue_key", type=str, help="Issue Key")
    parser.add_argument("file_path", type=str, help="File Path")

    args = parser.parse_args()
    main(args.issue_key, args.file_path)
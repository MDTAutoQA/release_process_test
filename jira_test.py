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
        if transition['name'].__eq__('Build Ready'):
            transition_id = transition['id']
            # Change state
            jira_server.transition_issue(issue, transition_id)
            break

    # Leave comment
    comment = f'Click path to download the file. {file_path}]'
    jira_server.add_comment(issue, comment)
    # Assign issue
    assignee = 'MD77006'
    jira_server.assign_issue(issue, assignee)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script that takes two arguments.")
    parser.add_argument("issue_key", type=str, help="Issue Key")
    parser.add_argument("file_path", type=str, help="File Path")

    args = parser.parse_args()
    main(args.issue_key, args.file_path)
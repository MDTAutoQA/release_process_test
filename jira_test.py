import os

from jira import JIRA

JIRA_URL = "https://jirabpzl2.mobiledrivetech.com/"
USERNAME = "MD77006"
PASSWORD = "Q!p0w2o912"

JIRA_SERVER = JIRA(JIRA_URL, basic_auth=(USERNAME, PASSWORD))
ISSUE = JIRA_SERVER.issue(os.getenv('issueKey'))

transitions = JIRA_SERVER.transitions(ISSUE)
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
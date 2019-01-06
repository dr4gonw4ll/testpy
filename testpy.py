# -*- coding: utf-8 -*-
import csv
from jira import JIRA

JIRA_URL = "URL"
jira = JIRA(JIRA_URL)
auth_jira = JIRA(auth=('username', 'password'))
with open('hem.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=",")
    for field in readcsv:
        print "Printing the CSV file"
        print field
        issue_dict = {
        'project': {'key': field[5]},
        'summary': field[0],
        'duedate':field[21],
        'description': field[24],
        'issuetype': {'name': field[3]},}

        issue = jira.create_issue(fields = issue_dict)
        print issue

# Refer https://jira.readthedocs.io/en/latest/index.html
# Install dependencies "pip install jira"

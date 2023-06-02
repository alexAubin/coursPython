
import json
import os
from datetime import datetime


def _time_points_until_today():

    year = 2017
    month = 1
    day = 1
    today = datetime.today()
    date = datetime(year, month, day)

    while date < today:
        yield date

        day += 14
        if day > 15:
            day = 1
            month += 1

        if month > 12:
            year += 1
            month = 1

        date = datetime(year, month, day)

time_points_until_today = list(_time_points_until_today())

def get_lists_history():

    os.system("rm -rf ./.work")
    os.system("git clone https://github.com/YunoHost/apps ./.work/apps")

    for t in time_points_until_today:
        print(t.strftime("%b %d %Y"))

        # Fetch repo at this date
        cmd = 'cd ./.work/apps; git checkout `git rev-list -1 --before="%s" master`'
        os.system(cmd % t.strftime("%b %d %Y"))

        # Merge community and official
        merged = {}

        if os.path.exists(".work/apps/community.json"):
            community = json.loads(open(".work/apps/community.json").read())
            merged.update(community)

        if os.path.exists(".work/apps/official.json"):
            official = json.loads(open(".work/apps/officials.json").read())
            for key in official:
                official[keys]["state"] = "official"
            merged.update(official)

        # Save it
        json.dump(merged, open('./.work/merged_lists.json.%s' % t.strftime("%y-%m-%d"), 'w'))

def make_count_summary():

    states = ["official", "working", "inprogress", "notworking"]
    history = []

    per_state = { state: [] for state in states }
    per_level = { "level-%s"%i: [] for i in range(0,8) }

    for d in time_points_until_today:

        print("Analyzing %s ..." % d.strftime("%y-%m-%d"))

        # Load corresponding json
        j = json.loads(open("./.work/merged_lists.json.%s" % d.strftime("%y-%m-%d")).read())
        d_label = d.strftime("%b %d %Y")

        summary = {}
        summary["date"] = d__label
        for state in states:
            summary[state] = len([ k for k, infos in j.items() if infos["state"] == state ])

        for level in range(0,8):
            summary["level-%s"%level] = len([ k for k, infos in j.items() \
                                              if  infos["state"] in ["working", "official"] \
                                              and infos["level"] == level ])

        history.append(summary)

    json.dump(history, open('count_history.json', 'w'))
    print("Result is available as count_history.json !")

get_lists_history()
make_count_summary()

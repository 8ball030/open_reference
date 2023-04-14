import pickle


file = open("object", "rb")
profile = pickle.load(file)

print(profile.keys())

template = """
Name: {first_name} {last_name}
headline: {headline}
honors: {honors}
education: {education}
"""

first_name = profile["firstName"]
last_name = profile["lastName"]
headline = profile["headline"]

honors = profile["honors"]

education = profile["education"]

output = template.format(
    first_name=first_name,
    last_name=last_name,
    headline = headline,
    honors=honors,
    education=education
)
print(output)


def parse_education_entry(entry):
    """Parse an educational entry from linked in order to create an output."""
    school = entry["schoolName"]
    degree = entry.get("degreeName", "NA")
    grade = entry.get("grade", "NA")
    # we get a date range, we want to get the start date
    description = entry.get("description", "NA")
    if "timePeriod" not in entry:
        return f"{school} - {degree} - {grade} - NA - NA"

    time_period = entry["timePeriod"]
    start_date = time_period.get("startDate", "NA")['year']
    end_date = time_period.get("endDate", "NA")['year']

    return f"{school} - {degree} - {grade} - {start_date} - {end_date} {description}"


for i in profile['education']:
    print(parse_education_entry(i))


def parse_honors_entry(entry):
    """
    Parse an honors entry from linked in order to create an output.
    honors: [{'description': 'Grand prize from Skale for a decentralised RPC', 'title': 'Eth Amsterdam', 'issueDate': {'month': 6, 'year': 2022}, 'issuer': 'Skale'}, {'description': 'Design and implementation of a custom trading strategy', 'occupation': 'urn:li:fs_education:(ACoAAAuaTzMB8WtSVfq24uaASoHn9HQeuhbOQ6Y,522977630)', 'title': 'First Prize at Quant Zone Rule Design', 'issueDate': {'month': 4, 'year': 2020}}, {'description': 'We implemented a parking simulator built on top of Fetch.ai in order to demonstrate negotiation and matchmaking in a decentralised system.', 'title': 'Winner of Diffusion Hackathon Track - Sharing in Consortia Networks: permissioned, tokenized data sharing with T-Labs', 'issueDate': {'month': 10, 'year': 2019}, 'issuer': 'Diffusion'}, {'description': 'Fetch is a tech stack allowing Agent based modelling. My winning entry involved reinforcement learning in an environment representing bartering for Music event tickets', 'title': 'Innovation Prize Hackathon 0x2', 'issueDate': {'month': 6, 'year': 2019}, 'issuer': 'Fetch.Ai'}, {'description': 'We implemented a parking simulator built on top of Fetch.ai in order to demonstrate negotiation and matchmaking in a decentralised system.', 'title': 'Diffusion Tech Stack Prize - Fetch.AI', 'issuer': 'Diffusion'}, {'description': 'We built a P2P ride sharing app. Built in python and Node.js', 'title': 'Hackathon 0x3 Decentralised Ride Sharing - First Prize', 'issuer': 'Fetch.Ai'}]

    """
    name = entry["title"]
    issuer = entry.get("issuer", "NA")
    date = entry.get("issueDate", "NA")
    if date != "NA":
        date = f"{date['month']}/{date['year']}"
    description = entry.get("description", "NA")

    return f"{name} - {issuer} - {date} - {description}"


for i in profile['honors']:
    
    print(parse_honors_entry(i))

for i in profile['experience']:
    print(i['title'])
    print(i['companyName'])
    print(i)

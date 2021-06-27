import datetime
import locale

import requests

# Both company_id and user_token can be found by inspecting the requests made by Convenia website
# and filtering by "month"
company_id = ""  # change this with you company id
user_token = ""  # change this with your access token
members = []  # change this with the name of the members if you want it to be filtered

headers = {"authorization": f"Bearer {user_token}"}


def getBirthdays(month_number, filtered_values=[]):
    result = []
    month_start = datetime.datetime(2021, month_number + 1, 1)
    result.append(f"\nMês: {month_start.strftime('%B')}")

    request = requests.get(
        f"https://core.convenia.com.br/api/v1/companies/{company_id}/calendars/month?reference_date={month_start.timestamp()}",
        headers=headers,
    )
    if request.status_code == 401:
        raise ValueError("401 - Token inválido")
    elif request.status_code == 200:
        data = request.json()["data"]
        birthdays = []
        for event in data:
            if event["category"] == "birthday":
                birthdays.append(event)

        birthdays.sort(key=lambda x: x["start_date"])

        for event in birthdays:
            if filtered_values == [] or any(
                team_member.lower() in event["event"].lower()
                for team_member in filtered_values
            ):
                result.append(event["start_date"] + " - " + event["event"])
        if len(result) == 1:
            return []
        else:
            return result


locale.setlocale(locale.LC_ALL, "pt_BR")
print("Buscando aniversários...")
birthdays = []
for month in range(12):
    birthdays += getBirthdays(month, filtered_values=members)

for birthday in birthdays:
    print(birthday)

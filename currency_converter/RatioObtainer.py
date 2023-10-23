import json, datetime, urllib.request, creds

class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        try:
            f = open("ratios.json")
            currency_file = json.load(f)
            f.close()
            for i in range(len(currency_file)):
                if currency_file[i]["base_currency"] == self.base and currency_file[i]["target_currency"] == self.target:
                    date = datetime.datetime.strptime(currency_file[i]["date_fetched"], "%Y-%m-%d")
                    date = date.date()
                    if date == datetime.date.today():
                        return True
        except:
            return False

    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        response = urllib.request.urlopen(creds.api)
        httpresponse = response.read()
        data = json.loads(httpresponse)
        ratio = data["quotes"][self.base+self.target]
        self.save_ratio(ratio)


    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        f = open("ratios.json")
        currency_file = json.load(f)
        f.close()
        for i in range(len(currency_file)):
            if currency_file[i]["base_currency"] == self.base and currency_file[i]["target_currency"] == self.target:
                date = datetime.date.today()
                currency_file[i]["date_fetched"] = "{}".format(date)
                currency_file[i]["ratio"] = ratio
                f = open("ratios.json", "w")
                json.dump(currency_file, f, indent=4)
                f.close()
                break
        else:
            json_dic = {
                "base_currency": "{}".format(self.base),
                "target_currency": "{}".format(self.target),
                "date_fetched": "{}".format(datetime.date.today()),
                "ratio": ratio
            }
            currency_file.append(json_dic)
            f = open("ratios.json", "w")
            json.dump(currency_file, f, indent=4)
            f.close()

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        f = open("ratios.json")
        currency_file = json.load(f)
        f.close()
        for i in range(len(currency_file)):
            if currency_file[i]["base_currency"] == self.base and currency_file[i]["target_currency"] == self.target:
                return currency_file[i]["ratio"]

# base="XDD"
# target="CFF"
# ratio = 131313
# f = open("ratios.json")
# currency_file = json.load(f)
# f.close()
# print(len(currency_file))
#
# for i in range(len(currency_file)):
#     if currency_file[i]["base_currency"] == base and currency_file[i]["target_currency"] == target:
#         date = datetime.date.today()
#         currency_file[i]["date_fetched"] = "{}".format(date)
#         currency_file[i]["ratio"] = ratio
#         with open("ratios.json","w") as f:
#             json.dump(currency_file, f, indent=4)
#         break
# else:
#     print("działa else")
#     json_dic = {
#         "base_currency": "{}".format(base),
#         "target_currency": "{}".format(target),
#         "date_fetched": "{}".format(datetime.date.today()),
#         "ratio": ratio
#     }
#     currency_file.append(json_dic)
#     with open("ratios.json", "w") as f:
#         json.dump(currency_file, f, indent=4)



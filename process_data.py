import re
import json

with open("data/raw_florida_free_association_norms.txt", "r") as data:
    text = data.read()

    text = re.sub('<.*?>', '', text)
    text = re.sub('"', '', text)
    text = re.sub(r'\\n', "", text)

    text = re.sub(r"NO. OF CUES:  (\d*)", r"NO. OF CUES:  \1 ~~", text)

    matches = re.findall(r'(.*?)~~', text, flags=re.DOTALL)
    fin_data = dict()
    for match in matches:

        header = re.search(r"(\w*.*)(FSG   BSG  MSG  OSG  QSS TSS  QFR TFR   QMC   TMC   QUC TUC)", match)
        associations = re.findall(r"(............)(.\...)(.\....)(.\....)(.\.....)(....)"
                                  r"(....)(.....)(.....)(...\...)(..\...)(.....)(....)", match)

        fin_data[header[1].strip()] = {}
        for association in associations:
            fin_data[header[1].strip()][association[0].strip()] = []
            for value in association[1:]:
                fin_data[header[1].strip()][association[0].strip()].append(value.strip())

    with open("data/UCLFAN.json", "w") as destination:
        json.dump(fin_data, destination)



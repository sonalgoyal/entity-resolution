"""Deduplicate customer records with the Zingg Python API.

Same job as config.json, written in Python. Run it inside the Zingg Docker
image, passing the phase on the command line:

  zingg.sh --properties-file config/zingg.conf \
      --run /tutorials/01-deduplicate-customer-records/dedupe_customers.py \
      --phase findTrainingData
"""

import sys

from zingg.client import Arguments, ClientOptions, FieldDefinition, MatchType, Zingg
from zingg.pipes import CsvPipe

args = Arguments()

# 1. Describe the fields and how each one should be compared.
#    "id" is carried through to the output but never used for matching.
fields = [FieldDefinition("id", "string", MatchType.DONT_USE)]
for name in ["fname", "lname", "stNo", "add1", "add2", "city", "areacode", "state", "dob", "ssn"]:
    fields.append(FieldDefinition(name, "string", MatchType.FUZZY))
args.setFieldDefinition(fields)

# 2. Where the model and labelled pairs are stored.
args.setModelId("customers-python")
args.setZinggDir("/tmp/zingg-models")
args.setNumPartitions(4)
args.setLabelDataSampleSize(0.5)

# 3. Input and output.
schema = (
    "id string, fname string, lname string, stNo string, add1 string, "
    "add2 string, city string, areacode string, state string, dob string, ssn string"
)
args.setData(CsvPipe("customers", "examples/febrl/test.csv", schema))
args.setOutput(CsvPipe("output", "/tmp/customers-deduped-python"))

# 4. Run the phase given on the command line (findTrainingData, label, train, match ...).
options = ClientOptions(sys.argv[1:])
Zingg(args, options).initAndExecute()

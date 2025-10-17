# imports
import os
import csv
import sys
from rdkit import Chem
from druglikeness.deepdl import DeepDL

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

def drug_likeness(smiles_list):
    PATH_TO_MODEL = os.path.join(root, "..", "..", 'checkpoints', "extended-20250618.ckpt")
    model = DeepDL.from_pretrained(PATH_TO_MODEL, device="cpu")
    scores = model.screening(smiles_list=smiles_list, naive=False, batch_size=64)
    return scores

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

print(smiles_list)
# drug_likeness
outputs = drug_likeness(smiles_list)
print(outputs)
#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["drug_likeness"])
    for o in outputs:
        writer.writerow([o])
